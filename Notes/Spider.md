# 1. Spider Basic Knowledge

![](C:\Users\87143\Desktop\Notebooks\Python\images\spider_basic.png)

+ 对称密钥加密：客户端会先把给服务端的数据进行加密（加密方式由客户端指定，加密完毕之后客户端会将密文和解密方式（密钥）一块发送给服务端）
+ 非对称密钥加密：服务器端把公钥发送给客户端，客户端根据得到的公钥把数据加密后发送给服务端，服务端再根据自己的私钥解密数据（没有办法保证客户端所拿到的公钥一定是服务端所发送的）
+ 证书密钥加密：服务端把公钥发送给双方可信的证书认证机构（给公钥进行数字签名），认证机构把公钥封装成证书再发送给客户端，客户端用携带着数字签名的公钥加密好数据在发送给服务端，服务端再使用私钥把数据解密（避免了在非对称密钥中公钥被拦截替换的安全隐患

## 查看目标网站的爬虫权限

+ 网站域名/robots.txt

## 1.1 requests

+ requests 对象无法保持连接状态; requests.Session()可以

### 示例

+ ```python
  import request
  
  response = requests.post(url=login_url, headers=headers, data=data)
  response = requests.Session().post(url=login_url, headers=headers, data=data)
  ```

## 1.2 Proxy IP

+ 代理IP（可以用来绕过封锁IP这种反爬机制）
+ 什么是代理
  + 代理服务器
+ 代理的作用
  + 突破自身IP访问的限制
  + 隐藏自身真实IP
+ 提供免费代理的网站
  + 快代理
  + 西祠代理
  + [www.goubanjia.com](http://www.goubanjia.com/)
+ 代理IP 的类型
  + http：应用到http协议对应的url中
  + https：应用到https协议对应的url中
+ 代理IP的不同匿名度介绍
  + 透明：服务器知道该次请求使用了代理，也知道请求对应的真实ip
  + 匿名：服务器知道使用了代理，不知道真实ip
  + 高匿：服务器不知道使用了代理，更不知道真实ip

### 示例1：通过Telnet服务器测试代理

- ```python
  import telnetlib
  
  # 连接Telnet服务器
  try:
      # 参数说明
      tn = telnetlib.Telnet('115.227.159.73', port='4312', timeout=10)
  except Exception as e:
      print(f'失败，原因: {e}')
  else:
      print('成功')
  ```

### 示例2：requests 模块使用代理

+ ```python
  import requests
  
  '''代理IP地址（高匿）'''
  proxy = {
      'http': 'http://117.85.105.170:808',
      'https': 'https://117.85.105.170:808'
  }
  head = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
  'Connection': 'keep-alive'
  }
  # http://icanhazip.com会返回当前的IP地址
  url = 'http://icanhazip.com'
  
  p = requests.get(url = url, headers=head, proxies=proxy)
  print(p.text)
  ```

## 1.3 数据解析

### 数据解析原理概述

+ 解析的局部的文本内容都会在标签之间或者标签对应的属性中进行存储
+ 进行指定标签的定位
+ 标签或者标签对应的属性中存储的数据值进行提取（解析）

### 聚焦爬虫

+ 爬取页面中指定的页面内容
+ 编码流程
  + 指定URL
  + 发起请求
  + 获取响应
  + 数据数据解析
  + 持久化存储

### 数据解析方法分类

#### 正则

+ re.M：多行匹配
+ re.S：单行匹配

#### bs4

+ python独有的解析方式

+ 大致步骤

  + 实例化一个BeautifulSoup对象，并且将页面源码数据加载到该对象中
  + 通过调用BeautifulSoup对象中相关的属性或者方法进行标签定位和数据提取

+ 环境安装

  + pip install bs4
  + pip install lxml

+ 实例化BeautifulSoup对象

  + from bs4 import BeautifulSoup

  + 对象的实例化

    1. 将本地的 .html文件 中的数据加载到该对象

       - ```python
         fp = open('./test.html', 'r', encoding='utf8')
         soup = BeautifulSoup(fp, 'lxml')
         ```

    2. 将互联网上获取的页面源码加载到该对象

       - ```python
         page_text = response.text
         soup = BeautifulSoup(page_text, 'lxml')
         ```

  + 提供的用于数据解析的方法和属性

    + 属性

      + soup.tagName: 返回的是文档中第一次出现的对应标签

    + 方法

      + soup.find('tagName') = soup.tagName

      + 根据属性定位

        + ```python
          # soup.find('tagName', class_/id/attr='song')
          content = soup.find('div', class_='chapter_content').text
          ```

      + soup.find_all('tagName'): 返回符合要求的所有标签（返回列表对象）

  + 层级选择器

    + soup.select('某种选择器（id,class,标签...选择器）') 返回的是列表
    + soup.select('.tagName > ul > li > a'): '>' 表示的是一个层级（直系）
    + soup.select('div a'): 空格表示的是多个层级

  + 获取标签之间的文本数据

    + 获取第一个 a 标签中的文本数据: soup.a.text/string/get_text()
      + text/get_text(): 可以获取某一个标签中所有的文本内容（即使文本内容不是该标签直系内容）
      + string: 只可以获取该标签下面直系文本内容

  + 获取标签中的属性值

    + 获取 a 标签 href 属性的值: soup.a['href']

#### xpath 解析

+ 最常用、最便捷、高效的一种解析方式

+ 处理中文乱码

  + ```python
    # fisrt
    'string'.encode('iso-8859-1').decode('gbk')
    
    # second
    def deal_garbled_code(response):	# response = request.get(url, headers)
        print(response.status_code)  # 查看返回对象的状态码
        response.encoding = response.apparent_encoding
        return response.text
        
    ```

+ 解析原理

  1. 实例化一个etree的对象，并且要将被解析的页面源码数据加载到该对象中。
  2. 调用etree对象中的xpath方法结合着xpath表达式实现标签的定位和内容的捕获。

+ 环境的安装

  + pip install lxml

+ 如何实例化一个etree对象

  1. 导入etree对象 
     - from lxml import etree
  2. 将加载到etree对象中
     - tree = etree.parse(filePath)
  3. 可以将从互联网上获取的页面源码数据加载到该对象中
     - etree.HTML('page_text')
  4. xpath表达式
     - /: 表示的是从根节点开始定位。表示的是一个层级
     - ./：表示的是从当前标签开始定位
     - //: 表示的是多个层级；表示从任意的位置开始定位
     - |（或): tree.xpath('//div[@class="test"]/ul/li/a | //div[@class="test"]/ul/div[2]/li/a')
     - 属性定位: //div[@class='song']
     - 索引定位: //div[@class='song']/p[3]  #这里索引是从1开始的
     - 获取文本:
       - /text(): 获取的是标签中直系的文本内容
       - //text(): 获取中非直系的文本内容
     - 获取属性的值: //img/@src
     - **注意：xpath表达式中不可以出现tbody标签**

