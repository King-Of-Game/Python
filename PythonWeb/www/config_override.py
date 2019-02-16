#!/usr/bin/python3
# _*_ coding: utf-8 _*_
# 服务器数据库的连接配置
__author__ = 'YiXuan'

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': '123',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}