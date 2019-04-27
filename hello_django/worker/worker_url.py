from django.conf.urls import include, url
from django.contrib import admin

# from worker import views as tv
# 同一级目录下，可以用以下的方式导入
from . import views

urlpatterns = [
    url(r'sun/', views.do_app),
]