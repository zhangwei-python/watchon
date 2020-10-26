from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r"^book/index/$", views.BookView.as_view()),
]