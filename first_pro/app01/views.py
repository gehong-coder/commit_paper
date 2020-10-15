import os
from django.shortcuts import render,HttpResponse
from django.urls import reverse
# Create your views here.
#验证反向解析
def index(request):
    return HttpResponse(reverse("app01:index"))

def time(request):
    import time
    ctime = time.time()
    return render(request,"timer.html",{"date":ctime})
'''render（）'''
def Special_2003(request):
    '''#反向解析--/app01/articles/2003/'''
    url = reverse('sc2003')
    url1 = reverse('artive',args=(4009,))#往前找
    #因为前面输入了一个两个加个参数
    print(url)
    print(url1)
    return HttpResponse("2003")

#登陆页面
def login(request):
    '''request中包含了所有的前段请求所有的数据'''
    #根据get请求和post请求进行数据不同的更新
    print(request.method)
    #判断
    if request.method=="GET":
        #说明现在进行的是刷新页面的请求
        return render(request,"login.html")
    else:#说明
        print(request.GET)
        print(request.POST)
        '''获得前面传来的数据'''
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")


        if user=="1" and pwd=="1":
            return HttpResponse("okk")
        else:
            return HttpResponse("no")



''' 有分组的时候才会产生新的参数'''
def Aritive(request,year):
    return HttpResponse("nainhub")

'''path新用法'''
'''固定的参数不能忘记'''
def pathyear(request,year):
    print(year)
    print(type(year))
    return HttpResponse("ok")


'''固定的参数不能忘记'''
'''自定义命名规则'''
def month(request,month):
    print(month)
    print(type(month))
    return HttpResponse("ok")