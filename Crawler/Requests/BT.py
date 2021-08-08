# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 2019/10/21 22:41
# __software__ : PyCharm

from tkinter import *
from tkinter import messagebox
# import tkinter.scrolledtext as scrolledtext

import time, threading
import requests
import lxml.html


class Crawler:
    # 初始化类的一些属性和方法
    def __init__(self):
        '''
        https://www.cltt14.xyz/search/苍井空_ctime_1.html
            爬虫需要的字段https://www.cltt14.xyz/search/%E8%8B%8D%E4%BA%95%E7%A9%BA_ctime_1.html
        '''
        # self.url = 'https://www.sky2022.xyz/search/苍井空_ctime_1.html'
        self.url = 'https://www.sky2022.xyz'
        self.headers = {
            'content-type': 'text/html;charset=UTF-8',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
        }

        self.allNameList = []
        self.allMagnetList = []
        self.allFileSizeList = []
        self.allHotList = []
        self.isMore = 1

    # 得到未经筛选的内容
    def getContent(self, url):
        request = requests.get(url=url, headers=self.headers)
        request.encoding = 'utf-8'
        response = request.text
        # print(response)
        return response

    # 筛选数据（返回一个列表）
    def filtrateData(self, data, rule):
        select = lxml.html.document_fromstring(data)
        dataList = select.xpath(rule)
        return dataList

    # 得到所有资源的详细磁力链接（返回一个列表）
    def getMagnetList(self, url):
        data = self.getContent(url)
        rule = '//h5[@class="item-title"]/a/@href'
        UrlList = self.filtrateData(data=data, rule=rule)

        if len(UrlList) > 0:
            for i in UrlList:
                # 获取资源名
                url = self.url + i
                # print(url)
                data = self.getContent(url=url)
                rule = '//tr[2]/td/text()'
                everyName = self.filtrateData(data=data, rule=rule)[0]
                self.allNameList.append(everyName)

                rule = '//textarea[@class="well magnet center"]/text()'
                everyMagnet = self.filtrateData(data=data, rule=rule)[0]
                self.allMagnetList.append(everyMagnet)

                rule = '//div[@class="col-xs-4"]/span/text()'
                everyFileSize = self.filtrateData(data=data, rule=rule)[1]
                self.allFileSizeList.append(everyFileSize)

                rule = '//div[@class="col-xs-4"]/span/text()'
                everyHot = self.filtrateData(data=data, rule=rule)[2]
                self.allHotList.append(everyHot)
        else:
            self.isMore = 0

