from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import connection
from serialnumber.models import SerialNumber
from django.core.paginator import Paginator
import datetime


# Create your views here.


def serial_list(request, page_num):

    serial_lists = SerialNumber.objects.order_by('-video_ticket')

    paginator = Paginator(serial_lists, 15)

    page_num = 1 if page_num == "" else int(page_num)

    now_page = paginator.page(page_num)  # 返回第number页的page类实例对象

    page_list = []
    num_pages = paginator.num_pages  # 返回分页之后的总页数
    page_range = paginator.page_range  # 返回分页后的页码列表

    if num_pages >= 5:
        if 3 <= page_num <= num_pages - 2:
            page_list = page_range[page_num - 3:page_num + 2]
        elif page_num < 3:
            page_list = page_range[0:page_num + 2]
        elif page_num > num_pages - 2:
            page_list = page_range[page_num-3:num_pages]
    else:
        page_list = page_range

    context = {
        "now_page": now_page,
        "page_list": page_list,

    }

    return render(request, "serialnumber/serial_list.html", context)

    # return render(request, 'serialnumber/serial_list.html')


# 模糊查询
def search_item(request):
    search_text = request.GET['search_text']
    search_text = '%' + search_text + '%'
    data = {}
    list1 = []

    sql = "SELECT * \
        from serialnumber_serialnumber \
        where author_name like '%s' or serial_number like'%s' or video_tag like '%s' \
        order by video_ticket desc; " % (search_text, search_text, search_text)
    cursor = connection.cursor()
    cursor.execute(sql)
    tup_items = cursor.fetchall()

    for tup in tup_items:
        json = {
            'id': tup[0],
            'serial_number': tup[1],
            'video_name': tup[2],
            'author_name': tup[3],
            'video_tag': tup[4],
            'publish_date': datetime.datetime.strftime(tup[5], '%Y-%m-%d'),
            'video_ticket': tup[6],
            'magnet_url': tup[7],
        }
        list1.append(json)
        data['data'] = list1

    return JsonResponse(data)


# def show_serial_list(request, page_num):
#     serial_lists = SerialNumber.objects.all()
#     print(serial_lists)
#     paginator = Paginator(serial_lists, 20)
#     if page_num == "":
#         page_num = 1
#     else:
#         page_num = int(page_num)
#     # page_num = 1 if page_num == "" else int(page_num)
#     page = paginator.page(page_num)
#     context = {
#         "page": page,
#     }
#     return render(request, "serialnumber/serial_list.html", context)
#
#


