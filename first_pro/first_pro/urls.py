"""first_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,re_path,include,register_converter
#repath 使用正则化集进行路径匹配
from app01 import views
from app01 import urls
#使用自定义路径匹配
#1.先导入规则，注册转换器
from app01.urlconvert import MonthConvert
register_converter(MonthConvert,"MC")

urlpatterns = [

    path('admin/', admin.site.urls),
    path('time/',views.time),
    #登陆页面-全局登陆
    path('login.html/',views.login,name='log'),


    #反向解析
    re_path(r'app01/',include(("app01.urls","app01"))),
    #加上房间名字-就可以不怕重名啦-namespace
    re_path(r'app02/',include(("app02.urls","app02"))),
    path("art/<str:year>",views.pathyear),
    path("art1/<path:year>", views.pathyear),
   # '''path:有名分组的使用。'''
    path("a1/<MC:month>",views.month)
]


'''
url：http
路径：
'''