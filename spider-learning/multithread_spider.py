import re
import json
import requests
from follower import Follower
from bs4 import BeautifulSoup
import threading
from queue import Queue
import os
import time
import send_to_db
try:
    from PIL import Image
except:
    pass
try:
    import cookielib
except:
    import http.cookiejar as cookielib


class EmptyStateError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


index_url = 'http://www.zhihu.com'
phone_login_url = 'https://www.zhihu.com/login/phone_num'


baiduagent = 'mozilla/5.0 (compatible; baiduspider/2.0; +http://www.baidu.com/search/spider.html)'
agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
macagent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:41.0) Gecko/20100101 Firefox/41.0'

phone_data = {
    'phone_num': '15373222439',
    'password': 'zhaotong0312',
}


headers = {
"Host": "www.zhihu.com",
"Referer": "https://www.zhihu.com/",
'User-Agent': macagent
}

query_headers = headers
query_headers["x-hd-token"] = "hello"
query_headers["X-UDID"] = "AGCCUUE-TwyPTteQ2nphO1KeknEKk9cgDhI="

payload = {
"include": "data[*].gender, is_followed,is_following",
"limit": "20",
}


def write_log(log_file, log):
    with open(log_file, "a") as f:
        f.write(log + "\n")
        f.close()


def get_xsrf(session):
    r = session.get(index_url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    try:
        xsrf = soup.find('input', {'name':'_xsrf', 'type':'hidden'}).get('value')
    except Exception as e:
        print(repr(e))
        unhuman_captcha(session)
        session.get()
    return xsrf


def get_authorization(cookiefile):
    with open(cookiefile, "r") as c:
        string = c.read()
        c.close()
    pattern = re.compile(r'z_c0=.*\\""')
    search = pattern.search(string)
    return "Bearer " + search.group(0).split('\\\"')[1]


def unhuman_captcha(session):
    url = "https://www.zhihu.com/api/v4/anticrawl/captcha_appeal"
    session.cookies = cookielib.LWPCookieJar(filename='cookies')
    authorization = get_authorization("cookies")
    query_headers["authorization"] = authorization
    r = session.get(url, headers=query_headers)
    with open('captcha.jpg', 'wb') as f:
        f.write(r.content)
        f.close()
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        print(u'请到 %s 目录找到captcha.jpg 手动输入' % os.path.abspath('captcha.jpg'))
    captcha = input("please input the captcha\n>").strip()
    return captcha


def get_captcha(session):
    t = str(int(time.time() * 1000))
    captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
    r = session.get(captcha_url, headers=headers)
    with open('captcha.jpg', 'wb') as f:
        f.write(r.content)
        f.close()
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        print(u'请到 %s 目录找到captcha.jpg 手动输入' % os.path.abspath('captcha.jpg'))
    captcha = input("please input the captcha\n>").strip()
    return captcha


def is_login(session):
    profile_url = "https://www.zhihu.com/settings/profile"
    login_code = session.get(profile_url, headers=headers, allow_redirects=False).status_code
    if login_code == 200:
        return True
    else:
        return False


def login(session, account, password, login_url):
    xsrf = get_xsrf(session)
    headers["X-Xsrftoken"] = xsrf
    headers["X-Requested-With"] = "XMLHttpRequest"
    postdata = {
        '_xsrf': xsrf,
        'password': password,
        'phone_num': account
    }
    # try to login without captcha

    login_req = session.post(login_url, headers=headers, data=postdata)
    login_code = login_req.json()
    if login_code['r'] == 1:
        # login failed, we need captcha
        postdata["captcha"] = get_captcha(session)
        login_req = session.post(login_url, headers=headers, data=postdata)
        login_code = login_req.json()
        print(login_code['msg'])

    # save cookies
    session.cookies.save()
    print('成功登陆')

# combine the set_follower and send_to_db
def set_and_send_follower(conn, cursor, person, authorization):
    f = Follower()
    if f.set_follower(person["url_token"], authorization):
        send_to_db.send_f(cursor, f)
        conn.commit()
        cursor.close()
        conn.close()
    else:
        person_fail_info = "person=" + person["url_token"]
        write_log("person_failure_log", person_fail_info)


def get_followers(session, user_token_id, page_start, page_end):
    count = 0
    count_should_be = 0

    authorization = get_authorization("cookies")
    query_headers["authorization"] = authorization

    for i in range(page_start, page_end):
        this_page_url = 'https://www.zhihu.com/people/' + user_token_id + '/followers?page=' + str(i)
        query_url = 'https://www.zhihu.com/api/v4/members/' + user_token_id + '/followers'
        payload["offset"] = i * 20
        query_headers["Referer"] = this_page_url

        try:
            # get followers list
            json_meta_data = session.get(query_url, headers=query_headers, params=payload)
            json_data = json.loads(json_meta_data.text, encoding="utf8")
            threads = []

            for person in json_data["data"]:
                conn = send_to_db.connect_db(send_to_db.config)
                cursor = send_to_db.get_cursor(conn)
                count_should_be += 1
                # set_and_send_follower(conn, cursor, person, authorization)
                t = threading.Thread(target=set_and_send_follower, args=(conn, cursor, person, authorization))
                threads.append(t)
            for t in threads:
                t.setDaemon(True)
                t.start()
            for t in threads:
                t.join()

        except KeyError as ke:
            print("0--" + repr(ke))
            page_fail_info = "page=" + str(i) + ". Failure code: " + ke.__str__()
            with open("page_failure_log", "a") as f:
                f.write(page_fail_info + "\n")
                f.close()
        except requests.exceptions.RequestException as rerr:
            print("1--" + repr(rerr))
            page_fail_info = "page=" + str(i) + ". Failure code: " + str(json_meta_data.status_code)
            write_log("page_failure_log", page_fail_info)
            time.sleep(600)
            if is_login(session):
                print("继续运行")
            else:
                login(session, phone_data['phone_num'], phone_data['password'], phone_login_url)

    return count, count_should_be


if __name__ == '__main__':
    # load cookies from file
    session = requests.session()
    session.cookies = cookielib.LWPCookieJar(filename='cookies')

    try:
        session.cookies.load(ignore_discard=True)
    except:
        print("page_session Cookie 未能加载")

    if is_login(session):
        print('您已经登录')
    else:
        login(session, phone_data['phone_num'], phone_data['password'], phone_login_url)

    # print(get_followers(session, 'zhang-jia-wei', 55746, 73000))


