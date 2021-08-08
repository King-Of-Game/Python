# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 9/22/2020 7:56 PM
# __software__ : PyCharm

import time
import requests
from lxml import etree

urls = [
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16488',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16583',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16380',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16911',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16581',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16674',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16112',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/17343',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16659',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16449',
]

headers = {
            'Referer': 'http://www.yhdongman.com/show/21129-37287-0.html',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
        }

def getTitle(url, index):
    response = requests.get(url, headers)
    html = response.content
    title = etree.HTML(html).xpath('//div[@id="title"]/text()')[0]
    print('第%d个title：%s' % (index, title))


if __name__ == '__main__':
    start = time.time()
    for i in range(len(urls)):
        s = time.time()
        getTitle(urls[i], i+1)
        print('第%s个title爬取耗时：%.5f秒' % (i+1, float(time.time() - s)))
    print('爬取总耗时：%.5f秒' % float(time.time()-start))

