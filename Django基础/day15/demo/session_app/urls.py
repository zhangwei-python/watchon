from django.contrib import admin
from django.urls import path, include, re_path

from . import views

urlpatterns = [
    re_path(r"^session/login/$", views.SessionView.as_view()),

    re_path(r"^session/index/$", views.SessionIndexView.as_view()),

    re_path(r"^session/logout/$", views.SessionOutView.as_view()),

]