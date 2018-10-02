# import easygui as g
# import sys
# import os
# 查看模块
# help("modules")

##for i in range(1,10):
##    f = open('何健是个大SB' + str(i) + '.txt','w')
##    f.write('老何健')
##    f.close()


##def digui(number):
##    if number == 1:
##        return 1
##    else:
##        return number * digui(number-1)
##
##def jiecheng(number):
##    result = 0
##    for i in range(1,number+1):
##        result += digui(i)    
##    return result
##
##number = int(input("请输入正整数：\n"))
##jiecheng(number)
##print(jiecheng(number))

# import sys
# import easygui as g
# while True:
#     g.msgbox("欢迎来到武船！")
#     msg = "选择一个吧"
#     title = "请选择一个继续"
#     choices = ['老何健','大保健','大宝剑']
#     choice = g.choicebox(msg,title,choices)
#     g.msgbox("你选择了"+str(choice))
#     msg = "你希望重新开始吗？"
#     title = "请选择："
#     if g.ccbox(msg,title):
#         pass
#     else:
#         sys.exit(0)






##print(sys.platform)
##print(2 ** 100)
##x = "SB"
##print(x * 8)











# import urllib.request
# def getHtml(url):
# 	page = urllib.request.urlopen(url)
# 	html=page.read()
# 	return html
#
# url="http://www.baidu.com"
# # html= getHtml(url)
# # print(html)



# import urllib.parse
# import urllib.request
# url = "https://mail.qq.com/"
# values = {'u': 'username', 'p': 'password'}
# headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)', 'Referer': 'http://www.zhihu.com/articles'}
# data = urllib.parse.urlencode(values).encode('utf-8')
# request = urllib.request.Request(url, data, headers)
# response = urllib.request.urlopen(request)
# print(response.read())


# import urllib.parse
# import urllib.request
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))
# print(type(response))
# print(response.status)
# print(response.getheaders())
# print(response.getheader("Server"))

# values = {'word': 'hello'}
# data = urllib.parse.urlencode(values).encode('utf-8')
# response = urllib.request.urlopen('http://httpbin.org/post', data, 1)
# print(response.read())







# urllib库的高级用法：

# import urllib.parse
# import urllib.request
# url = "http://httpbin.org/post"
# headers = {
#     #伪装一个火狐浏览器
#     'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
#     'Referer': 'http://www.zhihu.com/articles',
#     'host': 'httpbin.org'
# }
# dict1 = {
#     "name": "Jack"
# }
# data = urllib.parse.urlencode(dict1).encode('utf-8')
# request = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

#设置代理
# import urllib.request
# proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:8080/'})
# proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
# proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
# opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
# opener.open('http://www.example.com/login.html')


# 添加代理
# import urllib.request
# proxies = {'http': 'http://www.baidu.com:8080/'}
# opener = urllib.request.FancyURLopener(proxies)
# f = opener.open('http://www.baidu.com')
# print(f.read().decode('utf-8'))




# UrlError异常处理：

# import urllib.parse
# import urllib.request
# import socket
# import urllib.error
# try:
#     response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print("Time out!")

# request = urllib.request.Request('http://www.baidu.com')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

# import urllib.request
# import urllib.error
# url = 'http://www.xxxxxx.com'
# request = urllib.request.Request(url=url)
# try:
#     response = urllib.request.urlopen(request)
# except urllib.error.URLError as e:
#     print(e.reason())

# import urllib.request
# import urllib.error
# url = 'http://blog.csdn.net/cqcre'
# request = urllib.request.Request(url=url)
# try:
#     response = urllib.request.urlopen(request)
# except urllib.error.HTTPError as e:
#     print(e.code)
# except urllib.error.URLError as e:
#     print(e.reason)
# else:
#     print("OK!")

# import urllib.request
# import urllib.error
# url = 'http://blog.csdn.net/cqcre'
# request = urllib.request.Request(url=url)
# try:
#     response = urllib.request.urlopen(request)
# except urllib.error.URLError as e:
#     if hasattr(e, "code"):
#         print(e.code)
#     if hasattr(e, "reason"):
#         print(e.reason)
# else:
#     print("OK!")





