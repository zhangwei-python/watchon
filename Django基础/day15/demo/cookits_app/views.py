from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View


class BookView(View):

    def get(self, request):
        print("登录成功")
        # name = request.POST.get("name")
        name = "zhangsan"

        # 1.设置cookit到浏览器中 (通过响应对象)
        response = HttpResponse("返回cookit信息")
        response.set_cookie("user_name", name, max_age=3600)
        response.set_cookie("is_login", "True", max_age=3600)

        return response

class BookIndexView(View):

    def get(self, request):

        # 2. 获取cookie （通过请求对象)
        print(request.COOKIES)
        name = request.COOKIES.get("user_name")
        is_login = request.COOKIES.get("is_login")
        if is_login == "True":
            return HttpResponse("%s是登录用户，可以访问首页" % name)
        else:
            # return redirect("/book/login/")
            return HttpResponse("没有登录，请登录后再进入首页")


class BookOutView(View):

    def get(self, request):

        # 3. 删除cookie的值 (通过响应对象)
        response = HttpResponse("退出登录")
        response.delete_cookie("is_login")

        return response

