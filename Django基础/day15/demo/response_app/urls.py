from django.contrib import admin
from django.urls import path, include, re_path

from . import views

urlpatterns = [

    re_path(r"^response/index/$", views.index),

    re_path(r"^response/login/$", views.login),

]