from django.contrib import admin
from django.urls import path, include, re_path

from . import views

app_name = "user"

urlpatterns = [

    # re_path(r"^user/(?P<index>[a-z]+)/$", views.index, name="index"),

    re_path(r"^user/index/$", views.index, name="index"),

]
