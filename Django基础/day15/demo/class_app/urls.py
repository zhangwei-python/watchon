from django.contrib import admin
from django.urls import path, include, re_path

from . import views


urlpatterns = [

    # 类视图使用:
    # re_path(路径, 视图函数)

    # views.RegisterView.as_view() :
    #   返回真正的视图函数 (分发处理函数: GET -> get POST -> post)

    # views.RegisterView.as_view() --> as_view(RegisterView, ....) --> return view

    # re_path(r"^class/register/$", views.RegisterView.as_view.view)
    # re_path(r"^class/register/$", views.decorator(views.RegisterView.as_view()))
    re_path(r"^class/register/$", views.RegisterView.as_view()),

    re_path(r"^class/login/$", views.LoginView.as_view()),
]
