from django.urls import re_path

from . import views

# 子应用的名字空间名（子应用别名）
app_name = "user"

urlpatterns = [
    # re_path(r'^index/$', views.index),

    # 路由路径写在子路由中
    # 路由命名: 方便找到特点视图的路径
    re_path(r"^users/index/$", views.index, name="index"),
]

