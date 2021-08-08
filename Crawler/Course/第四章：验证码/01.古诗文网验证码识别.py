#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 10/27/2020 2:54 PM
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


def getCodeText(codeByte):
    with open('./randCode.jpg', 'wb') as fp:
        fp.write(codeByte)

def inputCode():
    code = input('请输入验证码：\n')
    return code


if __name__ == '__main__':
    login_url = 'http://so.gushiwen.cn/user/collect.aspx'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    }

    '''识别验证码'''
    login_page = requests.get(url=login_url, headers=headers).text
    tree = etree.HTML(login_page)

    # codeUrl = 'https://so.gushiwen.cn/RandCode.ashx'
    codeUrl = 'https://so.gushiwen.cn' + tree.xpath('//*[@id="imgCode"]/@src')[0]
    codeByte = requests.get(url=codeUrl, headers=headers).content

    ## 调用第三方验证码识别的接口
    # code = getCode(codeByte, 1902)

    ## 肉眼识别验证码


    with open('./randCode.jpg', 'wb') as fp:
        fp.write(codeByte)
    code = input('请输入验证码：\n')
    '''识别验证码'''
    # 登录
    data = {
    '__VIEWSTATEGENERATOR': 'C93BE1AE',
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '871437338@qq.com',
    'pwd': 'zx454049162~',
    'code': code,
    'denglu': '登录'
    }

    response = requests.post(url=login_url, headers=headers, data=data)
    page_text = response.text

    with open('test.html', 'w', encoding='utf-8') as f:
        f.write(page_text)







