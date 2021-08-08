#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 10/29/2020 6:50 PM
# __software__ : PyCharm

from CodeClass import Chaojiying_Client
from lxml import etree
import requests



def getCode(imgByte, codeType):
    chaojiying = Chaojiying_Client('zx454049162', '454049162', '909168')  # 用户中心>>软件ID 生成一个替换 96001
    print(chaojiying.PostPic(imgByte, codeType))  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    json = chaojiying.PostPic(imgByte, codeType)
    result = json['pic_str']
    print('result:%s' % result)
    return result


if __name__ == '__main__':
    session = requests.Session()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    }
    # 未登录状态url
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

    '''识别验证码'''
    login_page = session.get(url=url, headers=headers).text
    tree = etree.HTML(login_page)
    img_src = 'https://so.gushiwen.cn' + tree.xpath('//*[@id="imgCode"]/@src')[0]
    codeByte = session.get(url=img_src, headers=headers).content


    ## 调用第三方验证码识别的接口
    # code = getCode(codeByte, 1902)
    # print(code)

    ## 肉眼识别验证码

    with open('./randCode.jpg', 'wb') as fp:
        fp.write(codeByte)
    code = input('请输入验证码：\n')
    '''识别验证码'''


    # 登录'
    data = {
        '__VIEWSTATE': 'n5iQatsqryOxLUa3Jn5TBOI2rL+h0yV/2haFS2pQX9zE061mbGTdYI5+IxYm12LwRybtecESOttj4ZCWDYMXho6uyltaqRIANthVQbzSRZpZl9Uv/aztL+WvML8=',
        '__VIEWSTATEGENERATOR': 'C93BE1AE',
        'from': 'http://so.gushiwen.cn/user/collect.aspx',
        'email': '871437338@qq.com',
        'pwd': 'zx454049162~',
        'code': code,
        'denglu': '登录',
    }

    login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
    response = session.post(url=login_url, headers=headers, data=data)
    # print('页面响应状态码：', response.status_code)

    # 爬取当前用户的个人主页对应的页面数据
    detail_url = 'https://so.gushiwen.cn/user/collect.aspx?sort=t'
    detail_page = session.get(url=detail_url, headers=headers).text
    with open('detail.html', 'w', encoding='utf8') as fp:
        fp.write(detail_page)