# Cookie的使用:

# 1.获取Cookie保存到变量
# import urllib.request
# import urllib.parse
# import http.cookiejar
# url = 'http://c.highpin.cn/Users/CLogin'
# data = urllib.parse.urlencode({
#     "Logon_Password": "sunmin",
#     "Logon_PostCode": "fghc",
#     "Logon_RememberMe": "false",
#     "Logon_UserEmail": "sun121@qq.com"
# }).encode("utf-8")
# header = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#     "Accept-Encoding": "utf-8",
#     "Accept-Language": "zh-CN,zh;q=0.8",
#     "Cache-Control": "no-cache",
#     "Connection": "keep-alive",
#     "Host": "c.highpin.cn",
#     "Pragma": "no-cache",
#     "Referer": "http://c.highpin.cn/",
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"
# }
# request = urllib.request.Request(url=url, data=data, headers=header)
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open(request)
# print(response.read().decode("utf-8"))
# for item in cookie:
#     print('Name = '+item.name)
#     print('Value = ' + item.value)

# 2.保存Cookie到文件
# import urllib.request
# import http.cookiejar
# url = "http://www.baidu.com"
# # 设置保存cookie的文件，同级目录下的cookie.txt
# filename = "cookie.txt"
# # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
# cookie = http.cookiejar.MozillaCookieJar(filename)
# # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器
# handler = urllib.request.HTTPCookieProcessor(cookie)
# # 通过handler来构建opener
# opener = urllib.request.build_opener(handler)
# response = opener.open(url)
# # 保存cookie到文件
# cookie.save(ignore_discard=True, ignore_expires=True)
# # ignore_discard的意思是即使cookies将被丢弃也将它保存下来，ignore_expires的意思是如果在该文件中 cookies已经存在，则覆盖原文件写入.




# 3.从文件中获取Cookie并访问
# import urllib.request
# import http.cookiejar
# cookie = http.cookiejar.MozillaCookieJar()
# cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# url = "http://www.baidu.com"
# request = urllib.request.Request(url)
# response = opener.open(request)
# print(response.read().decode("utf-8"))


# 4.利用cookie模拟网站登录
# import urllib.request
# import http.cookiejar
# import urllib.parse
# filename = "cookie.txt"
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# # 登录教务系统的URL
# loginUrl = "http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login"
# data = urllib.parse.urlencode({
#     "username": "sa",
#     "password": "123456"
# }).encode("utf-8")
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"
# }
# request = urllib.request.Request(url=loginUrl, data=data, headers=header)
# # 模拟登录，并把cookie保存到变量
# response = opener.open(request)
# # 保存cookie到cookie.txt中
# cookie.save(ignore_discard=True, ignore_expires=True)
# # 利用cookie请求访问另一个网址，此网址是成绩查询网址
# gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
# # 请求访问成绩查询网址
# response = opener.open(gradeUrl)
# print(response.read().decode("utf-8"))





# 正则表达式：

# （1）re.match(pattern, string[, flags])这个方法将会从string（我们要匹配的字符串）的开头开始，尝试匹配pattern，一直向后匹配，如果遇到无法匹配的字符，立即返回 None，如果匹配未结束已经到达string的末尾，也会返回None。
# import re
# # 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”
# pattern = re.compile(r'hello')
#
# # 使用re.match匹配文本，获得匹配结果，无法匹配时将返回None
# result1 = re.match('hello', 'hello')
# result2 = re.match('hello', 'helloo CQC!')
# result3 = re.match(pattern, 'helo CQC!')
# result4 = re.match(pattern, 'hello CQC!')
#
# # 如果1匹配成功
# if result1:
#     # 使用Match获得分组信息
#     print(result1.group())
# else:
#     print('1匹配失败！')
# if result2:
#     # 使用Match获得分组信息
#     print(result2.group())
# else:
#     print('1匹配失败！')
# if result3:
#     # 使用Match获得分组信息
#     print(result3.group())
# else:
#     print('1匹配失败！')
# if result4:
#     # 使用Match获得分组信息
#     print(result4.group())
# else:
#     print('1匹配失败！')

