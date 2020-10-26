from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View


class SessionView(View):

    def get(self, request):

        request.session['user_name'] = 'zhangsan'
        request.session['is_login'] = 'True'
        request.session.set_expiry(3600)

        return HttpResponse("登录页面")


class SessionIndexView(View):

    def get(self, request):

        name = request.session.get("user_name")
        is_login = request.session.get("is_login")

        if is_login == "True":
            return HttpResponse("%s是登录用户，可以访问首页" % name)
        else:
            return HttpResponse("没有登录，请登录后再进入首页")

class SessionOutView(View):

    def get(self, request):

        # del request.session['is_login']
        # request.session.clear()
        request.session.flush()

        return HttpResponse("退出登录")