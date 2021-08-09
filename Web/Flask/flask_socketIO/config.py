# -*- coding: utf-8 -*-


class Config(object):

    SECRET_KEY = 'test'
    DEBUG = True
    # [server]
    # SERVER_HOST = "192.168.137.235"
    # SERVER_PORT = 8488
    WEB_SERVER_HOST = '0.0.0.0'
    WEB_SERVER_PORT = 8888


    # [redis]
    # REDIS_HOST = '127.0.0.1'
    REDIS_HOST = '192.168.211.128'
    REDIS_PORT = 6379
    REDIS_DB = 0
    REDIS_PWD = ''
    REDIS_STREX_TIME = 5


