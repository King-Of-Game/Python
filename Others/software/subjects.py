# _*_ coding : utf-8 _*_
# __author__ : YiXuan
# __date__ : 2019/9/3 13:01
# __Software__ : PyCharm

from datetime import datetime
from time import strftime
from time import strptime
from tkinter import Label
from tkinter import Tk
from tkinter import Frame
from tkinter import Listbox
from tkinter import Scrollbar
from tkinter import Button
from tkinter import W, S, E, N
# from tkinter import messagebox

class App:
    # 初始化类的一些属性和方法
    def __init__(self):
        self.root = Tk()
        self.width = self.root.winfo_screenwidth()  # 获取电脑窗体的宽度
        self.height = self.root.winfo_screenheight()  # 获取电脑窗体的高度

        '''设置开学日期'''
        self.basicDate = '2019-9-2'
        self.basicDate = strptime(self.basicDate, "%Y-%m-%d")

        '''获取当前日期'''
        self.today = strftime('%Y-%m-%d')
        # print(type(self.today))
        # self.today = '2019-9-16'
        self.today = strptime(self.today, "%Y-%m-%d")
        # print(type(self.today))
        '''获取当前日期'''

        '''计算当前是第几周'''
        self.basicDate = datetime(self.basicDate[0], self.basicDate[1], self.basicDate[2])
        self.today = datetime(self.today[0], self.today[1], self.today[2])
        self.result = (self.today - self.basicDate).days + 1  # 今天是开学的第self.result天
        # print(self.result)
        self.week = 0
        if self.result % 7 == 0:
            self.week = self.result // 7
        else:
            self.week = self.result // 7 + 1
        '''计算当前是第几周'''

        self.initForm()

    # 初始化应用窗体
    def initForm(self):
        self.root.title("课表（当前是第"+str(self.week)+"周）—— 作者：逸轩")
        w = int((self.width - 880) / 2)
        h = int((self.height - 500) / 2)
        self.root.geometry('880x500+%s+%s' % (w, h))


        self.initClasses(self.week)

        self.initListbox()


        self.root.mainloop()

    # 初始化课表
    def initClasses(self, week):


        self.fm = Frame(self.root, height=200, width=400)
        self.fm.place(x=0, y=0)

        # 上课时间
        labelTime = Label(self.fm, text=' ', fg='black')
        labelTime.grid(row=0, column=0, sticky=E, padx=5, pady=5)

        labelTime = Label(self.fm, text='1（8：00）', fg='black', background='#7FFF00', width=12)
        labelTime.grid(row=1, column=0, sticky=E, padx=5, pady=5)

        labelTime = Label(self.fm, text='2（8：55）', fg='black', background='#FFD700', width=12)
        labelTime.grid(row=2, column=0, sticky=E, padx=5, pady=5)

        labelTime = Label(self.fm, text='3（10：00）', fg='black', background='#FF69B4', width=12)
        labelTime.grid(row=3, column=0, sticky=E, padx=5, pady=5)

        labelTime = Label(self.fm, text='4（10：55）', fg='black', background='#BA2BE2', width=12)
        labelTime.grid(row=4, column=0, sticky=E, padx=5, pady=5)

        labelTime = Label(self.fm, text='5（14：00）', fg='black', background='#FFA07A', width=12)
        labelTime.grid(row=5, column=0, sticky=E, padx=5, pady=5)

        labelTime = Label(self.fm, text='6（14：55）', fg='black', background='#87CEFA', width=12)
        labelTime.grid(row=6, column=0, sticky=E, padx=5, pady=5)

        labelTime = Label(self.fm, text='7（16：00）', fg='black', background='#00FFFF', width=12)
        labelTime.grid(row=7, column=0, sticky=E, padx=5, pady=5)

        labelTime = Label(self.fm, text='8（16：55）', fg='black', background='#98FB98', width=12)
        labelTime.grid(row=8, column=0, sticky=E, padx=5, pady=5)

        labelTime = Label(self.fm, text='9（19：00）', fg='black', background='#FFFF00', width=12)
        labelTime.grid(row=9, column=0, sticky=E, padx=5, pady=5)

        labelTime = Label(self.fm, text='10（19：55）', fg='black', background='#D2691E', width=12)
        labelTime.grid(row=10, column=0, sticky=E, padx=5, pady=5)

        labelTime = Label(self.fm, text='11（20：50）', fg='black', background='#FF6347', width=12)
        labelTime.grid(row=11, column=0, sticky=E, padx=5, pady=5)

        label1 = Label(self.fm, text='星期一', fg='black', background='#FF8C00', width=20)
        label1.grid(row=0, column=1, sticky=W + S + N + E, padx=5, pady=5)

        label2 = Label(self.fm, text='星期二', fg='black', background='#FF8C00', width=20)
        label2.grid(row=0, column=2, sticky=W + S + N + E, padx=5, pady=5)

        label3 = Label(self.fm, text='星期三', fg='black', background='#FF8C00', width=20)
        label3.grid(row=0, column=3, sticky=W + S + N + E, padx=5, pady=5)

        label4 = Label(self.fm, text='星期四', fg='black', background='#FF8C00', width=20)
        label4.grid(row=0, column=4, sticky=W + S + N + E, padx=5, pady=5)

        label5 = Label(self.fm, text='星期五', fg='black', background='#FF8C00', width=20)
        label5.grid(row=0, column=5, sticky=W + S + N + E, padx=5, pady=5)
        # self.fm.place_forget()


        # 整理星期一*************************************************

        if week >= 16 and week <= 17:
            label1 = Label(self.fm, text='VC++（计科楼101）', fg='black', background='#7FFF00')
            label1.grid(row=1, column=1, sticky=W + S + N + E, padx=5, pady=5)

            label1 = Label(self.fm, text='VC++（计科楼101）', fg='black', background='#FFD700', width=20)
            label1.grid(row=2, column=1, sticky=W + S + N + E, padx=5, pady=5)

        if (week >= 4 and week <= 6) or (week >= 8 and week <= 16):
            label1 = Label(self.fm, text='JavaScript（教1楼307）', fg='black', background='#FF69B4', width=20)
            label1.grid(row=3, column=1, sticky=W + S + N + E, padx=5, pady=5)

            label1 = Label(self.fm, text='JavaScript（教1楼307）', fg='black', background='#BA2BE2', width=20)
            label1.grid(row=4, column=1, sticky=W + S + N + E, padx=5, pady=5)

        if week >= 1 and week <= 16:
            label1 = Label(self.fm, text='大学英语（经法楼107）', fg='black', background='#FFA07A', width=20)
            label1.grid(row=5, column=1, sticky=W + S + N + E, padx=5, pady=5)

            label1 = Label(self.fm, text='大学英语（经法楼107）', fg='black', background='#87CEFA', width=20)
            label1.grid(row=6, column=1, sticky=W + S + N + E, padx=5, pady=5)

        if (week >= 1 and week <= 6) or (week >= 8 and week <= 17):
            label1 = Label(self.fm, text='VC++（教1楼306）', fg='black', background='#00FFFF', width=20)
            label1.grid(row=7, column=1, sticky=W + S + N + E, padx=5, pady=5)

            label1 = Label(self.fm, text='VC++（教1楼306）', fg='black', background='#98FB98', width=20)
            label1.grid(row=8, column=1, sticky=W + S + N + E, padx=5, pady=5)

        if (week >= 1 and week <= 6) or (week >= 8 and week <= 17):
            label1 = Label(self.fm, text='VC++（计科楼203）', fg='black', background='#FFFF00', width=20)
            label1.grid(row=9, column=1, sticky=W + S + N + E, padx=5, pady=5)

            label1 = Label(self.fm, text='VC++（计科楼203）', fg='black', background='#D2691E', width=20)
            label1.grid(row=10, column=1, sticky=W + S + N + E, padx=5, pady=5)

        # 整理星期一*************************************************

        # 整理星期二*************************************************

        if (week >= 1 and week <= 6) or (week >= 8 and week <= 17):
            label2 = Label(self.fm, text='JSP（教1楼506）', fg='black', background='#7FFF00', width=20)
            label2.grid(row=1, column=2, sticky=W + S + N + E, padx=5, pady=5)

            label2 = Label(self.fm, text='JSP（教1楼506）', fg='black', background='#FFD700', width=20)
            label2.grid(row=2, column=2, sticky=W + S + N + E, padx=5, pady=5)

        if (week >= 5 and week <= 6) or (week >= 8 and week <= 17):
            label2 = Label(self.fm, text='JSP（计科楼203）', fg='black', background='#FF69B4', width=20)
            label2.grid(row=3, column=2, sticky=W + S + N + E, padx=5, pady=5)

            label2 = Label(self.fm, text='JSP（计科楼203）', fg='black', background='#BA2BE2', width=20)
            label2.grid(row=4, column=2, sticky=W + S + N + E, padx=5, pady=5)

        if (week >= 5 and week <= 6) or (week >= 8 and week <= 17):
            label2 = Label(self.fm, text='IOS（教1楼509）', fg='black', background='#FFA07A', width=20)
            label2.grid(row=5, column=2, sticky=W + S + N + E, padx=5, pady=5)

            label2 = Label(self.fm, text='IOS（教1楼509）', fg='black', background='#87CEFA', width=20)
            label2.grid(row=6, column=2, sticky=W + S + N + E, padx=5, pady=5)

        if week == 17:
            label2 = Label(self.fm, text='Java（计科楼203）', fg='black', background='#7FFF00', width=20)
            label2.grid(row=9, column=2, sticky=W + S + N + E, padx=5, pady=5)

            label2 = Label(self.fm, text='Java（计科楼203）', fg='black', background='#7FFF00', width=20)
            label2.grid(row=10, column=2, sticky=W + S + N + E, padx=5, pady=5)

        if (week <= 16) and (week % 2 == 0):
            label2 = Label(self.fm, text='计算机网络（计科楼104）', fg='black', background='#FFFF00', width=20)
            label2.grid(row=9, column=2, sticky=W + S + N + E, padx=5, pady=5)

            label2 = Label(self.fm, text='计算机网络（计科楼104）', fg='black', background='#D2691E', width=20)
            label2.grid(row=10, column=2, sticky=W + S + N + E, padx=5, pady=5)

        if (week <= 16) and (week % 2 == 0):
            label2 = Label(self.fm, text='计算机网络（计科楼104）', fg='black', background='#FF6347', width=20)
            label2.grid(row=11, column=2, sticky=W + S + N + E, padx=5, pady=5)

        # 整理星期二*************************************************

        # 整理星期三*************************************************

        if (week >= 9 and week <= 17) and (week % 2 != 0):
            label3 = Label(self.fm, text='计算机网络（教1楼308）', fg='black', background='#FF69B4', width=20)
            label3.grid(row=3, column=3, sticky=W + S + N + E, padx=5, pady=5)

            label3 = Label(self.fm, text='计算机网络（教1楼308）', fg='black', background='#BA2BE2', width=20)
            label3.grid(row=4, column=3, sticky=W + S + N + E, padx=5, pady=5)

        if (week >= 1 and week <= 6) or (week == 8):
            label3 = Label(self.fm, text='计算机网络（教1楼308）', fg='black', background='#FF69B4', width=20)
            label3.grid(row=3, column=3, sticky=W + S + N + E, padx=5, pady=5)

            label3 = Label(self.fm, text='计算机网络（教1楼308）', fg='black', background='#BA2BE2', width=20)
            label3.grid(row=4, column=3, sticky=W + S + N + E, padx=5, pady=5)

        if (week >= 10 and week <= 16) and (week % 2 == 0):
            label3 = Label(self.fm, text='IOS（计科楼203）', fg='black', background='#FF69B4', width=20)
            label3.grid(row=3, column=3, sticky=W + S + N + E, padx=5, pady=5)

            label3 = Label(self.fm, text='IOS（计科楼203）', fg='black', background='#BA2BE2', width=20)
            label3.grid(row=4, column=3, sticky=W + S + N + E, padx=5, pady=5)

        if (week >= 1 and week <= 6) or (week >= 8 and week <= 17):
            label3 = Label(self.fm, text='Java（教1楼509）', fg='black', background='#FFA07A', width=20)
            label3.grid(row=5, column=3, sticky=W + S + N + E, padx=5, pady=5)

            label3 = Label(self.fm, text='Java（教1楼509）', fg='black', background='#87CEFA', width=20)
            label3.grid(row=6, column=3, sticky=W + S + N + E, padx=5, pady=5)

        if (week >= 1 and week <= 6) or (week >= 8 and week <= 17):
            label3 = Label(self.fm, text='Java（计科楼203）', fg='black', background='#00FFFF', width=20)
            label3.grid(row=7, column=3, sticky=W + S + N + E, padx=5, pady=5)

            label3 = Label(self.fm, text='Java（计科楼203）', fg='black', background='#98FB98', width=20)
            label3.grid(row=8, column=3, sticky=W + S + N + E, padx=5, pady=5)

        # 整理星期三*************************************************

        # 整理星期四*************************************************

        if (week >= 1 and week <= 6) or (week >= 8 and week <= 17):
            label4 = Label(self.fm, text='数据库（教1楼406）', fg='black', background='#7FFF00', width=20)
            label4.grid(row=1, column=4, sticky=W + S + N + E, padx=5, pady=5)

            label4 = Label(self.fm, text='数据库（教1楼406）', fg='black', background='#FFD700', width=20)
            label4.grid(row=2, column=4, sticky=W + S + N + E, padx=5, pady=5)

        if (week >= 4 and week <= 6) or (week >= 8 and week <= 16):
            label4 = Label(self.fm, text='JavaScript（计科楼104）', fg='black', background='#FF69B4', width=20)
            label4.grid(row=3, column=4, sticky=W + S + N + E, padx=5, pady=5)

            label4 = Label(self.fm, text='JavaScript（计科楼104）', fg='black', background='#BA2BE2', width=20)
            label4.grid(row=4, column=4, sticky=W + S + N + E, padx=5, pady=5)

        if week == 6 or week == 8:
            label4 = Label(self.fm, text='IOS（计科楼203）', fg='black', background='#FFA07A', width=20)
            label4.grid(row=5, column=4, sticky=W + S + N + E, padx=5, pady=5)

            label4 = Label(self.fm, text='IOS（计科楼203）', fg='black', background='#87CEFA', width=20)
            label4.grid(row=6, column=4, sticky=W + S + N + E, padx=5, pady=5)

        if week >= 6 and week <= 11:
            label4 = Label(self.fm, text='心理健康（教1楼211）', fg='black', background='#FFFF00', width=20)
            label4.grid(row=9, column=4, sticky=W + S + N + E, padx=5, pady=5)

            label4 = Label(self.fm, text='心理健康（教1楼211）', fg='black', background='#D2691E', width=20)
            label4.grid(row=10, column=4, sticky=W + S + N + E, padx=5, pady=5)

        if week >= 6 and week <= 11:
            label4 = Label(self.fm, text='心理健康（教1楼211）', fg='black', background='#FF6347', width=20)
            label4.grid(row=11, column=4, sticky=W + S + N + E, padx=5, pady=5)

        # 整理星期四*************************************************

        # 整理星期五*************************************************

        if (week <= 17 and week % 2 != 0) and (week != 7):
            label5 = Label(self.fm, text='数据库（教1楼408）', fg='black', background='#7FFF00', width=20)
            label5.grid(row=1, column=5, sticky=W + S + N + E, padx=5, pady=5)

            label5 = Label(self.fm, text='数据库（教1楼408）', fg='black', background='#FFD700', width=20)
            label5.grid(row=2, column=5, sticky=W + S + N + E, padx=5, pady=5)

        if (week >= 5 and week <= 16) and (week % 2 == 0):
            label5 = Label(self.fm, text='数据库（计科楼203）', fg='black', background='#7FFF00', width=20)
            label5.grid(row=1, column=5, sticky=W + S + N + E, padx=5, pady=5)

            label5 = Label(self.fm, text='数据库（计科楼203）', fg='black', background='#FFD700', width=20)
            label5.grid(row=2, column=5, sticky=W + S + N + E, padx=5, pady=5)

        if (week <= 17 and week % 2 != 0) and (week != 7):
            label5 = Label(self.fm, text='Python（教1楼507）', fg='black', background='#FF69B4', width=20)
            label5.grid(row=3, column=5, sticky=W + S + N + E, padx=5, pady=5)

            label5 = Label(self.fm, text='Python（教1楼507）', fg='black', background='#BA2BE2', width=20)
            label5.grid(row=4, column=5, sticky=W + S + N + E, padx=5, pady=5)

        if (week >= 4 and week <= 6) or (week >= 8 and week <= 16):
            label5 = Label(self.fm, text='Python（计科楼303）', fg='black', background='#FFA07A', width=20)
            label5.grid(row=5, column=5, sticky=W + S + N + E, padx=5, pady=5)

            label5 = Label(self.fm, text='Python（计科楼303）', fg='black', background='#87CEFA', width=20)
            label5.grid(row=6, column=5, sticky=W + S + N + E, padx=5, pady=5)

        # 整理星期五*************************************************

    # 点击确定按钮
    def confirmBtn(self):
        value = self.listbox.get(self.listbox.curselection())
        # messagebox.showinfo('提示', '你刚才点击了' + str(value))confirmBtn
        self.fm.place_forget()
        if str(value) == '自动':
            self.initClasses(self.week)
            self.root.title("课表（当前是第" + str(self.week) + "周）—— 作者：逸轩")
        else:
            self.initClasses(value)
            self.root.title("课表（当前是第" + str(value) + "周）—— 作者：逸轩")



    # 初始化滑动列表
    def initListbox(self):
        label = Label(self.root, text='手动选择周数查看：')
        label.place(x=500, y=450)

        self.listbox = Listbox(self.root, width=5, height=4, background='yellow')
        self.listbox.place(x=630, y=420)
        self.listbox.insert(1, '自动')

        for i in range(1, 18):
            self.listbox.insert(17, i)
        self.listbox.selection_set(0)

        scroll = Scrollbar(self.root, relief='ridge', command=self.listbox.yview)
        scroll.place(x=670, y=420, height=65)
        self.listbox.configure(yscrollcommand=scroll.set)

        button = Button(self.root, text='确定', width=6, command=self.confirmBtn)
        button.place(x=720, y=450)




if __name__ == '__main__':

    App()



