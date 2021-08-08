#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
import requests
import lxml.html
from requests.exceptions import RequestException


def WeatherAPI():

    content = Text1.get('0.0', END)  # 获取文本框中输入的查询城市
    content = content.strip()  # .strip()就是把这个字符串头和尾的空格去掉

    if content == "":
        messagebox.showinfo('提示', '请输入查询的城市')
        Text1.delete(0.0, END)
    else:
        # ******************** 先从这个网站得到每个城市对应的编码 ********************
        url = 'https://www.cnblogs.com/Rhythm-/p/9255190.html'
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
            'Referer': 'https://www.cnblogs.com/'
        }

        request = requests.post(url=url, headers=header)
        data = request.text
        # print(data)  # 打印网页的内容
        select = lxml.html.document_fromstring(data)
        city = select.xpath('//div[@id="cnblogs_post_body"]/p/text()')

        cityNameList = []
        cityNumberList = []
        for i in range(len(city)):
            temp = city[i].split(',')
            cityNameList.append(temp[0])
            cityNumberList.append(temp[1])
        try:
            cityNameIndex = cityNameList.index(content)
            cityNumber = cityNumberList[cityNameIndex]
            print(cityNameList)
            print(cityNumberList)
        except Exception as e:
            print(e)
            messagebox.showinfo('提示', '查询不到该城市，请重新输入！')
            Text1.delete(0.0, END)
        # ******************** 先从这个网站得到每个城市对应的编码 ********************



        weatherAPI = 'http://www.weather.com.cn/weather1d/%s.shtml' % cityNumber
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7'
        }
        print(weatherAPI)
        request = requests.get(url=weatherAPI, headers=headers)
        data = request.content
        data = data.decode('utf-8')
        # print(data)  # 打印网页的内容

        select = lxml.html.document_fromstring(data)  # 用lxml模块解析网站内容

        # 得到天气最后更新时间
        # nowDate = datetime.datetime.now().strftime('%Y-%m-%d')  # 获取当前时间
        updateTime = select.xpath('//input[@id="fc_24h_internal_update_time"]/@value')  # 用lxml模块得到最后更新时间
        updateTime = updateTime[0]

        # 得到当日气温
        nowWeather = select.xpath('//input[@id="hidden_title"]/@value')
        nowWeather = nowWeather[0]

        # 得到空气污染扩散指数
        result1 = select.xpath('//li[@class="li6 hot"]/span/text()')
        result2 = select.xpath('//li[@class="li6 hot"]/p/text()')
        print(result1)
        pollutionIndex = '%s（%s）' % (result1[0], result2[0])

        # 得到紫外线指数
        result1 = select.xpath('//li[@class="li1 hot"]/span/text()')
        result2 = select.xpath('//li[@class="li1 hot"]/p/text()')
        uvIndex = '%s（%s）' % (result1[0], result2[0])

        # 得到穿衣指数
        result1 = select.xpath('//li[@class="li3 hot"]/a/span/text()')
        result2 = select.xpath('//li[@class="li3 hot"]/a/p/text()')
        dressingIndex = '%s（%s）' % (result1[0], result2[0])



        # 把最后更新时间输出到文本框里面
        Text2.delete(0.0, END)
        Text2.insert(INSERT, "%s" % updateTime)

        # 把当日天气输出到文本框里面
        Text3.delete(0.0, END)
        Text3.insert(INSERT, "%s" % nowWeather)

        # 把当日污染指数输出到文本框里面
        Text4.delete(0.0, END)
        Text4.insert(INSERT, "%s" % pollutionIndex)

        # 把当日紫外线指数输出到文本框里面
        Text5.delete(0.0, END)
        Text5.insert(INSERT, "%s" % uvIndex)

        # 把当日穿衣指数输出到文本框里面
        Text6.delete(0.0, END)
        Text6.insert(INSERT, "%s" % dressingIndex)









# 绘制窗体
root = Tk()
root.title("天气查询")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
w = int((width-462)/2)
h = int((height-190)/2)
root.geometry('462x190+%s+%s' % (w, h))

label1 = Label(root, text='请输入查询城市：', fg='black')
label1.grid(row=0, column=0, sticky=E)
Text1 = Text(root, width=22, height=1, font=('微软雅黑', 10))
Text1.grid(row=0, column=1, sticky=W)
label2 = Label(root, text='最后更新时间：')
label2.grid(row=1, column=0, sticky=E)
Text2 = Text(root, width=44, height=1, font=('微软雅黑', 10))
Text2.grid(row=1, column=1, sticky=W)
label3 = Label(root, text='当日气温：')
label3.grid(row=2, column=0, sticky=E)
Text3 = Text(root, width=44, height=1, font=('微软雅黑', 10))
Text3.grid(row=2, column=1, sticky=W)
label4 = Label(root, text='空气污染指数：')
label4.grid(row=3, column=0, sticky=E)
Text4 = Text(root, width=44, height=1, font=('微软雅黑', 10))
Text4.grid(row=3, column=1, sticky=W)
label5 = Label(root, text='紫外线指数：')
label5.grid(row=4, column=0, sticky=E)
Text5 = Text(root, width=44, height=1, font=('微软雅黑', 10))
Text5.grid(row=4, column=1, sticky=W)
label6 = Label(root, text='穿衣指数：')
label6.grid(row=5, column=0, sticky=E)
Text6 = Text(root, width=44, height=1, font=('微软雅黑', 10))
Text6.grid(row=5, column=1, sticky=W)
button1 = Button(root, text='查询', width=8, command=WeatherAPI)
button1.grid(row=6, column=0, sticky=W, pady=25)
button2 = Button(root, text='退出', width=8, command=root.quit)
button2.grid(row=6, column=1, sticky=E, pady=25)






# 消息循环
root.mainloop()






