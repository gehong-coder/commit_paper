from django.contrib import admin
from django.urls import path, re_path, include
# repath 使用正则化集进行路径匹配
from app02 import views
from app02 import urls


urlpatterns = [
    # 路由匹配
    re_path('index/',views.index,name='index')
]