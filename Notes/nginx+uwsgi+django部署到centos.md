# nginx+uwsgi+django部署到centos

## 1.安装并配置mysql

### 1.1 如果需要卸载系统自带的mysql

+ 1.yum remove mysql  卸载mysql
+ 2.rpm -qa|grep mysql  检查是否存在mysql 
  + rpm -e --nodeps xxx  删除查找出来的内容（一般有5条）
+ 3.find / -name mysql  查找卸载残留的mysql文件和库
  + rm -rf [document&filename]  删除残留的mysql文件

### 1.2下载并配置 mysql

+ wget 'https://dev.mysql.com/get/mysql57-community-release-el7-11.noarch.rpm'  下载mysql的yum源

+ rpm -Uvh mysql57-community-release-el7-11.noarch.rpm  安装yum源

+ yum repolist all | grep mysql  查看 mysql 所有版本的仓库

+ yum install -y mysql-community-server  安装mysql

+ systemctl start mysqld  启动mysql服务

+ systemctl status mysqld  查看状态

+ grep 'temporary password' /var/log/mysqld.log  查看默认的密码

  1. mysql -u root -p  # 用默认密码登录mysql

   1. set global validate_password_policy=0;  # 修改密码安全策略（默认为1）
     2. set global validate_password_length=1;  # 修改密码最小长度（默认为8）
   3. alter user 'root'@'localhost' identified by '123456';  # 修改root用户的密码为123456
     4. GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'root123456' WITH GRANT OPTION;   # 设置可以远程登录mysql
   5. flush privileges;  # 配置立即生效
3. 开启3306端口
  
   - 这里开启端口没用的话，就在腾讯云的设置页面上把防火墙打开
   
     + ```shell
       1、开启端口3306
       firewall-cmd --zone=public --add-port=3306/tcp --permanent
       systemctl start firewalld  #如果防火墙进程没运行
       2.重启防火墙
       firewall-cmd --reload
       3.查看已开放的端口
       firewall-cmd --list-ports
       ```

  4. 修改配置文件（可选）

     1. vim /etc/my.cnf

     2. 在[mysqld]下面添加，不需要分号

        1. 设置字符集为utf8

           + character-set-server=utf8

           + show variables like 'char%';  就可以查看到字符集都是utf8了

        2. 使mysql支持group by语句

           + sql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION  

        3. 设置时区为东八区

           + default-time_zone = '+8:00'

     3. systemctl restart mysqld  重启mysql服务使配置生效

  5. 设置开机自启动
  
     1. systemctl enable mysqld
     2. systemctl daemon-reload

## 2.安装并配置python3

### 2.1 下载对应版本的python3.tgz文件

+ wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz
+ 手动下载https://www.python.org/downloads/source/  

### 2.2 解压并安装

+ tar xfz Python-3.6.8.tgz
+ cd Python-3.6.8
+ ./configure --enable-shared --with-ssl=openssl
+ make && make install

+ 配置软连接
  + ln -s /usr/local/python3/bin/python3.6 /usr/bin/python3
  + ln -s /usr/local/python3/bin/pip3.6 /usr/bin/pip3
+ 测试
  + python3

## 3.上传web项目并用python3试运行

### 3.1 设置pip下载源

+ mkdir ~/.pip
+ cd ~/.pip
+ vim pip.conf
  + [global]
    index-url=https://pypi.tuna.tsinghua.edu.cn/simple
    trusted-host = pypi.tuna.tsinghua.edu.cn

### 3.2 安装项目所需模块

+ 可以把所需模块安装到虚拟环境中
+ pip3 install -U pip
+ pip3 install django==3.0.5
+ sudo yum install python3-devel mysql-devel
  + pip3 install mysqlclient==2.0.1

### 3.3 上传压缩项目文件并解压

1. 安装 lrzsz 工具（能在Xshell下，上传/下载文件）
   - yum -y install lrzsz
2. 上传压缩文件
   - cd 到服务器 www 目录下
   - rz（然后就可以手动选择本机上的文件）
3. 解压 zip 文件
   - unzip -o web.zip -d document/  # 以覆盖的方式解压到指定文件夹下

### 3.4 试运行项目

+ 1.修改配置文件

  + vim /var/www/YiXuan/YiXuan/setting.py

  + ```python
    DEBUG = False
    ALLOWED_HOSTS = ['*']
    ```

