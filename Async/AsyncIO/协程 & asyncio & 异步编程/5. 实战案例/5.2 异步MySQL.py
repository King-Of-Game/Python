#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 11/30/2020 12:10 PM
# __software__ : PyCharm
import asyncio
import aiomysql


'''示例1'''


# async def execute():
#     # 异步IO操作：连接MySQL
#     conn = await aiomysql.connect(host='localhost', port=3306, user='root', password='123456', db='test')
#
#     # 网络IO操作：创建游标
#     cur = await conn.cursor()
#
#     # 网络IO操作：执行SQL
#     # strSql = r"insert into t_student (id,name,password,birthday,major) values('%s','%s','%s','%s','%s')"
#     # strSql = "INSERT INTO t_student (id,name,password,birthday,major) VALUES ('1002','jack','123456','2020-12-1','计算机')"
#
#
#     strSql = 'select * from t_student'
#
#     await cur.execute(strSql)
#
#     # 网络IO操作：获取SQL结果
#     result = await cur.fetchall()
#     print(result)
#
#     # 网络IO操作：关闭连接
#     await cur.close()
#     conn.close()
#
#
# def main():
#     asyncio.run(execute())
#
#
# if __name__ == '__main__':
#     main()


'''示例2'''


async def execute(host, password):
    # 异步IO操作：连接MySQL(遇到IO会自动切换任务)
    conn = await aiomysql.connect(host=host, port=3306, user='root', password=password, db='test')

    # 网络IO操作：创建游标(遇到IO会自动切换任务)
    cur = await conn.cursor()

    # 网络IO操作：执行SQL(遇到IO会自动切换任务)
    await cur.execute('select * from t_student')

    # 网络IO操作：获取SQL结果(遇到IO会自动切换任务)
    result = await cur.fetchall()
    print(result)

    # 网络IO操作：关闭连接(遇到IO会自动切换任务)
    await cur.close()
    conn.close()
    print('结束', host)


async def main():
    task_list = [
        execute('47.91.42.197', '123456'),
        execute('localhost', '123456')
    ]
    await asyncio.wait(task_list)


if __name__ == '__main__':
    asyncio.run(main())

