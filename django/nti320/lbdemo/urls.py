# lbdemo/urls.py

from django.conf.urls import url
from lbdemo import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]