## 1.4 验证码识别

### 反爬机制

+ 验证码，识别验证码图片中的数据，用于模拟登录操作。

### 识别验证码的操作

+ 人工肉眼识别。（不推荐）
+ 第三方自动识别（推荐）
  + 云打码
    + 注册
      + 普通和开发者用户
    + 登录
      + 普通用户的登录：查询该用户是否有积分
      + 开发者用户登录：
        + 创建一个软件：我的软件 => 添加新软件 => 录入软件名称 => 提交（软件id和密钥）
        + 下载示例代码：开发文档 => 点此下载：云打码接口dll => pythonHTTP示例下载

## 1.5 根据上述知识点模拟登录

### 目的

+ 爬取基于用户的某些信息

### 需求1：对某网站进行模拟登录

+ 点击登录按钮之后会发起一个 post 请求
+ post请求中会携带登录之前录入的相关登录信息（用户名，密码，验证码...）
+ 验证码：每次请求都会变化（要保证 当前验证码 和 即将发生的post请求 相对应）

### 需求2：爬取当前用户的相关用户信息（比如：个人主页中显示的用户信息）

+ http/https协议特性：无状态（本身不携带状态信息）
+ 没有请求到对应页面数据的原因
  + 发起的第二次基于个人主页页面请求的时候，服务器端并不知道该次请求是基于登陆状态下的请求。
+ cookie：用来让服务器端记录客户端的相关状态
  + 手动处理：通过抓包工具获取cookie值，将该值封装到headers中。（不推荐）
  + 自动处理：
    + cookie值的来源是哪里？
      + 模拟的登录post请求后，由服务器端创建。
    + session会话对象的作用：
      1. 可以进行请求的发送。
      2. 如果请求过程中产生了cookie，则该cookie会被自动存储/携带在该session对象中
    + 创建一个session对象：session = requests.Session()
    + 使用session对象进行模拟登录post请求的发送（cookie会被存储到Session对象中）
    + Session对象对个人主页对应的get请求去进行发送（携带了cookie）

# 2. 异步爬虫的方式

## 2.1 多线程，多进程（不建议）

+ 好处：可以为相关阻塞的操作单独开启线程或进程，阻塞操作就可以异步执行。
+ 弊端：不能无限制的开启多线程或者多进程。

## 2.2 进程池（适当使用）

+ 作用：处理的是阻塞且耗时的操作。
+ 好处：可以降低系统对进程或者线程创建和销毁的一个频率，从而很好的降低系统开销。
+ 弊端：池中线程或进程的数量是有上限。

## 2.3 单线程 + 异步协程（推荐）

+ 注意：
  + 在异步协程中如果出现了同步模块相关的代码，那么就无法实现异步
  + 当在 asyncio 中遇到阻塞操作必须进行手动挂起（语句前加：await）
+ event_loop
  + 事件循环，相当于一个无限循环，我们可以把一些函数注册到这个事件循环上，当满足某些条件的时候，函数就会被循环执行。程序是按照设定的顺序从头执行到尾，运行的次数也是完全按照设定。当在编写异步程序时，必然其中有部分程序的运行耗时是比较久的，需要先让出当前程序的控制权，让其在背后运行，让另一部分的程序先运行起来。当背后运行的程序完成后，也需要及时通知主程序已经完成任务可以进行下一步操作，但这个过程所需的时间是不确定的，需要主程序不断的监听状态，一旦收到了任务完成的消息，就开始进行下一步。loop就是这个持续不断的监视器。
+ coroutine（协程）
  + 协程对象，我们可以将协程对象注册到事件循环中，它会被事件循环调用。我们可以使用 async 关键字来定义一个方法，这个方法在调用时不会立即被执行，而是返回一个协程对象。
+ task(任务): 它是对协程对象的进一步封装，包含了任务的各个状态。
+ future: 代表将来执行或还没有执行的任务，实际上和 task 没有本质区别。
+ async: 定义一个协程
+ await: 用来挂起阻塞方法的执行。

# 3. Selenium模块的基本使用

## 3.1 问题

+ selenium模块和爬虫之间具有怎样的关联？
  + 便捷的获取网站中动态加载的数据
  + 便捷的实现模拟登录
+ 什么是selenium模块？
  + 基于浏览器自动化的一个模块

## 3.2 selenium使用流程

