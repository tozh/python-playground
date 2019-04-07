import requests
import json
import re
import os
from bs4 import BeautifulSoup


# def extract(str, substr1, substr2):
#     return str.split(substr1, 1)[-1].split(substr2, 1)[0]

# 使用BeautifulSoup库
url = 'http://www.zhihu.com/question/62692821'
kv = {'user-agent':'Mozilla/5.0'}
local_dir = '/Users/zhaotong/'
local_path = local_dir+url.split('/')[-1] + '.html'
demo = ''
r = requests.get(url, headers=kv)
print(r.status_code)
issue = json.loads(r.text)
print(issue)



# img_dir = '/Users/zhaotong/'+local_path.split('/')[-1].split('.')[0]
# if not os.path.exists(img_dir):
#     os.mkdir(img_dir)
#     img_dir += '/'

# for child in bs.descendants:
#     if child.name == 'img':
#         img_url = child.get('data-original')
#         if img_url is not None:
#             img_path = img_dir + img_url.split('/')[-1]
#             try:
#                 if not os.path.exists(img_path):
#                     r_img = requests.get(img_url, headers= kv)
#                     r_img.raise_for_status()
#                     with open(img_path,'wb') as f:
#                         f.write(r_img.content)
#                         f.close()
#                         print("pic is successfully written.")
#                 else:
#                     print('the pic has been exists')
#             except:
#                 print("pic error")
#


# 通用代码框架
# 输入百度关键词查询 添加params
# 百度查询关键词API: http://www.baidu.com/s?wd=keyword
# kw = {'wd':'Python'}
# ua = {'user-agent':'Mozilla/5.0'}

# 保存目标图片
# url = 'http://www.baidu.com/img/bd_logo1.png'
# local_dir = '/Users/zhaotong/'
# local_path = local_dir+url.split('/')[-1]
#
# try:
#     if not os.path.exists(local_dir):
#         os.mkdir(local_dir)
#     if not os.path.exists(local_path):
#         r = requests.get(url)
#         r.raise_for_status()
#         with open(local_path,'wb') as f:
#             # f = open(local_path, 'wb')
#             f.write(r.content)
#             f.close()
#             print("pic is successfully written.")
#     else:
#         print('the pic has been exists')
# except:
#     print("error")


# 添加headers user-agent
# kv = {'user-agent':'Mozilla/5.0'}
# url = 'http://www.baidu.com'
# try:
#     f = requests.get(url, headers=kv, timeout=30)
#     f.raise_for_status()
#     f.encoding = f.apparent_encoding
#     print(f.request.headers)
# except:
#     print("Exception happend")

# 两个通用函数
# def get_html_text(url, user_agent):
#     try:
#         f = requests.get(url, headers=user_agent, timeout=30)
#         f.raise_for_status()
#         f.encoding = f.apparent_encoding
#     except:
#         return "Exception happend."
#
#     else:
#         return f.text
#
# def get_html_head(url):
#     try:
#         h = requests.head(url, timeout=30)
#         h.raise_for_status()
#         h.encoding = h.apparent_encoding
#     except:
#         return "Head exceprion happend."
#     else:
#         return h.headers
#
# if __name__ == "__main__":
#     url = "http://www.baidu.com"

