from django.contrib import admin
from django.urls import path, re_path, include
# repath 使用正则化集进行路径匹配
from app01 import views
from app01 import urls

urlpatterns = [
    # 路由匹配
    re_path("index/",views.index,name="index"),
    re_path(r'^articles/2003/$', views.Special_2003,name='sc2003'),
    re_path(r'^articles/([0-9]{4})/$', views.Aritive,name='artive'),
    #有名分组
    #re_path(r'^articles/(?P<y>[0-9]{4})/$',views.ym)#安找y，m进行分组-后台穿过去值
]