# （2）re.search(pattern, string[, flags])search方法与match方法极其类似,search()会扫描整个string查找匹配,match（）只有在0位置匹配成功的话才有返回。
# import re
# pattern = re.compile(r'world', re.I)
# match = re.search(pattern, 'hello World')
# if match:
#     print(match.group())
# else:
#     print("匹配失败！")

# （3）re.split(pattern, string[, maxsplit])按照能够匹配的子串将string分割后返回列表。maxsplit用于指定最大分割次数，不指定将全部分割。
# import re
# pattern = re.compile(r'\d')
# match = re.split(pattern, 'one1two2three3four')
# print(match)

# （4）re.findall(pattern, string[, flags])搜索string，以列表形式返回全部能匹配的子串。
# import re
# pattern = re.compile(r'\d+')
# match = re.findall(pattern, 'one1two2three3four4')
# print(match)

# （5）re.finditer(pattern, string[, flags])搜索string，返回一个顺序访问每一个匹配结果（Match对象）的迭代器。
# import re
# pattern = re.compile(r'\d+')
# match = re.finditer(pattern, 'one1two2three3four4')
# for i in re.finditer(pattern, 'one1two2three3four4'):
#     print(i.group())
# print(match)

# （6）re.sub(pattern, repl, string[, count])使用repl替换string中每一个匹配的子串后返回替换后的字符串。不能使用编号0。count用于指定最多替换次数，不指定时全部替换。
# import re
# pattern = re.compile(r'(\w+) (\w+)')
# def func(m):
#     return m.group(1).title() + ' ' + m.group(2).title()
# match = re.sub(pattern, r'\2 \1', 'i say, hello world!')
# match1 = re.sub(pattern, func, 'i say, hello world!')
# print(match)
# print(match1)

# （7）re.subn(pattern, repl, string[, count])返回 (sub(repl, string[, count]), 替换次数)。
# import re
# pattern = re.compile(r'(\w+) (\w+)')
# match = re.subn(pattern, r'\2 \1', 'i say,hello world!')
# def func(i):
#     return i.group(1).title()+" "+i.group(2).title()
# match1 = re.subn(pattern,func,'i say,hello world!')
# print(match)
# print(match1)



# 创建 Beautiful Soup 对象(Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种:Tag、NavigableString、BeautifulSoup、Comment)

# from bs4 import BeautifulSoup
# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie<!-- Elsie --></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# <div data-foo="value">test1</div>
# """
# soup = BeautifulSoup(html)
# 将本地 index.html 文件打开，用它来创建 soup 对象
# soup = BeautifulSoup(open('index.html'))
# 打印一下 soup 对象的内容，格式化输出
# print(soup.prettify())

# 5. 四大对象种类(Tag、NavigableString、BeautifulSoup、Comment)

# （1）Tag (通俗点讲就是 HTML 中的一个个标签：(它查找的是在所有内容中的第一个符合要求的标签))
# print(soup.title)
# print(type(soup.title))
# 对于 Tag，它有两个重要的属性，是 name 和 attrs
# name:
# print(soup.name)
# print(soup.head.name)
# attrs:
# 在这里，我们把 p 标签的所有属性打印输出了出来，得到的类型是一个字典。
# print(soup.p.attrs)
# 如果我们想要单独获取某个属性，可以这样，例如我们获取它的 class 叫什么
# print(soup.p['class'])
# 还可以这样，利用get方法，传入属性的名称
# print(soup.p.get('class'))
# 我们可以对这些属性和内容等等进行修改
# soup.p['class'] = "newClass"
# print(soup.p['class'])
# 还可以对这个属性进行删除
# del soup.p['class']
# print(soup.p)


# （2）NavigableString
# 获取标签内部的文字:
# print(soup.p.string)
# 检查一下它的类型
# print(type(soup.p.string))


# （3）BeautifulSoup（BeautifulSoup 对象表示的是一个文档的全部内容.大部分时候,可以把它当作 Tag 对象，是一个特殊的 Tag）
# print(type(soup.name))
# print(soup.name)
# print(soup.attrs)