+ 环境安装：pip install selenium
+ 下载对应浏览器的驱动程序
+ 实例化一个浏览器对象
+ 编写基于浏览器自动化的操作代码
  + 发起请求：driver.get(url)
  + 标签定位：find系列方法
  + 标签交互：
    - clear()  #清除输入框的内容
    - send_keys('内容')  # 在文本框内输入内容
    - click()  #点击按钮
    - submit()  #表单的提交
  + 执行 js code：execute_script('jsCode')
  + 前进：forward()
  + 后退：back()
  + 关闭浏览器：quit()
+ selenium处理iframe
  + 如果定位的标签存在于iframe中，则必须使用switch_to_frame('标签id')
  + 动作链：
    + 导入包 ：from selenium.webdriver imporet ActionChains
    + 实例化一个动作链对象：action = ActionChains(browser)
    + ActionChains提供的方法
      + click(on_element=None)  \#单击鼠标左键
      + click_and_hold(on_element=None)  \#点击鼠标左键，按住不放
      + context_click(on_element=None)  #点击鼠标右键
      + double_click(on_element=None)  #双击鼠标左键
      + drag_and_drop(source, target)  #拖拽某个元素然后松开
      + drag_and_drop_by_offset(source, xoffset, yoffset)  \#拖拽某个元素到指定坐标然后松开
      + move_by_offset(xoffset, yoffset)  \#鼠标移动到距离当前位置（x,y）
      + move_to_element(to_element)  #鼠标移动到某个元素
      + move_to_element_with_offset(to_element, xoffset, yoffset)  #将鼠标移动到距某个元素多少距离的位置
      + release(on_element=None)  \#释放动作链
      + perform()  #执行链中的所有动作

# 4. Scrapy 框架

## 4.1 什么是框架？

+ 框架就是一个集成了很多功能并且具有很强通用性的一个项目模板。

## 4.2 如何学习框架？

+ 专门学习目标框架封装的各种功能的详细用法。

## 4.3 什么是scrapy？

+ 爬虫中封装好的一个主流热门框架。
+ 功能
  + 高性能的持久化存储
  + 异步的数据下载
  + 高性能的数据解析
  + 分布式爬取

## 4.4 scrapy框架的基本使用

+ 1 环境的安装

  + mac or linux
    + pip install scrapy
  + windows
    + pip install wheel
    + 下载 twisted，下载地址为http://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
    + 安装 twisted：pip install Twisted‑17.1.0‑cp36‑cp36m‑win_amd64.whl
    + pip install pywin32
    + pip install scrapy (ps: 最新版本的scrapy直接安装 scrapy 模块会一并安装上述模块)
  + 安装完成后进行测试：在终端里录入scrapy指令，没有报错即表示安装成功！

+ 2 创建一个工程

  + scrapy startproject projectName

