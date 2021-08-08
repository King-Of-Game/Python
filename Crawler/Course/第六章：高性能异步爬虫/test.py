#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 11/1/2020 10:19 PM
# __software__ : PyCharm

import requests
import random
import re

#这段url的conId对不同视频爬取的时候也需要修改
url = "https://www.pearvideo.com/videoStatus.jsp?contId=1704500&mrd="

#生成mrd
ran = ['0.']
for i in range(0,18):
    ran.append(str(random.randint(0,9)))
print(ran)
a = ''.join(ran)


headers = {
        "Referer": "https://www.pearvideo.com/video_1704500",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.63",
}

#对应的视频不一样，conId也要进行相对应的修改
data = {
    'contId': '1704500',
    'mrd': str(a)
}

url = url+str(a)

response = requests.get(url=url,headers=headers, params=data)

page_text = response.text

print(page_text)

#利用正则进行src的提取
re_url = r'srcUrl":"(.*)"}'

src = re.findall(re_url, page_text, re.S)[0]

print(src)