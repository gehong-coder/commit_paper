from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from app01.models import Book
def AddBook(request):
    #获取前端的值、
    if request.method=='POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        date = request.POST.get('date')
        publish = request.POST.get('publish')
        #对数据库进行添加操作
        book_obj = Book.objects.create(title=title,price=price,pub_date=date,publish=publish)
        return redirect("/books/")
    return render(request,'addbook.html',)
def GetBooks(request):
    #操作数据库
    books = Book.objects.all()
    return render(request,'books.html',locals())
def DeleteBook(request,id):
    Book.objects.filter(id=id).delete()
    return redirect('/books/')

def ChangeBook(request,id):
    book = Book.objects.filter(id=id).first()
    if request.method=="POST":
        title = request.POST.get('title')
        price = request.POST.get('price')
        date = request.POST.get('date')
        publish = request.POST.get('publish')
        Book.objects.filter(id=id).update(title=title,price=price,pub_date=date,publish=publish)
        return redirect('/books/')
    return render(request,'changebook.html',locals())