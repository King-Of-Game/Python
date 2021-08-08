#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 11/8/2020 4:00 PM
# __software__ : PyCharm


from selenium import webdriver
# 实现无可视化界面
from selenium.webdriver.chrome.options import Options
# 实现selenium规避
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
# 超级鹰
from chaojiying import Chaojiying_Client
# 用来截取图片局部区域
from PIL import Image

import time


# 通过超级鹰破解验证码
def getCode(imgByte, codeType):
    chaojiying = Chaojiying_Client('zx454049162', '454049162', '909168')  # 用户中心>>软件ID 生成一个替换 96001
    # print(chaojiying.PostPic(imgByte, codeType))  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    result = chaojiying.PostPic(imgByte, codeType)['pic_str']
    return result


# 自动点击验证码
def click_code_img(code_img):
    pass


# 实现无可视化界面（无头浏览器）
def main(browser):
    url = 'https://kyfw.12306.cn/otn/resources/login.html'

    browser.get(url)
    time.sleep(1)
    # 切换成账号密码登录
    browser.find_elements_by_link_text('账号登录')[0].click()
    time.sleep(1)
    # 输入账号和密码
    browser.find_elements_by_id('J-userName')[0].send_keys('17762411423')
    time.sleep(0.5)
    browser.find_elements_by_id('J-password')[0].send_keys('zx454049162_')
    # 找到验证码图片所在标签元素
    code_img = browser.find_element_by_xpath('//*[@id="J-loginImg"]')

    '''
    得到验证码图片方法一
    '''
    # img_data = code_img.screenshot_as_png
    # with open('./random_code.png', 'wb') as fp:
    #     fp.write(img_data)

    '''
    得到验证码图片方法二
    '''
    # 将当前页面进行截图并保存
    browser.save_screenshot('./login_page.png')
    # 确定验证码图片对应的左上角和右下角的坐标（确定裁剪的区域）
    location = code_img.location  # 获取元素左上角的x, y坐标
    size = code_img.size  # 元素的宽高
    # 左上角和右下角的坐标：x1, y1, x2, y2
    x1 = location['x']
    y1 = location['y']
    x2 = location['x'] + size['width']
    y2 = location['y'] + size['height']
    box = (x1, y1, x2, y2)  # # 根据左上角和右下角的坐标（确定裁剪的区域）

    img = Image.open('./login_page.png')
    # 根据指定区域进行图片裁剪
    frame = img.crop(box)  # 得到了图片验证码那一小块区域
    frame.save('./random_code.png')
    time.sleep(1)

    # 使用超级鹰识别图片验证码
    im = open('./random_code.png', 'rb').read()
    result = getCode(im, 9004)
    print(result)
    # 获取等待点击图片的坐标位置
    positions = result.split('|')
    time.sleep(0.5)

    for xy in positions:
        x = int(xy.split(',')[0])
        y = int(xy.split(',')[1])
        print(xy)
        # 动作链
        action = webdriver.ActionChains(browser)
        action.move_to_element_with_offset(code_img, x, y).click().perform()
        action.release()
        time.sleep(0.5)

    # 点击登录
    browser.find_elements_by_id('J-login')[0].click()
    time.sleep(0.5)
    # 选中滑块元素
    btn_slide = browser.find_elements_by_id('nc_1_n1z')[0]
    # 实例化动作链
    action = webdriver.ActionChains(browser)
    # 点击长按指定的标签
    action.click_and_hold(btn_slide)
    # 处理滑动模块
    for i in range(5):
        action.move_by_offset(xoffset=30, yoffset=0).perform()
        time.sleep(0.3)
    # 释放动作链
    action.release()

    # browser.quit()


if __name__ == '__main__':
    '''
     创建一个参数对象，用来控制chrome以无界面模式打开
    '''
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    # browser = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)

    '''
     如何实现让selenium规避被检测到的风险
    '''
    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser = webdriver.Chrome(executable_path='D:\Google\Chrome\Application/chromedriver.exe', options=option)
    browser.maximize_window()  # 设置浏览器窗口最大化
    
    main(browser)
