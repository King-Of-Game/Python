#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'YiXuan'

import os, re
from datetime import datetime

# 导入Fabric API:
from fabric.api import *

# # 服务器登录用户名:
# env.user = 'YiXuan'
# # sudo用户为root:
# env.sudo_user = 'root'

# 服务器登录用户名和秘钥:
env.hosts = ['47.101.200.21']
env.key_filename = 'PythonWeb.pem'

# 服务器MySQL用户名和口令:
db_user = 'root'
db_password = '123456'




# 生成压缩文件
_TAR_FILE = 'dist-awesome.tar.gz'   # 压缩文件名
def build():
    includes = ['static', 'templates', 'transwarp', 'favicon.ico', '*.py', '*.txt']
    excludes = ['test', '.*', '*.pyc', '*.pyo']
    local('rm -f dist/%s' % _TAR_FILE)
    with lcd(os.path.join(os.path.abspath('.'), 'www')):
        cmd = ['tar', '--dereference', '-czvf', '../dist/%s' % _TAR_FILE]
        cmd.extend(['--exclude=\'%s\'' % ex for ex in excludes])
        cmd.extend(includes)
        local(' '.join(cmd))



# 把打包文件上传至服务器，解压，重置www软链接，重启相关服务 _TAR_FILE = 'dist-awesome.tar.gz'
_REMOTE_TMP_TAR = '/tmp/%s' % _TAR_FILE     # 服务器上存放上传的压缩文件的地址
_REMOTE_BASE_DIR = '/srv/awesome'           # 服务器上Web项目的地址

def deploy():
    newdir = 'www-%s' % datetime.now().strftime('%y-%m-%d_%H.%M.%S')
    # 删除已有的tar文件:
    sudo('rm -f %s' % _REMOTE_TMP_TAR)
    # 上传新的tar文件:
    put('dist/%s' % _TAR_FILE, _REMOTE_TMP_TAR)
    # 创建新目录:
    with cd(_REMOTE_BASE_DIR):
        sudo('mkdir %s' % newdir)
    # 解压到新目录:
    with cd('%s/%s' % (_REMOTE_BASE_DIR, newdir)):
        sudo('tar -xzvf %s' % _REMOTE_TMP_TAR)
    # 重置软链接:
    with cd(_REMOTE_BASE_DIR):
        sudo('rm -f www')
        sudo('ln -s %s www' % newdir)
        sudo('chown root:root www')
        sudo('chown -R root:root %s' % newdir)
    # 重启Python服务和nginx服务器:
    with settings(warn_only=True):
        sudo('supervisorctl stop awesome')
        sudo('supervisorctl start awesome')
        sudo('/etc/init.d/nginx reload')

if __name__ == '__main__':
    build()