class App:
    def __init__(self):
        '''
            窗体需要的字段
        '''
        self.root = Tk()
        self.root.state
        self.width = self.root.winfo_screenwidth()  # 获取电脑窗体的宽度
        self.height = self.root.winfo_screenheight()  # 获取电脑窗体的高度
        self.url = ''
        self.searchData = ''
        self.page = ''

        self.crawler = Crawler()

        self.initForm()
        self.root.mainloop()

    # 初始化窗体
    def initForm(self):
        self.root.title("SearchTool —— Author: 逸轩")
        w = int((self.width - 590) / 2)
        h = int((self.height - 420) / 2)
        self.root.geometry('590x420+%s+%s' % (w, h))
        self.root.resizable(0, 0)

        # 第一行控件
        label1 = Label(self.root, text='请输入你感兴趣的内容：')
        label1.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.text1 = Entry(self.root, width=40)
        self.text1.grid(row=0, column=1, padx=5)
        self.text1.bind('<KeyPress-Return>', self.bindSearchToEnter)
        btnSearch = Button(self.root, width=10, height=1, text='搜索', command=self.clickSearch)
        btnSearch.grid(row=0, sticky=E, column=2)


        # 第二行控件
        fm = Frame(self.root, width=580, height=240)
        fm.grid(row=1, column=0, columnspan=3, sticky=W, padx=5)

        self.listbox = Listbox(fm, width=93, height=15)
        self.listbox.place(x=0, y=0)
        scroll = Scrollbar(fm, command=self.listbox.yview)
        scroll.place(x=561, y=0, width=20, height=240)

        # 第三行控件
        self.btnLoadMore = Button(self.root, width=10, height=1, text='加载更多', state='disabled', command=self.clickLoadMore)
        self.btnLoadMore.grid(row=2, column=0, sticky=W, padx=5, pady=5)

        self.btnConfirm = Button(self.root, width=10, height=1, text='确认选择', state='disabled', command=self.confirmBtn)
        self.btnConfirm.grid(row=2, column=2, sticky=E, padx=5, pady=5)

        # 第四行控件
        self.text2 = Text(self.root, width=82, height=8)
        self.text2.grid(row=3, column=0, columnspan=3, sticky=W, padx=5)

    # 点击搜索按钮
    def clickSearch(self):
        thread = threading.Thread(target=self.search)
        thread.setDaemon(True)  # 确保主线程结束时,杀死子线程
        thread.start()
    # 搜索
    def search(self):
        self.text2.delete(0.0, END)  # 清除磁力链接信息
        content = self.text1.get()  # 获取搜索内容的值
        self.searchData = content.strip()  # .strip()就是把这个字符串头和尾的空格去掉
        self.page = 1
        self.url = self.crawler.url + '/search/%s_ctime_%s.html' % (self.searchData, self.page)
        print(self.url)

        self.crawler.allNameList.clear()
        self.crawler.allMagnetList.clear()
        self.listbox.delete(0, END)
        self.listbox.insert(END, '请稍后，数据正在加载...')
        self.btnLoadMore.config(state='disabled')
        self.btnConfirm.config(state='disabled')

        thread = threading.Thread(target=self.crawler.getMagnetList(url=self.url))
        thread.setDaemon(True)  # 确保主线程结束时,杀死子线程
        thread.start()

        allNameList = self.crawler.allNameList
        # print(allNameList)
        self.listbox.delete(0, END)
        for i in range(0, len(allNameList)):
            self.listbox.insert(END, allNameList[i])
        self.listbox.selection_set(0)   # 默认选择第一个
        self.btnLoadMore.config(state='normal')
        self.btnConfirm.config(state='normal')

    # 点击加载更多按钮
    def clickLoadMore(self):
        self.thread = threading.Thread(target=self.loadMore)
        self.thread.setDaemon(True)  # 确保主线程结束时,杀死子线程
        self.thread.start()
    # 点击加载更多
    def loadMore(self):
        self.page += 1
        self.url = self.crawler.url + '/search/%s_ctime_%s.html' % (self.searchData, self.page)
        print(self.url)
        self.thread = threading.Thread(target=self.crawler.getMagnetList(url=self.url))
        self.thread.setDaemon(True)  # 确保主线程结束时,杀死子线程
        self.thread.start()

        if self.crawler.isMore == 1:
            allNameList = self.crawler.allNameList
            # print(allNameList)
            for i in range(self.listbox.size(), len(allNameList)):
                self.listbox.insert(END, allNameList[i])
            self.btnLoadMore.config(state='normal')
            self.btnConfirm.config(state='normal')
        else:
            self.btnLoadMore.config(state='disabled')
            messagebox.showinfo(title='Error', message='no more data!')

    # 点击确定按钮
    def confirmBtn(self):
        self.text2.delete(0.0, END)
        index = self.listbox.curselection()[0]
        # messagebox.showinfo(title='提示', message='你点击了第%s个' % str(index+1))
        data = '磁力链接：%s\n文件大小：%s\n热度：%s' \
        % (self.crawler.allMagnetList[index], self.crawler.allFileSizeList[index], self.crawler.allHotList[index])
        self.text2.insert(INSERT, data)

    # 把按钮绑定给回车
    def bindSearchToEnter(self, event):
        if event.keysym == 'Return':
            self.clickSearch()   # 搜索



if __name__ == '__main__':
    App()

