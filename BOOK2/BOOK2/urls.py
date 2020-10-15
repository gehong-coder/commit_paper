"""BOOK2 URL Configuration

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
urlpatterns = [
    path('admin/', admin.site.urls),
    path('addbook/', views.AddBook),
    path('books/', views.GetBooks),
    #path('book/', views.GetBook),
    re_path(r'books/(\d+)/delete', views.DeleteBook),
    re_path(r'books/(\d+)/change', views.ChangeBook),
    path('findbook/',views.FindBook),
    path('getauthor/',views.GetAuthor),
    path('salebook/',views.SaleBooks),
    path('data/',views.GetData),
    re_path(r'salebook/(\d+)/changesale', views.ChangeSale),
    path('data2/',views.GetData2)

   # path('changesale/',views.ChangeSale)
]