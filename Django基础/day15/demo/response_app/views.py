from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def index(request):
    # 1. 使用HttpResponse构建响应对象
    # 1.1.一般使用方式: 返回响应体内容, 其他使用默认
    # return HttpResponse("假装是一个首页")

    # 1.2.指定状态码返回: status=400
    # return HttpResponse("假装是一个首页", status=400)

    # 1.3.指定响应体类型: content_type=application/json
    # json_str = '{"name": "xiaoming"}'
    # return HttpResponse(json_str, content_type="application/json", status=200)

    json_str = '{"name": "xiaoming"}'
    response_obj = HttpResponse(json_str, content_type="application/json", status=200)
    # 1.4.给响应体自定义一个响应头的键值对。
    response_obj['app_name'] = 'itcast.cn'

    # 1.5.对象属性: content, status_code
    print(response_obj.content)
    print(response_obj.status_code)

    return response_obj


def login(request):

    # 2.使用HttpResponse的子构建响应体对象
    # response_obj = HttpResponse("<h1>404 not Found</h1>", status=404)
    # 2.1HttpResponseNotFound: status_code = 404
    # response_obj = HttpResponseNotFound("<h1>Not Found</h1>")

    # 2.2 JsonResponse: 1. content_type="application/json" 2. dict --> json_str
    # dict = {'name':'itcast.cn', 'flag':'已登录'}
    # response_obj = JsonResponse(dict, json_dumps_params={"ensure_ascii":False})   #
    # return response_obj

    # 3. redirect： 重定向页面 (本站地址，其他域名地址)
    # return redirect("/user/index/")

    # 3.2.先反向解析命名路由再重定向。
    # url = reverse("user:index")
    # print(url)
    # return redirect(url)

    return redirect("https://www.baidu.com")