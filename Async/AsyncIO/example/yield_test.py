# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 9/12/2020 3:50 PM
# __software__ : PyCharm


# 消费者
def consumer():
    r = ''
    while True:
        n = yield r  # yield 后面的变量必须有值，而return后面可以什么都没有
        if not n:  # 如果n不存在则执行
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'
# 生产者
def produce(c):
    c.send(None)  # 生成器一开始启动时必须发送一个None值
    n = 0
    while n < 3:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()



if __name__ == '__main__':
    c = consumer()
    produce(c)











