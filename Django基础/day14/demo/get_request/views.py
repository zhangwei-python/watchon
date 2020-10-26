from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import json


# 请求报文 解析成的 请求对象 request
# 获取查询参数字符串:
def get_query(request):

    # <QueryDict: {}>
    # <class 'django.http.request.QueryDict'>
    # 通过对象.GET 属性 获取浏览器发送的查询字符串， 无论是GET请求方式还是POST请求方式
    print(request.GET)
    print(type(request.GET))

    # QueryDict.get() : 1对1时，获取到key对应的值
    #                   1对多时, 获取到key对应的最后一个值
    #           getlist() : 1对多时, 获取到key对应的所有值
    print(request.GET.get("user_name", ""))
    print(request.GET.get("like", ""))
    print(request.GET.getlist("like", []))

    return HttpResponse("获取查询参数成功")


# 通过请求资源路径获取参数
def weather(request, city, year):

    print(city)
    print(year)

    return HttpResponse("查询天气成功")


# 获取前端发送的表单数据(请求体)
def get_form(request):

    # 通过POST属性获取请求体的表单数据
    print(request.POST)

    print(request.POST.get("b", "默认值"))
    print(request.POST.get("a", "默认值"))
    print(request.POST.getlist("a", []))

    return HttpResponse("获取表单数据成功")


# 或股前端发送的非表单数据(请求体 可以是各种类型)
def get_body(request):

    # 通过body属性获取前端发送的非表单类型请求体
    print(request.body)

    print(request.body.decode("utf-8"))

    # json.dumps(): 字典转换成json字符串
    # json.loads(): json字符串转换成字典

    json_dict = json.loads(request.body.decode("utf-8"))
    print(type(json_dict), json_dict)
    print(json_dict['name'])

    return HttpResponse("获取非表单数据")


# 获取请求头数据
def get_head(request):

    # 通过META 属性获取请求头信息
    print(request.META['CONTENT_TYPE'])
    print(request.META['HTTP_NAME'])

    # request对象的其他属性
    print(request.method)
    print(request.user)
    print(request.encoding)
    print(request.path)
    print(request.FILES)

    return HttpResponse("获取前端的请求头成功")


