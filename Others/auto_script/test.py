# -*- coding: utf-8 -*-
# ! /usr/bin/env python3
# @Date__ : 2021/3/26 13:53
# @Author__ : YiXuan
# @File : test.py
# @Software : PyCharm
# @Version : 
# @Description :

import os
import time
import logging
import traceback
import logging.handlers


def init_logger(log_file):
    dir_path = os.path.dirname(log_file)
    try:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
    except Exception as e:
        pass

    handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=20 * 1024 * 1024, backupCount=10)
    fmt = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)
    logger_instance = logging.getLogger('logs')
    logger_instance.addHandler(handler)
    logger_instance.setLevel(logging.DEBUG)
    if len(logger_instance.handlers) != 1:
        logger_instance.handlers.pop()
    else:
        pass
    return logger_instance


def install(config, mylog):
    try:
        mylog.info('[+] Start to install')
        for command in config['command_lists']:
            index = config['command_lists'].index(command)
            mylog.info('[+] Step {0}, {1}'.format(str(index), command))
            res = os.system(command)
            if res != 0:
                raise ValueError('[-] Failed to excute: {0}'.format(command))
        mylog.info('[+] Success to install')
        return True
    except Exception as e:
        mylog.info(str(e))
        mylog.info(str(traceback.format_exc()))  # traceback 模块用于跟踪异常，返回信息。
        return False


def get_web_server():
    '''
    os.system(cmd): 返回值是脚本的退出状态码
    os.popen(cmd): 返回值是脚本执行过程中的输出内容。
    '''
    res = None
    try:
        res = os.popen('netstat -nlp | grep :::80').readlines()
        res = res[0].strip().split('/')[-1]  # 得到当前 占用80端口的服务
    except:
        res = os.popen('netstat -nlp | grep 0.0.0.0:80').readlines()
        res = res[0].strip().split('/')[-1]
    return res


if __name__ == '__main__':
    APP_NAME = 'YiXuan'
    BASE_DIR = os.getcwd() + os.sep

    MYSQL_HOST = '127.0.0.1'
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PWD = 123456
    MYSQL_DB = 'test'

    log_path = '{0}log/'.format(BASE_DIR)
    log_file = '{0}{1}.log'.format(log_path, APP_NAME)
    failed_file_path = '{0}{1}.failed'.format(log_path, APP_NAME)
    success_file_path = '{0}{1}.success'.format(BASE_DIR, APP_NAME)
    my_log = init_logger(log_file=log_file)

    try:
        config = dict(
            command_lists=[
                'rm -rf {0}'.format(failed_file_path),
                'rm -rf {0}'.format(success_file_path),
                # "mysql -h{0} -P{1} -u{2} -p{3} -e 'drop database if exists {4}'".format(
                #     MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PWD, MYSQL_DB  # mysql -e (execute => 执行sql语句)
                # ),
                # "mysql -h{0} -P{1} -u{2} -p{3} -e 'create database if not exists {4}'".format(
                #     MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PWD, MYSQL_DB
                # ),
                # "mysql -h{0} -P{1} -u{2} -p{3} {4} -e 'source {5}{6}.sql'".format(
                #     MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PWD, MYSQL_DB, BASE_DIR, MYSQL_DB
                # ),
                'rm -rf /var/www/YiXuan',
                'unzip {0}{1}.zip -d /var/www'.format(BASE_DIR, APP_NAME),
                'touch {0}'.format(success_file_path)
            ],
        )

        isSuccess = False
        count = 0
        # 最大命令重试次数
        while count < 3:
            if not install(config, my_log):
                count += 1
                time.sleep(10)  # 10s后重试
                continue
            else:
                isSuccess = True
                break

        if isSuccess is False:  # 当isSuccess为False
            raise ValueError('[-] Time out, failed to install app: {0}'.format(APP_NAME))

    except Exception as e:
        my_log.info(str(e))
        my_log.info(str(traceback.format_exc()))
        with open(failed_file_path, 'w') as f:
            f.write(e)
