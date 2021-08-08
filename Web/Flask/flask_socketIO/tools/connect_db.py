import os

import redis
import json
import random
from config import Config


# 连接redis db0
def connect_redis():
    return redis.Redis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_DB, password=Config.REDIS_PWD,
                       decode_responses=True, charset='UTF-8', encoding='UTF-8')


# 连接redis db6
def connect_redis_db6():
    return redis.Redis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=6, password=Config.REDIS_PWD,
                       decode_responses=True, charset='UTF-8', encoding='UTF-8')


if __name__ == '__main__':
    redisObj = connect_redis()
    data_list = redisObj.zrange('不想和队友一队', 0, -1)
    list1 = []
    for i in range(len(data_list)):
        if i > 360:
            # string转json
            json_data = json.loads(data_list[i])
            # 用当前时间替换原来的时间
            # json转string
            string_data = json.dumps(json_data, ensure_ascii=False)
            list1.append(string_data)
    print(list1)

