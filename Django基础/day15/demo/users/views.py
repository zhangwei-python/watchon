import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# 视图函数
from django.urls import reverse


def decorator(fn):

    def inner(request, *args, **kwargs):
        print("装饰器被调用了")
        print("视图函数被调用后，获取请求方式: ", request.method)
        result = fn(request, *args, **kwargs)
        print("视图函数被调用后，获取响应状态码: ", result.status_code)
        return result

    return inner


# def index(request, index):
@decorator      # index = decorator(index)
def index(request):
    # print(index)

    # url = reverse("user:index")
    # print(url)

    # 查询参数
    # print(request.GET.get("user_name"))
    # 请求体的表单数据
    # print(request.POST.get("a"))
    # print(request.POST.getlist("a"))
    # 请求体非表单数据
    # print(json.loads(request.body.decode("utf-8"))['name'])
    # 请求头数据
    # print(request.META.get("CONTENT_TYPE"))

    return HttpResponse("假装是一个首页")
