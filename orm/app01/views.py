from django.shortcuts import render,HttpResponse

# Create your views here.
#导入数据库
from app01.models import Book1
def index(request):
    #添加表记录
    #1要，save
    book_obj = Book1(id=1,title="月亮与六便士",price="30",pub_date="1981-11-15",publish="时代文艺出版社",state=True)
    book_obj.save()
    #2.直接生成数据-create直接生成了一个对象
    #book_obj = Book1.objects.create(title="小王子",price="28",pub_date="1942-10-8",publish="人民出版社",state=True)
    #print(book_obj.title)
    #print(book_obj.state)
    #'''单表查询--all   返回值：queryset-对象类型'''
    '''book_all = Book1.objects.all()
    print(book_all)
    for i in book_all:
        print(i.title,i.price)
    print(book_all[1].publish)
    '''
    #''' first，last'''-一个对象
    '''book = Book1.objects.all().first()
    print(book)'''
   # '''fiter对象'''-多个对象
    b = Book1.objects.filter(price=30)
    print(b)
    # get方法-一条记录
    book1 = Book1.objects.get(title="小王子")
    print(book1)
    #exclude-多个对象
    b2 = Book1.objects.exclude(price=30)
    print(b2)
    #order_by-返回多个对象-queryset可以调用order——by
    b_oder = Book1.objects.all().order_by('price')
    print(b_oder)
    #count()-返回一个数字
    bs = Book1.objects.all().count()
    print(bs)
    #exists方法
    ret = Book1.objects.all().exists()
    if ret:
        print('oo')
    #values 方法-调用者queryset可以调用，生成的也是queryset--字典
    t = Book1.objects.all().values('title')
    print(t)
    #<QuerySet [{'title': '月亮与六便士'}, {'title': '小王子'}]>
    #values 调用的是queryset--放的是值
    t1 = Book1.objects.all().values_list('title')
    print(t1)
    #<QuerySet [('月亮与六便士',), ('小王子',)]>

    #disrinct-去重一般配合values使用-字典
    rc=Book1.objects.values('title').distinct()
    print(rc)

    # 大于和小于的
    ww = Book1.objects.filter(price__gt=100)
    print(ww)
    bx = Book1.objects.all().filter(title__startswith='小')
    print(bx)
    bl=Book1.objects.all().filter(title__contains='王')
    print(bl)
    #山河该、


    return HttpResponse("ok")