# （4）Comment（Comment 对象是一个特殊类型的 NavigableString 对象，其实输出的内容仍然不包括注释符号，但是如果不好好处理它，可能会对我们的文本处理造成意想不到的麻烦。）
# print(soup.a)
# print(soup.a.string)
# print(type(soup.a.string))
# if type(soup.a.string) == 'bs4.element.Comment':
#     print(soup.a.string)


# 6. 遍历文档树

# （1）直接子节点
# .contents（tag 的 .content 属性可以将tag的子节点以列表的方式输出）
# print(soup.head.contents)
# 输出方式为列表，我们可以用列表索引来获取它的某一个元素
# print(soup.head.contents[0])

# .children（它返回的不是一个 list，不过我们可以通过遍历获取所有子节点）
# 打印输出 .children 看一下，可以发现它是一个 list 生成器对象
# print(soup.head.children)
# 我们怎样获得里面的内容呢？很简单，遍历一下就好了
# for child in soup.body.children:
#     print(child)

# （2）所有子孙节点
# .descendants（.contents 和 .children 属性仅包含tag的直接子节点，.descendants 属性可以对所有tag的子孙节点进行递归循环，和 children类似，我们也需要遍历获取其中的内容。）
# for child in soup.descendants:
#     print(child)

# （3）节点内容
# .string 属性（通俗点说就是：如果一个标签里面没有标签了，那么 .string 就会返回标签里面的内容。如果标签里面只有唯一的一个标签了，那么 .string 也会返回最里面的内容。）
# print(soup.head.string)
# print(soup.title.string)
# 如果tag包含了多个子节点,tag就无法确定，string 方法应该调用哪个子节点的内容, .string 的输出结果是 None
# print(soup.html.string)


# （4）多个内容
# .strings（获取多个内容，不过需要遍历获取）
# for string in soup.strings:
#     print(repr(string))

# .stripped_strings（输出的字符串中可能包含了很多空格或空行,使用 .stripped_strings 可以去除多余空白内容）
# for string in soup.stripped_strings:
#     print(repr(string))


# （5）父节点
# .parent
# p = soup.p
# print(p.parent.name)

# content = soup.head.title.string
# print(content.parent.name)


# （6）全部父节点
# .patents（通过元素的 .parents 属性可以递归得到元素的所有父辈节点）
# content = soup.head.title.string
# for patent in content.parents:
#     print(patent.name)


# （7）兄弟节点
# .next_sibling .previous_sibling（.next_sibling 属性获取了该节点的下一个兄弟节点，.previous_sibling 则与之相反，如果节点不存在，则返回 None）
# print(soup.p.next_sibling.name)
# print(soup.p.previous_sibling.name)
# print(soup.p.next_sibling.next_sibling.name)


# （8）全部兄弟节点
# .next_siblings .previous_siblings（通过 .next_siblings 和 .previous_siblings 属性可以对当前节点的兄弟节点迭代输出）
# for sibling in soup.a.next_siblings:
#     print(sibling.name)
# for sibling in soup.a.previous_siblings:
#     print(sibling.name)


# （9）前后节点
# .next_element .previous_element（与 .next_sibling .previous_sibling 不同，它并不是针对于兄弟节点，而是在所有节点，不分层次）
# 比如 head 节点为<head><title>The Dormouse's story</title></head>那么它的下一个节点便是 title，它是不分层次关系的
# print(soup.head.next_element.name)


# （10）所有前后节点
# .next_elements .previous_elements（通过 .next_elements 和 .previous_elements 的迭代器就可以向前或向后访问文档的解析内容,就好像文档正在被解析一样）
# for element in soup.head.next_elements:
#     print(repr(element))



# 7.搜索文档树
# （1）find_all( name , attrs , recursive , text , **kwargs )find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件
# name 参数可以查找所有名字为 name 的tag,字符串对象会被自动忽略掉

# A.传字符串（最简单的过滤器是字符串.在搜索方法中传入一个字符串参数,Beautiful Soup会查找与字符串完整匹配的内容,下面的例子用于查找文档中所有的<b>标签）
# print(soup.find_all('a'))

