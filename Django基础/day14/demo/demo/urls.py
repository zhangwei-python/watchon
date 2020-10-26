"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from users import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 总路由写一部分路径，子路由再写另外一部分
    # path("users/", include("users.urls")),

    # 完整路由写在总路由中.
    # path("users/index/", views.index),

    # 总路由不写路径，直接包含。
    path("", include("users.urls")),

    path("", include("get_request.urls")),

]
