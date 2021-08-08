#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 11/1/2020 7:57 PM
# __software__ : PyCharm

import requests
import re, os, time, random
from multiprocessing import Pool
from lxml import etree



# 生成mrd
def generate_mrd():
    mrd = '0.'
    for i in range(18):
        rd = random.randint(0, 9)
        mrd += str(random.randint(0, 9))
    return mrd

# 生成正确的video_src
def generate_video_src(video_src, number):
    split1 = video_src.split('/')
    split2 = split1[-1].split('-')
    # print(split1)
    # print(split2)
    cont_number = 'cont-' + number
    split1[-1] = ''
    split2[0] = cont_number
    new_video_src = '/'.join(split1) + '-'.join(split2)
    return new_video_src

# 得到视频名称和下载链接
def get_video_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    }
    print('正在爬取url：%s 中的热门视频信息' % url)
    Session = requests.Session()
    # get方法是一个阻塞的方法
    response = Session.get(url=url, headers=headers)
    if response.status_code != 200:
        print(url, '请求失败！')
        return response

    page_text = response.text
    tree = etree.HTML(page_text)
    div_tree = tree.xpath('//ul[@id="listvideoListUl"]/li/div')
    for div in div_tree:
        video_name = div.xpath('./a/div[2]/text()')[0] + '.mp4'
        video_number = div.xpath('./a/@href')[0]

        number = video_number.split('_')[-1]
        # 取得视频数据的ajax接口
        url = 'https://www.pearvideo.com/videoStatus.jsp'
        # 生成mrd
        mrd = generate_mrd()
        param = {
            # 'wd': kw
            'contId': number,
            'mrd': mrd
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
            'Referer': 'https://www.pearvideo.com/%s' % video_number,
        }
        response = requests.get(url=url, params=param, headers=headers)
        pattern = re.compile('"srcUrl":"(.*?)"')
        video_src = pattern.findall(response.text)[0]
        # print('原来的视频src：', video_src)
        new_video_src = generate_video_src(video_src, number)
        # print('正确的视频src：', new_video_src)

        dict1 = {
            'video_name': video_name,
            'video_src': new_video_src
        }

        # tuple1 = (video_name, new_video_src)
        video_infos.append(dict1)

# 对视频的二进制数据进行持久化存储
def get_video_file(video_info):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    }
    video_name = video_info['video_name']
    video_src = video_info['video_src']

    print(video_src)
    video_content = requests.get(url=video_src, headers=headers).content
    print('%s正在下载...' % video_name)
    with open('./videos/' + video_name, 'wb') as fp:
        fp.write(video_content)
        print('%s下载成功！' % video_name)






if __name__ == '__main__':
    video_infos = []

    # 梨视频生活板块页面url
    url = 'https://www.pearvideo.com/category_5'

    # 得到梨视频生活板块视频信息及下载链接
    get_video_info(url)
    # print(video_infos)

    if not os.path.exists('./videos'):
        os.mkdir('./videos')

    '''使用单线程串行方式执行'''
    # start_time = time.time()
    #
    # for video_info in video_infos:
    #     get_video_file(video_info)
    #
    # end_time = time.time()
    # print('单线程串行总耗时：%.5f 秒' % float(end_time - start_time))


    '''使用线程池方式执行'''
    start_time = time.time()

    pool = Pool(4)
    # 将href_list列表中的每一个元素作为参数传递给getVideo方法
    video_data = pool.map(get_video_file, video_infos)
    end_time = time.time()

    pool.close()
    pool.join()

    print('多进程总耗时：%.5f 秒' % float(end_time-start_time))