# B.传正则表达式（如果传入正则表达式作为参数,Beautiful Soup会通过正则表达式的 match() 来匹配内容.下面例子中找出所有以b开头的标签,这表示<body>和<b>标签都应该被找到）
# import re
# for tag in soup.find_all(re.compile('^b')):
#     print(tag.name)

# C.传列表（如果传入列表参数,Beautiful Soup会将与列表中任一元素匹配的内容返回.下面代码找到文档中所有<a>标签和<b>标签）
# print(soup.find_all(["a","b"]))

# D.传 True（True 可以匹配任何值,下面代码查找到所有的tag,但是不会返回字符串节点）
# for tag in soup.find_all(True):
#     print(tag.name)


# E.传方法（如果没有合适过滤器,那么还可以定义一个方法,方法只接受一个元素参数  ,如果这个方法返回 True 表示当前元素匹配并且被找到,如果不是则反回 False
# 下面方法校验了当前元素,如果包含 class 属性却不包含 id 属性,那么将返回 True:）
# def has_class_but_no_id(tag):
#     return tag.has_attr('class') and not tag.has_attr('id')
# print(soup.find_all(has_class_but_no_id))

# 2）keyword 参数（注意：如果一个指定名字的参数不是搜索内置的参数名,搜索时会把该参数当作指定名字tag的属性来搜索,如果包含一个名字为 id 的参数,Beautiful Soup会搜索每个tag的”id”属性）
# print(soup.find_all(id='link2'))

# 如果传入 href 参数,Beautiful Soup会搜索每个tag的”href”属性
# import re
# print(soup.find_all(href=re.compile("elsie")))

# 使用多个指定名字的参数可以同时过滤tag的多个属性
# import re
# print(soup.find_all(href=re.compile('elsie'), id='link1'))

# 在这里我们想用 class 过滤，不过 class 是 python 的关键词，这怎么办？加个下划线就可以
# print(soup.find_all("a", class_='sister'))

# 有些tag属性在搜索不能使用,比如HTML5中的 data-* 属性,但是可以通过 find_all() 方法的 attrs 参数定义一个字典参数来搜索包含特殊属性的tag
# print(soup.find_all(attrs={"data-foo": "value"}))

# 3）text 参数（通过 text 参数可以搜搜文档中的字符串内容.与 name 参数的可选值一样, text 参数接受 字符串 , 正则表达式 , 列表, True）
# print(soup.find_all(text="Elsie"))
# print(soup.find_all(text=["Tillie", "Elsie", "Lacie"]))
# import re
# print(soup.find_all(text=re.compile("Dormouse")))

# 4）limit 参数（使用 limit 参数限制返回结果的数量.效果与SQL中的limit关键字类似,当搜索到的结果数量达到 limit 的限制时,就停止搜索返回结果.）
# 文档树中有3个tag符合搜索条件,但结果只返回了2个,因为我们限制了返回数量
# print(soup.find_all("a",limit=2))

# 5）recursive 参数（）调用tag的 find_all() 方法时,Beautiful Soup会检索当前tag的所有子孙节点,如果只想搜索tag的直接子节点,可以使用参数 recursive=False .
# print(soup.find_all("title"))
# print(soup.find_all("title", recursive=False))


# （2）find( name , attrs , recursive , text , **kwargs )
# 它与 find_all() 方法唯一的区别是 find_all() 方法的返回结果是值包含一个元素的列表,而 find() 方法直接返回结果
# print(soup.find("title"))

# （3）find_parents() find_parent()
# find_all() 和 find() 只搜索当前节点的所有子节点,孙子节点等. find_parents() 和 find_parent() 用来搜索当前节点的父辈节点,搜索方法与普通tag的搜索方法相同,搜索文档搜索文档包含的内容

# （4）find_next_siblings() find_next_sibling()
# 这2个方法通过 .next_siblings 属性对当前 tag 的所有后面解析的兄弟 tag 节点进行迭代, find_next_siblings() 方法返回所有符合条件的后面的兄弟节点,find_next_sibling() 只返回符合条件的后面的第一个tag节点

