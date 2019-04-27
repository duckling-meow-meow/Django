from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def do_normal_map(request):
    print("In do_normal_map")
    return HttpResponse("This is normal_map")


def with_param(request, year, month):
    return HttpResponse("This is with param {0},{1}".format(year,month))


def do_app(r):
    return HttpResponse("这是个子路由")


def do_page_zh(r, pn):
    return HttpResponse("这是第"+pn+"页")


def do_page_en(r, pn):
    return HttpResponse("Page Number is {0}".format(pn))


def external_param(r, name):
    # 下面用format也可以，return后面不要加“，”
    return HttpResponse("your name is " + name)


