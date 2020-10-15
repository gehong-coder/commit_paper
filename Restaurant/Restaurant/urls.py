"""Restaurant URL Configuration

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
from django.urls import path,re_path
from app01 import views
import re
pattern = u'\u6211.*?\u3002'
pat = re.compile(pattern)
urlpatterns = [
    path('admin/', admin.site.urls),

    path('addfood/', views.AddFood),
    path('foods/', views.GetFoods),
    re_path(r'foods/(\d+)/delete', views.DeleteFood),
    re_path(r'foods/(\d+)/change', views.ChangeFood),
    path('findfood/',views.FindFood),
    path('getcooker/',views.GetCooker),
    path('salefood/',views.SaleFoods),
    re_path(r'salefood/(\d+)/changesale', views.ChangeSale),

    path('data/', views.GetData),
    path('data2/',views.GetData2),

    path('addcanteen/',views.AddCanteen),
    path('canteens/',views.GetCanteens),
    re_path(r'canteens/(\d+)/delete', views.DeleteCanteen),
    re_path(r'canteens/(\d+)/change', views.ChangeCanteen),
    path('sigaldata/',views.singalData),
    re_path(u'sigaldata/foods/([\u4e00-\u9fa5]+)/show',views.showSigalData)
    #这个是用来显示单个菜品
    #path('data/',views.GetData),
]