# （5）find_previous_siblings() find_previous_sibling()
# 这2个方法通过 .previous_siblings 属性对当前 tag 的前面解析的兄弟 tag 节点进行迭代, find_previous_siblings() 方法返回所有符合条件的前面的兄弟节点, find_previous_sibling() 方法返回第一个符合条件的前面的兄弟节点

# （6）find_all_next() find_next()
# 这2个方法通过 .next_elements 属性对当前 tag 的之后的 tag 和字符串进行迭代, find_all_next() 方法返回所有符合条件的节点, find_next() 方法返回第一个符合条件的节点

# （7）find_all_previous() 和 find_previous()
# 这2个方法通过 .previous_elements 属性对当前节点前面的 tag 和字符串进行迭代, find_all_previous() 方法返回所有符合条件的节点, find_previous()方法返回第一个符合条件的节点


# 8.CSS选择器（我们在写 CSS 时，标签名不加任何修饰，类名前加点，id名前加 #，在这里我们也可以利用类似的方法来筛选元素，用到的方法是 soup.select()，返回类型是 list）
# （1）通过标签名查找
# print(soup.select("a"))
# （2）通过类名查找
# print(soup.select(".sister"))
# （3）通过 id 名查找
# print(soup.select("#link1"))
# （4）组合查找（组合查找即和写 class 文件时，标签名与类名、id名进行的组合原理是一样的，例如查找 p 标签中，id 等于 link1的内容，二者需要用空格分开）
# print(soup.select('p #link1'))
# print(soup.select('head > title'))
# （5）属性查找（查找时还可以加入属性元素，属性需要用中括号括起来，注意属性和标签属于同一节点，所以中间不能加空格，否则会无法匹配到。）
# print(soup.select('p a[href="http://example.com/elsie"]'))



# import urllib.request
# import re
# url = "https://findicons.com/pack/2787/beautiful_flat_icons"
# def download_url(url):
#     header = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"
#     }
#     request = urllib.request.Request(headers=header, url=url)
#     response = urllib.request.urlopen(request)
#     data = response.read()
#     return data
#
# html = download_url(url)
# pattern = re.compile('src="(.+?\.png)"')
# # Python3的urlopen返回的不是string是bytes。html用decode(‘utf-8’)进行解码，由bytes变成string。
# imglist = re.findall(pattern, html.decode("utf-8"))
# num = 1
# for imgurl in imglist:
#     # 重新解析每个图片的链接，返回bytes类型
#     byte = download_url(imgurl)
#     # f = open('%s.png' % num, 'wb')
#     f = open('C:/Users/pc/Desktop/import/%s.png' % num, 'wb')
#     f.write(byte)
#     print("正在下载第%s张图片" % num)
#     num += 1
#     if num > 3:
#         break


# 十进制转任意进制
# def f(n,x):
#     #n为待转换的十进制数，x为进制，取值为2-16
#     a = [0,1,2,3,4,5,6,7,8,9,'A','b','C','D','E','F']
#     b = []
#     while True:
#         s = n//x#商
#         y = n%x#余数
#         b = b+[y]
#         if s == 0:
#             break
#         n = s
#     b.reverse()
#     for i in b:
#         print(a[i], end='')
# f(26,16)

















# 自定义函数：
# import urllib.request
# url = {'百度':'http://www.baidu.com', '小游戏':'http://www.4399.com'}
# def pachong(url):
#     request = urllib.request.Request(url=url)
#     response = urllib.request.urlopen(request)
#     html = response.read().decode('utf-8')
#     return html
# temp = input('请输入要打开的网站：\n')
# print(pachong(url[temp]))
import requests

def temp():
    url = "http://dl.stream.qqmusic.qq.com/M800000rthMY4SRqM0.mp3?vkey=B9A8393A2E01D2902DD20EA6B128DD417EA8F35CD1721381E82E59900743E3EAE519BFAC2942D73A57E333EA70A60AD3302F90B77325515F&guid=5150825362&fromtag=1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"
    }
    r = requests.get(url=url,headers=headers)

    with open('尽头.mp3','wb') as f:
        f.write(r.content)
if __name__ == '__main__':
    temp()


