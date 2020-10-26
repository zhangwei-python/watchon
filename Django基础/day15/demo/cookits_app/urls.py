from django.contrib import admin
from django.urls import path, include, re_path

from . import views

urlpatterns = [
    re_path(r"^book/login/$", views.BookView.as_view()),

    re_path(r"^book/index/$", views.BookIndexView.as_view()),

    re_path(r"^book/logout/$", views.BookOutView.as_view()),

]