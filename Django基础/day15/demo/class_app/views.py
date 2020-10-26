from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# 使用类实现视图：叫类视图
# 优点: 1.可读性更好 2.复用性更高

# 1. 必须继承View
# 2. 类视图中的方法名是固定的，请求方式小写
from django.utils.decorators import method_decorator
from django.views.generic.base import View


# 装饰器
def decorator(fn):
    def inner(request, *args, **kwargs):
        print("装饰器被调用了")
        print("视图函数被调用后，获取请求方式: ", request.method)
        result = fn(request, *args, **kwargs)
        print("视图函数被调用后，获取响应状态码: ", result.status_code)
        return result
    return inner


# @decorator      # RegisterView=decorator(RegisterView) 错误用法
# 2. @method_decorator(装饰器, name="需要装饰的方法名")
# @method_decorator(decorator, name="get")
@method_decorator(decorator, name="dispatch")
class RegisterView(View):

    # 1.给类视图的方法添加装饰器: method_decorator(装饰器) 转换 装饰器 为适合装饰类方法的装饰器
    # @method_decorator(decorator)
    def get(self, request):
        print("GET 请求 注册业务")
        return HttpResponse("返回注册页面")

    def post(self, request):
        print("POST 请求 注册业务")
        return HttpResponse("执行注册逻辑")


# 扩展类: 定义父类扩展子类的方法. 子类使用多继承，继承父类的方法.
class GetMixin(object):
    def get(self, request, *args, **kwargs):
        return HttpResponse("扩展类的get 方法")


class PostMixin(object):
    def post(self, request, *args, **kwargs):
        return HttpResponse("扩展类的Post 方法")


class LoginView(GetMixin, PostMixin, View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Login实现的get 方法")