+ 3 在spiders子目录中创建一个爬虫文件（一定要先cd到projectName工程目录中）

  + scrapy genspider spiderName [www.xxx.com](http://www.xxx.com/)

+ 4 设置配置文件：settings.py

  + ```python
    LOG_LEVEL = 'ERROR'  # 显示指定类型的日志信息
    ROBOTSTXT_OBEY = False
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
    ```

+ 5 执行工程（一定要先cd到projectName工程目录中）

  + scrapy crawl spiderName (可选参数--nolog：不打印日志)

## 4.5 scrapy数据解析

+ ```python
  def parse(self, response):
      # 解析：作者的名称 + 段子内容
      div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
      all_data = []  # 存储所有解析到的数据
      for div in div_list:
          # xpath返回的是列表，但是列表元素一定是Selector类型的对象
          # extract()可以将Selector对象中data参数存储的字符串提取出来
          # author_name = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
          author = div.xpath('./div[1]/a[2]/h2/text() | ./div[1]/span[2]/h2/text()').extract_first()  # 如果列表中只有一个元素可以用该方法
          # 如果列表调用了extract之后，则表示将列表中每一个Selector对象data对应的字符串提取出来
          content = div.xpath('./a[1]/div/span//text()').extract()
          content = ''.join(content)
          print(f"作者名称: {author}, 内容: {content}")
  ```

## 4.6 scrapy持久化存储

+ 基于终端指令
  + 要求：只可以将parse方法的返回值存储到本地的文本文件中
  + 注意：持久化存储的文件类型只支持：'json', 'jsonlines', 'jl', 'csv', 'xml', 'marshal', 'pickle'
  + 指令：scrapy crawl spiderName -o ./qiubai.csv
  + 优点：简洁高效便捷
  + 缺点：局限性比较强（数据值可以存储到上述后缀的文本文件中）
+ 基于管道
  + 优点：通用性强。
  + 缺点：编码流程繁琐
  + 编码流程：
    + 数据解析
    + 在item类中定义相关的属性
    + 将解析的数据封装存储到item类型的对象
    + 将item类型的对象提交给管道进行持久化存储的操作
    + 在管道类的process_item中要将其接收到的item对象中存储的数据进行持久化存储
    + 在配置文件中开启管道

### 面试题：将爬取到的数据一份存储到本地一份存储到数据库，如何实现？

+ 管道文件中一个管道类对应的时将数据存储到一种平台
+ 爬虫文件提交的item只会给管道文件中第一个被执行的管道类
+ 管道文件process_item 方法中的renturn item 表示：将item传递给下一个即将被执行的管道类
+ 在pipelines.py中添加一个类，然后在setting.py中注册该类

## 4.7 基于Spider手动请求的全站数据爬取

+ 含义：将网站中某板块下的全部页码对应的页面数据进行爬取
+ 需求：爬取校花网中的照片的名称
+ 实现方式：
  + 将所有页码的 url 添加到start_urls 列表中（不推荐）
  + 自行手动进行请求发送（推荐）
    + 如果是手动请求发送
    + yield scrapy.Request(url, callback)：callback 用于回调数据解析的方法

### 示例：爬取校花网中的照片的名称

+ ```python
  class XiaohuaSpider(scrapy.Spider):
      name = 'xiaohua'
      # allowed_domains = ['www.xxx.com']
      start_urls = ['http://www.521609.com/meinvxiaohua/']
  
      # 生成一个通用的url模板（模板是不可变的）
      url = 'http://www.521609.com/meinvxiaohua/list12%d.html'
      page_num = 2
  
      def parse(self, response):
          name_list = response.xpath('//*[@id="content"]/div[2]/div[2]/ul/li/a[2]/text()').extract()
          print(name_list)
          # for name in name_list:
          #     print(name)
  
          if self.page_num <= 11:
              new_url = format(self.url % self.page_num)
              self.page_num += 1
              # 手动请求发送：callback回调函数是专门用于数据解析
              # return 或 yield使得parse()方法具有返回值，scrapy会根据返回值进行递归调用parse()方法
              yield scrapy.Request(url=new_url, callback=self.parse)
  ```

## 4.8  五大核心组件

+ 示例
  + ![](C:\Users\87143\Desktop\Notebooks\Python\images\five_core_components.png)
  + ![](C:\Users\87143\Desktop\Notebooks\Python\images\five_core_components_detail.png)

+ 引擎(Scrapy)
  + 用来处理整个系统的数据流处理, 触发事务(框架核心)
+ 调度器(Scheduler)
  + 用来接受引擎发过来的请求, 压入队列中, 并在引擎再次请求的时候返回. 可以想像成一个URL（抓取网页的网址或者说是链接）的优先队列, 由它来决定下一个要抓取的网址是什么, 同时去除重复的网址
+ 下载器(Downloader)
  + 用于下载网页内容, 并将网页内容返回给蜘蛛 (Scrapy下载器是建立在twisted这个高效的异步模型上的)
+ 爬虫(Spiders)
  + 爬虫是主要干活的, 用于从特定的网页中提取自己需要的信息, 即所谓的实体(Item)。用户也可以从中提取出链接,让Scrapy继续抓取下一个页面。
+ 项目管道(Pipeline)
  + 负责处理爬虫从网页中抽取的实体，主要的功能是持久化实体、验证实体的有效性、清除不需要的信息。当页面被爬虫解析后，将被发送到项目管道，并经过几个特定的次序处理数据。
+ 中间件（middleware）
  + 下载中间件
    + 位置：引擎和下载器之间
    + 作用：批量拦截到整个工程中所有的请求和响应
    + 拦截请求：
      + 配置UA伪装：process_request
      + 配置代理IP：process_exception: return request

### 示例：在下载中间件配置UA伪装和代理IP

+ ```python
  class MiddleproDownloaderMiddleware(object):
      
      user_agent_list = [
          "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
          "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
          "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
      ]
  
      # 可被选用的代理IP
      PROXY_http = [
          '123.54.45.55:9999',
          '47.107.160.99:8118',
      ]
      PROXY_https = [
          '120.83.49.90:9000',
          '95.189.112.214:35508',
      ]
  
  
      # @classmethod
      # def from_crawler(cls, crawler):
      #     # This method is used by Scrapy to create your spiders.
      #     s = cls()
      #     crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
      #     return s
  
      # 拦截请求
      def process_request(self, request, spider):
          # UA伪装
          request.headers['User-Agent'] = random.choice(self.user_agent_list)
  
          return None
  
      # 拦截所有的响应
      def process_response(self, request, response, spider):
          # Called with the response returned from the downloader.
  
          # Must either;
          # - return a Response object
          # - return a Request object
          # - or raise IgnoreRequest
          return response
  
      # 拦截发生异常的请求
      def process_exception(self, request, exception, spider):
          # 用代理IP处理异常请求
          if request.url.split(':')[0] == 'http':
              request.meta['proxy'] = 'http://' + random.choice(self.PROXY_http)
          else:
              request.meta['proxy'] = 'https://' + random.choice(self.PROXY_https)
  
          return request  # 将修正之后的请求对象重新请求发送
  
  
      # def spider_opened(self, spider):
      #     spider.logger.info('Spider opened: %s' % spider.name)
  ```
  + 拦截响应：
    + 篡改响应数据（响应对象）
    + 需求：爬取网易新闻中的新闻数据（标题和内容）
      1. 通过网易新闻的首页解析出五大板块对应的详情页的url
      2. 每一个板块对应的新闻标题都是动态加载出来的（动态加载）
      3. 通过解析出每一条新闻详情页的url获取详情页的页面源码，解析出新闻内容

### 示例：在下载中间件中配置响应对象

+ ```python
  class NeteasyproDownloaderMiddleware(object):
  
      # @classmethod
      # def from_crawler(cls, crawler):
      #     # This method is used by Scrapy to create your spiders.
      #     s = cls()
      #     crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
      #     return s
  
      def process_request(self, request, spider):
          # Called for each request that goes through the downloader
          # middleware.
  
          # Must either:
          # - return None: continue processing this request
          # - or return a Response object
          # - or return a Request object
          # - or raise IgnoreRequest: process_exception() methods of
          #   installed downloader middleware will be called
          return None
  
      # 通过该方法拦截五大板块对应的响应对象，进行篡改
      def process_response(self, request, response, spider):  # spider表示爬虫对象
  
          # 挑选出指定的响应对象进行篡改
          # 通过Url指定request
          # 通过request指定response
          if request.url in spider.module_urls:
              bro = spider.bro    # 获取爬虫类中定义的浏览器对象
              sleep(2)
              # 篡改符合条件的response
              # 实例化一个新的响应对象（符合需求：包含动态加载出的新闻数据），替代旧的响应对象
              # 如何获取动态加载出的新闻数据
              bro.get(request.url)
              page_text = bro.page_source  # 包含了动态加载的新闻数据
  
              new_response = HtmlResponse(url=request.url, body=page_text, encoding='utf-8', request=request)  # 五大板块对应的响应对象
              return new_response
          else:
              return response    # 其它请求对应的响应对象
  
      def process_exception(self, request, exception, spider):
          # Called when a download handler or a process_request()
          # (from other downloader middleware) raises an exception.
  
          # Must either:
          # - return None: continue processing this exception
          # - return a Response object: stops process_exception() chain
          # - return a Request object: stops process_exception() chain
          pass
  
      # def spider_opened(self, spider):
      #     spider.logger.info('Spider opened: %s' % spider.name)
  ```

## 4.9 请求传参

### 使用场景

+ 如果要爬取解析的数据不在同一页面中。（深度爬取）

### 示例：爬取boss直聘的岗位名称，岗位描述

+ ```python
  # -*- coding: utf-8 -*-
  import scrapy
  import time
  from bossPro.items import BossproItem
  
  
  class BossSpider(scrapy.Spider):
      name = 'boss'
      # allowed_domains = ['www.xxx.com']
      start_urls = ['https://www.zhipin.com/c101280100/?query=python&ka=sel-city-101280100']
  
      url = 'https://www.zhipin.com/c101280100/?query=python&page=%d&ka=page-%d'
      page_num = 1
  
      def get_header(self):
          referer = format(self.url % (self.page_num, self.page_num))
          header = {
              'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
              'accept-encoding': 'gzip, deflate, br',
              'accept-language': 'zh-CN,zh;q=0.9',
              'cookie': 'lastCity=100010000; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1605344272,1605414348,1605433881,1605440586; __fid=359feb99a2ef63e117a2126787aea581; ___gtid=-247494185; __c=1605414348; __l=l=%2Fwww.zhipin.com%2Fc101280100%2F%3Fquery%3Dpython%26ka%3Dsel-city-101280100&r=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DmkG6TaIYhZqKYru9oMLuXPdyRsIBURWndpRcpgHf5Xj0VS5D7mOpqOPD6t0BnXvP%26wd%3D%26eqid%3D8923a17000007108000000065fb11446&g=&friend_source=0&friend_source=0; __a=71300573.1605328514.1605328514.1605414348.67.2.34.67; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1605444311; __zp_stoken__=af16bYXhuUQxmO1cAZV1ZRDkvdQd6IFsBKCQ0MSV0XmlkDXMQKG16AHIabUE5Jil0FyB%2BDD10GG9rH3ZmBlwzDEZZFGgpF1Y0fjxkdC0sFFRVbA5BDlxvRFR0GmA7KllIEXF0H3gAFxtIPGAFdA%3D%3D',
              'referer': referer
          }
          return header
  
      def start_requests(self):
          url = format(self.url % (self.page_num, self.page_num))
          print('正在爬取：%s' % url)
  
          header = self.get_header()
          yield scrapy.Request(url=url, headers=header, callback=self.parse)
  
      def parse(self, response):
  
          li_list = response.xpath('//*[@id="main"]/div/div[2]/ul/li')
          for li in li_list:
              item = BossproItem()
              job_name = li.xpath('.//span[@class="job-name"]/a/text()').extract_first()
              job_area = li.xpath('.//span[@class="job-area"]/text()').extract_first()
              detail_url = 'https://www.zhipin.com' + li.xpath('.//span[@class="job-name"]/a/@href').extract_first()
  
              # print(job_name, job_area)
              item['job_name'] = job_name
              item['job_area'] = job_area
              
              # 对详情页发请求获取详情页的源码数据
              # 手动请求的发送
              # 请求传参: meta={}, 可以将meta子弹传递给请求对应的回调函数
              header = self.get_header()
              yield scrapy.Request(url=detail_url, headers=header, callback=self.parse_detail, meta={'item': item})
  
          # 分页操作
          if self.page_num < 2:
              self.page_num += 1
              new_url = format(self.url % (self.page_num, self.page_num))
              print('正在爬取:%s' % new_url)
              time.sleep(5)
  
              header = self.get_header()
              yield scrapy.Request(url=new_url, headers=header, callback=self.parse)
  
      # 自定义回调函数: 解析详情页岗位描述
      def parse_detail(self, response):
          job_detail = response.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div//text()').extract()
          job_detail = ''.join(job_detail)
  
          item = response.meta['item']
          item['job_detail'] = job_detail
          yield item
  
      def close(spider, reason):
          print('爬虫结束')
  
  ```

## 4.10 图片数据爬取之 ImagesPipeline

### 基于scrapy爬取字符串类型的数据和爬取图片类型的数据区别？

+ 字符串：
  + 只需要基于xpath进行解析且提交管道进行持久化存储
+ 图片类型：
  + xpath解析出图片src的属性值后，还需要单独的对图片地址发起请求获取图片二进制数据

### ImagesPipeline

+ 只需要将图片的src的属性值进行解析并提交到管道，管道就会对图片的src进行请求发送，获取图片二进制数据，还会帮我们进行持久化存储。

### 需求：爬取站长素材中的高清图片

+ 使用流程

  + 数据解析（图片地址）
  + 将存储图片地址的item提交到指定的管道类
  + 在管道文件中自定义一个基于（继承）ImagesPipeLine的一个管道类，并重写以下方法
    + get_media_requests()
    + file_path()
  + 修改配置文件
    + 指定图片存储的目录：IMAGES_STORE = './images'
    + 开启管道：自定义的管道类

+ ```python
  import scrapy
  from scrapy.pipelines.images import ImagesPipeline
  
  
  class ImgsPipeline(ImagesPipeline):
      # 根据图片地址进行图片二进制数据的请求
      def get_media_requests(self, item, info):
          src = item['src']
          yield scrapy.Request(url=src, meta={'item': item})
  
      # 指定图片存储路径
      def file_path(self, request, response=None, info=None):
          # imgName = request.url.split('/')[-1]
  
          item = request.meta['item']
          file_format = item['src'].split('.')[-1]
          imgName = item['imgName']
          path = '%s.%s' % (imgName, file_format)
  
          return path
  
      def item_completed(self, results, item, info):
          # 返回给下一个即将被执行的管道类
          return item
  ```

## 4.11 CrawlSpider：Spider的一个子类

### 全站数据爬取的方式有两种

1. 基于Spider：手动请求发送
2. 基于CrawlSpider：根据正则表达式自动请求发送

### CrawlSpider的使用流程

+ 创建一个工程
  + scrapy startproject projectName
  + cd projectName
+ 创建爬虫文件（CrawlSpider）
  + scrapy genspider -t crawl spiderName [www.xxx.com](http://www.xxx.com/)
  + 链接提取器的作用
    + 根据正则表达式指定的规则（allow=r''）进行指定链接的提取
  + 规则解析器的作用
    + 将链接提取器提取到的链接进行指定规则的解析，并给 callback 传入参数

### 需求：爬取小说名称、人气、简介、最新章节

+ 分析：爬取的数据不在同一个页面中

  1. 使用链接提取器提取所有的页码链接
  2. 使用链接提取器提取所有的小说详情页的链接

+ 示例

  + sun.py

  + ```python
    # -*- coding: utf-8 -*-
    import scrapy
    from scrapy.linkextractors import LinkExtractor
    from scrapy.spiders import CrawlSpider, Rule
    from sunPro.items import SunproItem
    from sunPro.items import DetailItem
    
    
    # 需求：爬取小说分类、名称、人气、简介
    class SunSpider(CrawlSpider):
        name = 'sun'
        # allowed_domains = ['www.xxx.com']
        start_urls = ['https://www.69shu.org/fenlei/1_1/']
    
        # 链接提取器：根据指定规则（allow="正则"）进行链接的提取
        link_extractor = LinkExtractor(allow=r'fenlei/1_(?!16|\d{3,})')
        link_detail_extractor = LinkExtractor(allow=r'/book/\d+/(?!\d+\.html)')  # /book/\d+/(?!\d+\.html)
        rules = (
            # 规则解析器：将链接提取器提取到的链接进行指定规则（callback）的解析操作
            # follow=True：可以将链接提取器继续作用到，链接提取器提取的链接，对应的页面中
            Rule(link_extractor, callback='parse_novel_name', follow=False),
    
            Rule(link_detail_extractor, callback='parse_novel_detail', follow=False),
        )
    
        '''
        以下两个解析方法没有手动发起请求，是不可以实现请求传参的: 也就是说不能通过yield scrapy.Request() 回调其它函数
        无法将两个解析方法解析的数据存储到同一个item中，可以依次存储到两个item中
        '''
        # 解析小说类别、名称、作者
        def parse_novel_name(self, response):
            # item = {}
            # #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
            # #item['name'] = response.xpath('//div[su@id="name"]').get()
            # #item['description'] = response.xpath('//div[@id="description"]').get()
            # return item
    
            print('\n', response)
            # 注意：xpath表达式中不可以出现tbody标签
            li_list = response.xpath('/html/body/div[3]/div/div/div[2]/div[1]/div[2]/ul/li')
            for li in li_list:
                novel_category = li.xpath('./span[1]/text()').extract_first()
                novel_name = li.xpath('./span[2]/a/text()').extract_first()
                novel_author = li.xpath('./span[4]/text()').extract_first()
                # print(novel_category, novel_name, novel_author)
    
                item = SunproItem()
                item['novel_category'] = novel_category
                item['novel_name'] = novel_name
                item['novel_author'] = novel_author
                yield item
    
        # 解析小说人气和简介
        def parse_novel_detail(self, response):
            # print(response)
            novel_popularity = response.xpath('//*[@id="info"]/p/span/text()').extract_first()
            novel_synopsis = response.xpath('//*[@id="info"]/div[3]//text()').extract()
            novel_synopsis = ''.join(novel_synopsis)
            # print(novel_popularity)
    
            item = DetailItem()
            item['novel_popularity'] = novel_popularity
            item['novel_synopsis'] = novel_synopsis
            yield item
    ```

  + pipelines.py

  + ```python
    class SunproPipeline(object):
        def process_item(self, item, spider):
            '''
                将数据写入数据库时，如何保证数据的一致性?
                如果两个item类可以爬到相同的id，那就根据id插入数据，
                如果不行，那就用一个item类型，spider使用scrapy.Request(meta={'item':item})传参
            '''
    
            # 判定处理不同的 item对象
            if item.__class__.__name__ == 'DetailItem':
                novel_popularity = item['novel_popularity']
                novel_synopsis = item['novel_synopsis']
                print(novel_popularity)
            else:
                novel_category = item['novel_category']
                novel_name = item['novel_name']
                novel_author = item['novel_author']
                print(novel_category, novel_name, novel_author)
            return item
    ```

## 4.12 分布式爬虫

### 概念

+ 我们需要搭建一个分布式的机群（多台电脑），让其对一组资源进行分布联合爬取。

### 作用

+ 提升爬虫的效率

### 如何实现分布式？

+ 安装一个scrapy-redis的组件（该组件只能把数据存到redis数据库中）
+ 原生的scrapy不能实现分布式爬虫，必须要让scrapy结合着scrapy-redis组件一起实现分布式爬虫
+ 为什么原生的scrapy不可以实现分布式？
  + 调度器、管道不可以被分布式机群共享

### scrapy-redis 组件的作用

+ 可以给原生的 scrapy 框架提供可以被机群共享的管道和调度器

### 实现流程

+ 1 创建一个工程

  + scrapy startproject projectName

+ 2 创建一个基于 CrawlSpider 的爬虫

  + scrapy genspider -t crawl spiderName www.xxx.com

+ 3 修改当前的爬虫文件

  + 导包：from scrapy_redis.spiders import RedisCrawlSpider

  + 将start_urls和allowed_domains进行注释

  + 添加一个新属性：redis_key = 'queueName' （可以被共享的调度器队列名称）

  + 编写数据解析相关的操作

  + 将当前爬虫类的父类修改成：RedisCrawlSpider

  + 示例

    + ```python
      from scrapy.linkextractors import LinkExtractor
      from scrapy.spiders import CrawlSpider, Rule
      from scrapy_redis.spiders import RedisCrawlSpider
      from fbsPro.items import FbsproItem
      
      
      class FbsSpider(RedisCrawlSpider):
          name = 'fbs'
          # allowed_domains = ['www.xxx.com']
          # start_urls = ['http://www.xxx.com/']
      
          redis_key = 'fbs'
          rules = (
              Rule(LinkExtractor(allow=r'fenlei/1_(?!16|\d{3,})'), callback='parse_item', follow=True),
          )
      
          # 解析小说类别、名称、作者
          def parse_novel_name(self, response):
              # item = {}
              # #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
              # #item['name'] = response.xpath('//div[su@id="name"]').get()
              # #item['description'] = response.xpath('//div[@id="description"]').get()
              # return item
      
              print('\n', response)
              # 注意：xpath表达式中不可以出现tbody标签
              li_list = response.xpath('/html/body/div[3]/div/div/div[2]/div[1]/div[2]/ul/li')
              for li in li_list:
                  novel_category = li.xpath('./span[1]/text()').extract_first()
                  novel_name = li.xpath('./span[2]/a/text()').extract_first()
                  novel_author = li.xpath('./span[4]/text()').extract_first()
                  # print(novel_category, novel_name, novel_author)
      
                  item = FbsproItem()
                  item['novel_category'] = novel_category
                  item['novel_name'] = novel_name
                  item['novel_author'] = novel_author
      ```

+ 4 修改配置文件settings

  + ```python
    # -*- coding: utf-8 -*-
    
    # Scrapy settings for fbsPro project
    #
    # For simplicity, this file contains only settings considered important or
    # commonly used. You can find more settings consulting the documentation:
    #
    #     https://docs.scrapy.org/en/latest/topics/settings.html
    #     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
    #     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
    
    BOT_NAME = 'fbsPro'
    
    SPIDER_MODULES = ['fbsPro.spiders']
    NEWSPIDER_MODULE = 'fbsPro.spiders'
    
    
    # Crawl responsibly by identifying yourself (and your website) on the user-agent
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
    
    # Obey robots.txt rules
    ROBOTSTXT_OBEY = False
    
    LOG_LEVEL = 'ERROR'
    
    # 中间注释的不改动
    
    '''
    配置scrapy_redis
    '''
    # 指定管道
    ITEM_PIPELINES = {
       'scrapy_redis.pipelines.RedisPipeline': 400,
    }
    # 指定调度器
    # 增加了一个去重容器类的配置，作为使用Redis的set集合来存储请求的指纹数据，从而实现请求去重的持久化存储
    DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'
    # 使用scrapy-redis组件自己的调度器
    SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
    # 配置调度器是否要持久化
    # （也就是当爬虫结束了，要不要请空Redis中请求队列和去重指纹的set。如果是Ture则不清空，允许调度器暂停：从上次暂停的地方继续爬）
    SCHEDULER_PERSIST = True
    
    # 指定redis
    REDIS_HOST = '127.0.0.1'  # redis远程服务器的ip
    REDIS_PORT = 6379
    REDIS_ENCODING = 'utf-8'
    REDIS_PARAMS = {'password': '123456'}
    ```
  
+ 5 redis相关操作配置
  + 配置redis配置文件
    + Linux 或者 mac: redis.conf
    + windows: redis.windows.conf
    + 修改配置文件
      + 注释默认绑定：# bind 127.0.0.1
      + 关闭保护模式：protected-mode yes改为no
  + 结合配置文件开启redis服务
    + 进入redis目录：redis-server redis.windows.conf
    + 启动客户端：redis-cli
+ 6 执行工程
  
  + 进入spiders目录：scrapy runspider xxx.py
+ 7 向调度器的队列中放入一个起始 url
  + 在redis终端中输入以下命令（调度器的队列在redis的客户端中）
    + lpush fbs(redis_key = 'fbs') www.xxx.com
+ 8 爬取到的数据就会存储到 redis的proName: items 这个数据结构中

## 4.13 增量式爬虫

### 概念

+ 监测网站数据更新的情况，只会爬取网站最新更新出来的数据。 

### 分析

+ 指定一个起始url
+ 基于 CrawlSpider 获取其它页码链接
+ 基于Rule将其它页码链接进行请求
+ 从每一个页码对应的页码源码中解析出每一个电影详情页的URL
+ 核心：检测电影详情页的url之前有没有请求过
  + 将爬取过的电影详情页的 url 存储到redis的set数据结构
+ 对详情页的url发起请求，然后解析出电影的名称和简介
+ 进行持久化存储

### 示例

+ ```python
  # -*- coding: utf-8 -*-
  import scrapy
  
  from redis import Redis
  from serialNumber.items import SerialnumberItem
  
  
  class FhkSpider(scrapy.Spider):
      name = 'fhk'
      allowed_domains = ['www.xxx.com']
      start_urls = ['http://ys.okfanhao.com/fhdq_renqi_0_0_1.htm']
  
      url = 'http://ys.okfanhao.com/fhdq_renqi_0_0_%d.html'
      page_num = 1
      # 创建redis链接对象
      conn = Redis(host='127.0.0.1', port=6379)
  
      def parse(self, response):
          print(response)
          li_list = response.xpath('//article[@class="bd"]/ul/li')
          # print(li_list)
          for li in li_list:
              movie_name = li.xpath('./div/h3/a/text()').extract_first()
              # movie_ticket = li.xpath('./div/h3/span/b/text()').extract_first()
              # 获取详情页的url
              detail_url = 'http://ys.okfanhao.com/' + li.xpath('./div/h3/a/@href').extract_first()
              # 将详情页的url存入redis的set中
              ex = self.conn.sadd('urls', detail_url)
              if ex == 1:
                  print('%s没有被爬取过，存入redis数据库中并爬取其对应的详细信息' % detail_url)
                  yield scrapy.Request(url=detail_url, callback=self.parse_detail)
              else:
                  print('%s: 该影片早已收录在库，无需再爬!' % movie_name)
  
          # 分页
          if self.page_num <= 400:
              self.page_num += 1
              url = format(self.url % self.page_num)
              print(self.page_num)
              print(url)
              return scrapy.Request(url=url, callback=self.parse)
  
      # 处理每个番号详细数据
      def parse_detail(self, response):
          serial_number = response.xpath('//div[@class="col-md-6 infos"]/h2/text()').extract_first()
          video_name = serial_number
          author_name = response.xpath('//div[@class="col-md-6 infos"]/h4[2]/a/text()').extract()
          author_name = author_name[0] if len(author_name) == 1 else ','.join(author_name)
          video_tag = response.xpath('//div[@class="col-md-6 infos"]/h4[3]/a/text()').extract()
          video_tag = video_tag[0] if len(video_tag) == 1 else ','.join(video_tag)
          publish_date = response.xpath('//div[@class="col-md-6 infos"]/h4[1]/a/text()').extract_first()
          video_ticket = response.xpath('//div[@class="col-md-6 infos"]/p/span/b/text()').extract_first()
  
          print(serial_number, author_name, video_tag, video_ticket, publish_date)
  
          item = SerialnumberItem()
          item['serial_number'] = serial_number
          item['video_name'] = video_name
          item['author_name'] = author_name
          item['video_tag'] = video_tag
          item['publish_date'] = publish_date
          item['video_ticket'] = video_ticket
          yield item
  
      def close(spider, reason):
          spider.conn.close()
          print('爬虫结束，redis链接关闭！')
  
  ```

# 5. Scrapy 配置

## 5.1 scrapy添加cookie的三种方式

1. 修改 settings.py 文件

   - Cookies_enabled = False 取消注释
   - 取消注释后 headers中设置的 cookie 就可以使用了
   - 这种方法最简单，同时 cookie 可以直接从浏览器上粘贴

2. 使用下载中间件 DownloadMiddleware

   - downloadmiddleware 取消注释
   - Cookies_enabled = False 取消注释并改为 True
   - 在middlewares.py 文件中修改下载中间件的 process_request() 方法，添加 request.cookes = {}

3. 爬虫文件中重写 start_request() 方法

   - ```python
     def start_requests(self):
         yield scrapy.Request(url, dont_filter=True, cookies={})
     ```

## 5.2 提升 scrapy 的效率

### 增加并发

+ 默认scrapy开启的并发线程为32个，可以适当进行增加。
+ 在settings配置文件中修改CONCURRENT_REQUESTS = 100值为100,并发设置成了为100。

### 降低日志级别

+ 在运行 scrapy 时，会有大量日志信息的输出，为了减少CPU的使用率。可以设置log输出信息为INFO或者ERROR即可。
+ 在配置文件中编写：LOG_LEVEL = ‘INFO’

### 禁止 cookie

+ 如果不是真的需要cookie，则在scrapy爬取数据时可以禁止cookie从而减少CPU的使用率，提升爬取效率。
+ 在配置文件中编写：COOKIES_ENABLED = False

### 禁止重试

+ 对失败的HTTP进行重新请求（重试）会减慢爬取速度，因此可以禁止重试。
+ 在配置文件中编写：RETRY_ENABLED = False

### 减少下载超时

+ 如果对一个非常慢的链接进行爬取，减少下载超时可以能让卡住的链接快速被放弃，从而提升效率。
+ 在配置文件中进行编写：DOWNLOAD_TIMEOUT = 10 超时时间为10s

## 5.3 在 Pycharm 上调试 scrapy项目

+ 在 scrapy 生成的爬虫项目下新建一个 main.py 文件，写入下列内容：

  + main.py 与 scrapy.cfg 处于同一目录下

  + ```python
    #!/usr/bin/env python
    #-*- coding:utf-8 -*-
    
    from scrapy.cmdline import execute
    import os
    import sys
    
    #添加当前项目的绝对地址
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    #执行 scrapy 内置的函数方法execute， 使用 crawl 爬取并调试，最后一个参数jobbole 是我的爬虫文件名
    execute(['scrapy', 'crawl', 'jobbole'])
    ```

+ 接下来在爬虫文件中设置断点，回到 main.py 文件中右键点击 debug main.py 就可以进行调试了。

