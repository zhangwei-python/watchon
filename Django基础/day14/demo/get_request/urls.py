from django.urls import re_path

from . import views

app_name = 'get_request'

urlpatterns = [
    re_path(r'^get_query/$', views.get_query, name="get_query"),

    # re_path(r"^weather/shenzhen/20200719/$", views.weather),

    # 正则分组: group(1) group(2)
    # re_path(r"^weather/([a-z]+)/(\d{8})/$", views.weather),

    # django 自动会对url进行分组提取字符串，并且按照别名给视图函数传递参数。
    re_path(r"^weather/(?P<city>[a-z]+)/(?P<year>\d{8})/$", views.weather),


    re_path(r"^get_form/$", views.get_form),

    re_path(r"^get_body/$", views.get_body),

    re_path(r"^get_head/$", views.get_head),
]