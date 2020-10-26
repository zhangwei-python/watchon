from django.http import HttpResponse
from django.shortcuts import render
import time
# Create your views here.
from django.urls import reverse


def index(request):

    # val = 1 / 0

    # print(time.ctime())

    # 反向解析：通过命名视图找到路径 (通过视图代码找到路径)
    url = reverse("user:index")
    print(url)

    url = reverse("get_request:get_query")
    print(url)

    return HttpResponse("test code")
