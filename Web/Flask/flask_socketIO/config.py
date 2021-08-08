# -*- coding: utf-8 -*-


class Config(object):

    SECRET_KEY = 'tianqiong'
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

    # [time]
    # 每隔free_time秒判断是否有websocket连接
    TIME_FREE_TIME = 2
    # 当有websocket连接时，每隔interval秒查询数据库。
    TIME_INTERVAL = 1

    # [cache_count]
    CACHE_COUNT = 1000

    # [templates]
    TEMPLATE = 10

    # [play]
    SHUFFLING_TIME = 10
    # 播放历史时间，单位为秒
    LISHI_TIME = 3
    # 最终flag
    FLAG_BOSS = "172.16.10.220"
    # socket接口
    SOCKET_EVENT = "message"
    SOCKET_URL = "/tq/train/info"

    # game_time_interval
    GAME_TIME_INTERVAL = 1

    # send_new_list_interval
    SEND_NEW_LIST_INTERVAL = 1

    # query_flag_interval
    QUERY_FLAG_INTERVAL = 1

    # SCORE
    SCORE_INTERVAL = 300
    SCORE_SEND_INTERVAL = 5
    REDIS_DB_SCORE = 5
    # 处理时时数据的线程数量
    ATTACK_THREAD_COUNT = 2
    NETWORK_THREAD_COUNT = 2

    # 获取redis队列的超时时间
    REDIS_MQ_INTERVAL = 5

    # kafka
    # 测试
    KAFKA_HOST = '192.168.117.55'
    KAFKA_PORT = ('9092', '9093', '9094')
    KAFKA_GROUP_ID = 'bigScreenConsumer'
    KAFKA_TOPIC = 'RawData'


    #网络流量放在db0





