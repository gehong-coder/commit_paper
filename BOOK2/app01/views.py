from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from app01.models import *


def AddBook(request):

    # 对数据库进行添加操作
    # 因为现在book不是一张单表，所以先使用它使用的那一张表进行创建对象
    #先查询单表里面的数据-之
    pub = Publish.objects.all()
    aut  = Author.objects.all()
    #
    if request.method=='POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        publishDate = request.POST.get('date')
        publishid = request.POST.get('pub')
        author=request.POST.get('author')
        pub_obj = Publish.objects.filter(nid=publishid).first()
        book_obj = Book.objects.create(title=title, price=price, publishDate=publishDate, publish=pub_obj)
        book_obj.authors.add(author)
        return redirect("/books/")
   # book_obj = Book.objects.create(title="1", price=11, publishDate='2016-7-9', publish=pub_obj)
    return render(request,'addbook.html',locals())

def GetBooks(request):
    #操作数据库
    books = Book.objects.all()
    return render(request,'books.html',locals())

def DeleteBook(request,id):
    Book.objects.filter(nid=id).delete()
    return redirect('/books/')

def ChangeBook(request,id):
    pub = Publish.objects.all()
    book = Book.objects.filter(nid=id).first()
    aut = Author.objects.all()
    if request.method=="POST":
        title = request.POST.get('title')
        price = request.POST.get('price')
        date = request.POST.get('date')
        publishid = request.POST.get('pub')
        author = request.POST.get('author')
        pub_obj = Publish.objects.filter(nid=publishid).first()
        Book.objects.filter(nid=id).update(title=title,price=price,publishDate=date,publish=pub_obj)
        book_obj = Book.objects.filter(nid=id).first()
        book_obj.authors.add(author)
        return redirect('/books/')
    return render(request,'changebook.html',locals())

def FindBook(request):
    pub = Publish.objects.all()
    aut = Author.objects.all()
    if request.method=="POST":
        title = request.POST.get('findname')
        authorname = request.POST.get('authorname')
        publishid = request.POST.get('pub')
        if title:
            book = Book.objects.filter(title=title).first()
            return render(request,'book.html',locals())
        elif authorname:
            author_obj = Author.objects.filter(name=authorname).first()
            book_list = author_obj.book_set.all()
            return render(request,'authorinfor.html',locals())
        elif publishid:
            pub_obj = Publish.objects.filter(nid=publishid).first()
            book_list =  pub_obj.book_set.all()
            print(book_list)
            return render(request,'publishbooks.html',locals())
    return render(request,'findbook.html',locals())

def GetAuthor(request):
    pub = Publish.objects.all()
    aut = Author.objects.all()
    if request.method=="POST":
        id = request.POST.get('author')
        author_obj = Author.objects.filter(nid=id).first()
        #print(author_obj.authorDetail.telephone)
        book_list = author_obj.book_set.all()
        print(book_list)
        return render(request,'authorinfor.html',locals())
    return render(request,'author.html',locals())

#一对多：zhengxiang
def SaleBooks(request):
    # 操作数据库
    books = Book.objects.all()
    salebooks = SaleBook.objects.all()
    for salebook in salebooks:
        if salebook.snumber==None:
            salebook.objects.update(snumber=0)
   # return render(request, 'books.html', locals())
    return render(request,'salebook.html',locals())
def GetData(request):
    books = Book.objects.all()
    salebooks = SaleBook.objects.all()
    b = []
    s = []
    for book in books:
        b.append(book.title)
        sbook = SaleBook.objects.filter(booksale=book.nid).first()
        if sbook:
            s.append(sbook.snumber)
        else:
            s.append(0)
    print(s)
    print(b)
    # return render(request, 'books.html', locals())
    return render(request, 'datacharts.html', locals())


def ChangeSale(request,id):
    #传来的是bookid，有的书还没有在salebook表中
    book = Book.objects.filter(nid=id).first()
    salebook=SaleBook.objects.filter(booksale_id=id).first()
    if salebook:
        salebook = salebook
    else:
        book=Book.objects.filter(nid=id).first()
        SaleBook.objects.create(snumber=0,booksale=book)
    book = Book.objects.filter(nid=id).first()
    salebook = SaleBook.objects.filter(booksale_id=id).first()
    if request.method=="POST":
        name  = request.POST.get('title')
        snumber = request.POST.get('number')
        print(snumber)
        SaleBook.objects.filter(booksale_id=id).update(snumber=snumber)
        return redirect("/salebook/")
    return render(request,'changesale.html',locals())



def GetData2(request):
    D=[]
    publish = Publish.objects.all()
    print(publish)
    for publish_obj in publish:
        data = dict(name="",value="")
        book_list = publish_obj.book_set.all()
        d=0
        print(book_list)
        for book in book_list:
            d=d+1
        data['name']=publish_obj.name
        data['value']=d
        D.append(data)
    print(D)
    #print(D[0].k
    # eys())
    return render(request, 'datapublish.html',locals())