+ 2.运行django项目

  + python3 manange.py runserver

## 4.pip3安装并配置uwsgi

### 4.1 卸载pip2的uwsgi

+ pip uninstall uwsgi

### 4.2 pip3安装uwsgi

+ pip3 install uwsgi

### 4.3 设置软链接（可以直接使用 uwsgi 命令）

+ ln -s /usr/local/python3/bin/uwsgi /usr/bin/uwsgi3

### 4.4 新建 uwsgi.ini 配置文件

- uwsgi --http :9090 --wsgi-file main.py --callable app --processes 4 --threads 2 --stats 127.0.0.1:9191

+ vim /var/www/YiXuan/uwsgi.ini

  + ```python
    [uwsgi]
    #配置和nginx交互的socket连接
    socket = 127.0.0.1:8888
    
    # 配置本地访问的http链接
    http = 127.0.0.1:8080
    
    #配置项目路径，项目的所在目录
    chdir = /var/www/YiXuan
    
    #配置静态文件
    static-map = /static=/var/www/YiXuan/static
    
    #配置wsgi接口模块文件路径
    wsgi-file = YiXuan/wsgi.py
    
    #配置启动的进程数
    processes = 2
    
    #配置每个进程的线程数
    threads = 4
    
    #配置启动管理主进程
    master=True
    
    #配置最大解析的数据包
    buffer-size = 65536
    
    chmod-socket = 664
    
    #配置存放主进程的进程号文件
    pidfile = uwsgi.pid
    
    #配置dump日志记录
    daemonize = uwsgi.log
    
    vacuum = true
    
    ```


### 4.5 uwsgi 常用命令

+ uwsgi3 --ini[可选参数] uwsgi.ini  #根据配置ini配置文件启动uwsgi
+ uwsgi3 --stop uwsgi.pid  #根据自动生成的.pid文件停止uwsgi
+ uwsgi3 --reload uwsgi.ini  #重载配置

+ 6.杀死uwsgi进程

  + killall -9 uwsgi3

## 5.安装并配置nginx

### 5.1 安装nginx

+ yum install -y nginx
+ 如果出错，就先安装Nginx的依赖库“pcre”
  + yum install -y pcre pcre-devel
+ 如果没有找到安装源
  + yum install epel-release

### 5.2 设置软连接

+ ln -s /usr/sbin/nginx /usr/bin/nginx

### 5.3 设置开启自启动

+ vim /etc/rc.local

  + ```shell
    # 在末尾添加
    /usr/local/nginx/sbin/nginx
    ```

### 5.4 配置nginx.conf文件

+ ```python
  # For more information on configuration, see:
  #   * Official English Documentation: http://nginx.org/en/docs/
  #   * Official Russian Documentation: http://nginx.org/ru/docs/
  
  user nginx;
  worker_processes auto;
  error_log /var/log/nginx/error.log;
  pid /run/nginx.pid;
  
  # Load dynamic modules. See /usr/share/doc/nginx/README.dynamic.
  include /usr/share/nginx/modules/*.conf;
  
  events {
      worker_connections 1024;
  }
  
  http {
      log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                        '$status $body_bytes_sent "$http_referer" '
                        '"$http_user_agent" "$http_x_forwarded_for"';
  
      access_log  /var/log/nginx/access.log  main;
  
      sendfile            on;
      tcp_nopush          on;
      tcp_nodelay         on;
      keepalive_timeout   65;
      types_hash_max_size 2048;
  
      include             /etc/nginx/mime.types;
      default_type        application/octet-stream;
  
      # Load modular configuration files from the /etc/nginx/conf.d directory.
      # See http://nginx.org/en/docs/ngx_core_module.html#include
      # for more information.
      # include /etc/nginx/conf.d/*.conf;
  
      server {
          listen       80 default_server;
          listen       [::]:80 default_server;
          server_name  _;
          root         /usr/share/nginx/html;
  
          # Load configuration files for the default server block.
          # include /etc/nginx/default.d/*.conf;
  
          location / {
  	    include uwsgi_params;
              uwsgi_pass 0.0.0.0:8888;
          }
  
  	location /static {
              alias /var/www/YiXuan/static;
      	}
  
          error_page 404 /404.html;
          location = /404.html {
          }
  
          error_page 500 502 503 504 /50x.html;
          location = /50x.html {
          }
      }
  
  }
  
  ```

