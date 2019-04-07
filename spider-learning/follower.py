import json
import requests
try:
    import cookielib
except:
    import http.cookiejar as cookielib


baiduagent = 'mozilla/5.0 (compatible; baiduspider/2.0; +http://www.baidu.com/search/spider.html)'
agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
headers = {
    "Host": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/",
    'User-Agent': baiduagent
}


class Follower(object):
    count = 0

    def __init__(self):
        self.id = ''  # url_token
        self.name = ''
        self.gender = -1  # male: 1, female: 0, unknown: -1
        self.location = ''
        self.location_id = ''
        self.school = ''
        self.school_id = ''
        self.business = ''
        self.business_id = ''
        self.answer_count = 0  # 回答数
        self.articles_count = 0  # 文章数
        self.columns_count = 0  # 文章数
        self.question_count = 0  # 提问数
        self.following_count = 0  # 关注数
        self.follower_count = 0  # 粉丝数
        self.logs_count = 0  # 参与公共编辑数
        self.favorite_count = 0  # 收藏夹数
        self.participated_live_count = 0  # 参与的live数
        self.hosted_live_count = 0  # 举办的live数
        self.following_question_count = 0  # 关注的问题数
        self.following_topic_count = 0  # 关注的话题数
        self.voteup_count = 0  # 获得的赞同数
        self.favorited_count = 0  # 获得的被收藏数
        self.thanked_count = 0  # 获得的感谢数
        self.following_favlists_count = 0  # 收藏的收藏夹数
        self.is_bind_sina = False

    def set_follower(self, follower_id, authorization):
        try:
            Follower.count += 1
            self.id = follower_id
            follower_info = self.query_by_id(follower_id, authorization)
            if follower_info["error"] is False:
                self.name = follower_info["name"]
                self.gender = follower_info["gender"]
                if "locations" in follower_info and len(follower_info["locations"]) != 0 and follower_info["locations"][0]["id"] != "":
                    self.location = follower_info["locations"][0]["name"]
                    self.location_id = follower_info["locations"][0]["id"]

                else:
                    self.location_id = ""
                    self.location = ""
                if "educations" in follower_info and len(follower_info["educations"]) != 0 and "school" in follower_info["educations"][0] and follower_info["educations"][0]["school"]["id"] != "":
                    self.school = follower_info["educations"][0]["school"]["name"]
                    self.school_id = follower_info["educations"][0]["school"]["id"]
                else:
                    self.school = ""
                    self.school_id = ""
                if "business" in follower_info and len(follower_info["business"]) != 0 and follower_info["business"]["id"] != "":
                    self.business = follower_info["business"]["name"]
                    self.business_id = follower_info["business"]["id"]
                else:
                    self.business = ""
                    self.business_id = ""
                self.answer_count = follower_info["answer_count"]  # 回答数
                self.articles_count = follower_info["articles_count"]  # 文章数
                self.columns_count = follower_info["columns_count"]  # 文章数
                self.question_count = follower_info["question_count"]  # 提问数
                self.following_count = follower_info["following_count"]  # 关注数
                self.follower_count = follower_info["follower_count"]  # 粉丝数
                self.logs_count = follower_info["logs_count"]  # 参与公共编辑数
                self.favorite_count = follower_info["favorite_count"]  # 收藏夹数
                self.participated_live_count = follower_info["participated_live_count"]  # 参与的live数
                self.hosted_live_count = follower_info["hosted_live_count"]  # 举办的live数
                self.following_question_count = follower_info["following_question_count"]  # 关注的问题数
                self.following_topic_count = follower_info["following_topic_count"]  # 关注的话题数
                self.voteup_count = follower_info["voteup_count"]  # 获得的赞同数
                self.favorited_count = follower_info["favorited_count"]  # 获得的被收藏数
                self.thanked_count = follower_info["thanked_count"]  # 获得的感谢数
                self.following_favlists_count = follower_info["following_favlists_count"]  # 收藏的收藏夹数
                return True
            else:
                # print(str(Follower.count) + ": " + follower_info["failure_info"])
                return False
        except Exception as e:
            print("2--"+repr(e))
            print("Set follower error: " + follower_id)
            return False

    def query_by_id(self, query_id, authorization):
        url = 'https://www.zhihu.com/api/v4/members/' + query_id

        baiduagent = 'mozilla/5.0 (compatible; baiduspider/2.0; +http://www.baidu.com/search/spider.html)'
        headers = {
            "Host": "www.zhihu.com",
            "Referer": "https://www.zhihu.com/people/" + query_id + "/activities",
            'User-Agent': baiduagent,
            "authorization": authorization
        }

        payload = {
            "include": "locations,employments,gender,educations,business,voteup_count,thanked_count,follower_count,following_count,following_topic_count,following_question_count,following_favlists_count,following_columns_count,answer_count,articles_count,question_count,columns_count,commercial_question_count,favorite_count,favorited_count,logs_count,marked_answers_count,marked_answers_text,is_active,is_bind_sina,is_privacy_protected,sina_weibo_url,hosted_live_count,participated_live_count"
        }
        s = requests.session()
        s.cookies = cookielib.LWPCookieJar(filename='cookies')
        try:
            s.cookies.load(ignore_discard=True)
        except Exception as e:
            print("Cookie 未能加载")

        page = s.get(url, headers=headers, params=payload)
        if page.status_code == 200:
            json_data = json.loads(page.text)
            json_data["error"] = False
        else:
            json_data = {
                "error": True,
                "failure_info": "Query Failure, link: " + query_id + ", Failure code: " + (str)(page.status_code)
            }
        return json_data

    def __str__(self):
        return 'id: ' + self.id + ', ' + 'name: ' + self.name





