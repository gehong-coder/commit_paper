from django.shortcuts import render

# Create your views here.
import os
from django.shortcuts import render,HttpResponse
from django.urls import reverse
def index(request):
    name="ddd"
    b='true'
    l={"j":"hb","yy":"ii"}
    i=["JF",'dsd',"d"]
    user = "sd"
    s= 10
    return render(request,"index.html",locals())
''' locals可以传递所有的便来过'''