

# def simple_middleware(get_response):
#     # 此处编写的代码仅在 Django 第一次配置和初始化的时候执行一次。
#     print("中间件初始化")
#
#     def middleware(request):
#
#         # 此处编写的代码会在每个请求处理视图前被调用。
#         print("调用视图函数前，获取请求对象中请求方式: ", request.method)
#
#         response = get_response(request)
#
#         # 此处编写的代码会在每个请求处理视图之后被调用。
#         print("调用视图函数后, 获取响应对象中状态码: ", response.status_code)
#
#         return response
#
#     return middleware
#
#
# def simple_middleware2(get_response):
#     # 此处编写的代码仅在 Django 第一次配置和初始化的时候执行一次。
#     print("2中间件初始化")
#
#     def middleware(request):
#
#         # 此处编写的代码会在每个请求处理视图前被调用。
#         print("2调用视图函数前，获取请求对象中请求方式: ", request.method)
#
#         response = get_response(request)
#
#         # 此处编写的代码会在每个请求处理视图之后被调用。
#         print("2调用视图函数后, 获取响应对象中状态码: ", response.status_code)
#
#         return response
#
#     return middleware


from django.utils.deprecation import MiddlewareMixin


class MiddleWare(MiddlewareMixin):

    """自定义中间件"""
    def process_request(self, request):
        """处理请求前自动调用"""
        print('process_request1 被调用')

    def process_view(self, request, view_func, view_args, view_kwargs):
        # 处理视图前自动调用
        print('process_view1 被调用')

    def process_response(self, request, response):
        """在每个响应返回给客户端之前自动调用"""
        print('process_response1 被调用')
        return response


class MiddleWare2(MiddlewareMixin):

    """自定义中间件"""
    def process_request(self, request):
        """处理请求前自动调用"""
        print('process_request2 被调用')

    def process_view(self, request, view_func, view_args, view_kwargs):
        # 处理视图前自动调用
        print('process_view2 被调用')

    def process_response(self, request, response):
        """在每个响应返回给客户端之前自动调用"""
        print('process_response2 被调用')
        return response