### 5.5 检验 nginx.conf 正确性

- nginx -t

### 5.6 开启80端口

+ ```shell
  # 开启端口80
  firewall-cmd --zone=public --add-port=80/tcp --permanent
  # 重启防火墙
  firewall-cmd --reload
  # 查看已开放的端口
  firewall-cmd --list-ports
  
  # 如果80端口被占用
  lsof -i :80  #查询80端口的占用情况
  kill -9 [进程id]
  ```

### 5.7 把配置好的 nginx.conf 放入 /etc/nginx 目录下

### 5.8 nginx常用命令

+ nginx  #以默认的.conf文件启动nginx
+ nginx -c nginx.conf  #加载.conf文件并启动nginx
+ nginx -s reload  #重启nginx
+ nginx -s quit  #退出nginx

## 6.使用supervisor管理uwsgi和nginx

+ tips: supervisor可以在程序意外关闭时自动重新启动

+ 1.安装supervisor（不行就用pip2）

  + pip3 install supervisor

+ 2.生成supervisord.conf配置文件

  + echo_supervisord_conf > /etc/supervisord.conf

+ 3.在配置文件末尾添加内容

  + vim /etc/supervisord.conf

  + ```python
    [program:yixuan]
    command=uwsgi3 --ini /var/www/YiXuan/uwsgi.ini
    #directory=/var/www/YiXuan
    startsecs=10
    stopwaitsecs=10
    autostart=true
    autorestart=true
    # 如果"uwsgi.ini"文件中开启了多进程，一定要加上下面两句，否则会导致再次启动或重启uWSGI失败。
    stopasgroup=true
    killasgroup=true
    
    [program:gunicorn]
    environment=PATH="/home/jack/WebApps/tq_match_bigscreen_backend/venv/bin" 
    directory=/home/jack/WebApps/tq_match_bigscreen_backend/
    command=gunicorn -b 0.0.0.0:8888 -k eventlet --workers=1 main:app
    startsecs=10
    stopwaitsecs=10
    autostart=true
    autorestart=true
    stopasgroup=true
    killasgroup=true
    
    [program:nginx]
    command=nginx -c /var/www/tq_match_bigscreen_backend/deploy/nginx.conf -g 'daemon off;'
    startsecs=10
    stopwaitsecs=10
    autostart=true
    autorestart=true
    stopasgroup=true
    killasgroup=true
    ```

+ 4.利用supervisor启动管理程序

  + supervisorctl -c /etc/supervisord.conf start yixuan  #启动yiuxan程序
  + **ERROR (spawn error)**：可能是该进程已存在所导致的
    + ps aux|grep [program_name]
    + killall -9 [program_name]
    + 补充：
      + 如果还是出现错误“**ERROR (spawn error)**”，也可能是因为“uwsgi.ini”中添加了“daemonize ”（日志）项导致的，将其删除即可。
      + 如果提示没有supervisor.sock
        + touch /var/run/supervisor.sock
        + chmod 777 /var/run/supervisor.sock
      + 提示：Unlinking stale socket /tmp/supervisor.sock
        + unlink /tmp/supervisor.sock
  + **Error: Another program is already listening...**：可能是已经有“supervisor.sock”文件被链接（上一次启动Supervisor造成的）。
    + find / -name supervisor.sock  #找到该文件
    + unlink /pathto/supervisor.sock  #取消已有链接
  + 常用命令
    + supervisord  #启动supervisord
    + supervisorctl update  #按配置文件更新
    + supervisorctl status  #查看任务状态
    + supervisorctl start [program_name]  #启动某个程序命令
    + supervisorctl restart [program_name]  #重启某个程序命令
    + supervisorctl stop [program_name]  #停止某个程序命令
    + supervisorctl <start/restart/stop> all  #控制所有程序命令

# --------------------分隔符--------------------

# 补充

## WSGI / uwsgi / uWSGI 三者的区别

1. WSGI 是一种通信协议。
2. uwsgi 是一种线路协议而不是通信协议，在此常用于在uWSGI服务器与其他网络服务器的数据通信。
3. uWSGI 是实现了uwsgi 和 WSGI 两种协议的Web服务器。
   - uWSGI 是一个Web服务器，它实现了WSGI协议、uwsgi、http等协议。Nginx中HttpUwsgiModule的作用是与uWSGI服务器进行交换。