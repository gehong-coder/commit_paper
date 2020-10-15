
# Create your views here.
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from app01.models import *


# Create your views here.



def AddFood(request):

    # 对数据库进行添加操作
    # 因为现在book不是一张单表，所以先使用它使用的那一张表进行创建对象
    #先查询单表里面的数据-之
    canteen = Canteen.objects.all()
    cookers  = Cooker.objects.all()
    #
    if request.method=='POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        designDate = request.POST.get('date')
        canteenId = request.POST.get('canteen')
        cooker=request.POST.get('cooker')

        can_obj = Canteen.objects.filter(nid=canteenId).first()
        food_obj = Food.objects.create(name=name, price=price, designDate=designDate, canteen=can_obj)
        food_obj.cookers.add(cooker)

        return redirect("/foods/")
   # book_obj = Book.objects.create(title="1", price=11, publishDate='2016-7-9', publish=pub_obj)
    return render(request,'addfood.html',locals())

def GetFoods(request):
    #操作数据库
    foods = Food.objects.all()
    return render(request,'foods.html',locals())

def DeleteFood(request,id):
    Food.objects.filter(nid=id).delete()
    return redirect('/foods/')

def ChangeFood(request,id):
    canteen = Canteen.objects.all()
    food = Food.objects.filter(nid=id).first()
    cookers = Cooker.objects.all()
    if request.method=="POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        designDate = request.POST.get('date')
        canteenId = request.POST.get('canteen')
        cooker = request.POST.get('cooker')
        canteen_obj = Canteen.objects.filter(nid=canteenId).first()
        Food.objects.filter(nid=id).update(name=name,price=price,designDate=designDate,canteen=canteen_obj)
        food_obj = Food.objects.filter(nid=id).first()
        food_obj.cookers.add(cooker)
        return redirect('/foods/')
    return render(request,'changefood.html',locals())

def FindFood(request):
    canteen = Canteen.objects.all()
    cookers = Cooker.objects.all()
    if request.method=="POST":
        name = request.POST.get('findname')
        cookername = request.POST.get('cookername')
        canteenId = request.POST.get('canteen')
        if name:
            food = Food.objects.filter(name=name).first()
            return render(request,'food.html',locals())
        elif cookername:
            cooker_obj = Cooker.objects.filter(name=cookername).first()
            food_list = cooker_obj.food_set.all()
            return render(request,'cookerinfo.html',locals())
        elif canteenId:
            canteen_obj = Canteen.objects.filter(nid=canteenId).first()
            food_list =  canteen_obj.food_set.all()
            print(food_list)
            return render(request,'designfood.html',locals())
    return render(request,'findfood.html',locals())

def GetCooker(request):
    canteen = Canteen.objects.all()
    cookers = Cooker.objects.all()
    if request.method=="POST":
        id = request.POST.get('cooker')
        cooker_obj = Cooker.objects.filter(nid=id).first()
        #print(author_obj.authorDetail.telephone)
        food_list = cooker_obj.food_set.all()
        print(food_list)
        return render(request,'cookerinfo.html',locals())
    return render(request,'cooker.html',locals())
def SaleFoods(request):
    # 操作数据库
    foods = Food.objects.all()
    salefoods = SaleFood.objects.all()
    for salefood in salefoods:
        if salefood.snumber==None:
            salefood.objects.update(snumber=0)
   # return render(request, 'books.html', locals())
    return render(request,'salefood.html',locals())

def ChangeSale(request,id):
    #传来的是bookid，有的书还没有在salebook表中
    food = Food.objects.filter(nid=id).first()
    salefood=SaleFood.objects.filter(foodsale=id).first()
    if salefood:
        salefood = salefood
    else:
        food=Food.objects.filter(nid=id).first()
        SaleFood.objects.create(snumber=0,foodsale=food)
    food = Food.objects.filter(nid=id).first()
    salefood = SaleFood.objects.filter(foodsale_id=id).first()

    if request.method=="POST":
        name  = request.POST.get('name')
        snumber = request.POST.get('number')
        print(snumber)
        SaleFood.objects.filter(foodsale_id=id).update(snumber=snumber)
        return redirect("/salefood/")
    return render(request,'changesale.html',locals())

def GetData0(request):#销量统计
    foods = Food.objects.all()
    salefoods = SaleFood.objects.all()
    b = []#菜品名字
    s = []#菜品产量
    for food in foods:
        b.append(food.name)
        sfood = SaleFood.objects.filter(foodsale=food.nid).first()
        if sfood:
            s.append(sfood.snumber)
        else:
            s.append(0)
    print(s)
    print(b)
    # return render(request, 'books.html', locals())
    return render(request, 'datacharts.html', locals())

def GetData(request):#销量统计
    foods = Food.objects.all()
    salefoods = SaleFood.objects.all()
    b = []#菜品名字
    s = []#菜品产量
    '''
    统计销量时，使用一个状态码来进行标记这个销量是否已经被记录，
    所以开始设计成false后来再设计成true，如果是true说明已经被改变
    '''
    break_tag = False
    for food in foods:
        for bname in b:
            if bname==food.name:
                index = b.index(bname)
                print(index)#6
                sfood = SaleFood.objects.filter(foodsale=food.nid).first()
                if sfood:
                    snumber = sfood.snumber
                else :
                    snumber = 0
                print(s[index])#7
                print(sfood)
                s[index] += snumber
                break_tag=True
        if break_tag == False :
            b.append(food.name)
            sfood = SaleFood.objects.filter(foodsale=food.nid).first()
            if sfood:
                s.append(sfood.snumber)
            else:
                s.append(0)
    print(s)
    print(b)

    # return render(request, 'books.html', locals())
    return render(request, 'datacharts.html', locals())

def GetData2(request):
    D=[]
    canteen = Canteen.objects.all()
    print(canteen)
    for canteen_obj in canteen:
        data = dict(name="",value="")
        food_list = canteen_obj.food_set.all()
        d=0
        print(food_list)
        for book in food_list:
            d=d+1
        data['name']=canteen_obj.name
        data['value']=d
        D.append(data)
    print(D)
    #print(D[0].k
    # eys())
    return render(request, 'datacanteen.html',locals())

'''获取所有的餐馆'''
def GetCanteens(request):
    # 操作数据库
    canteens = Canteen.objects.all()
    return render(request, 'canteens.html', locals())

def AddCanteen(request):
    canteen = Canteen.objects.all()
    #
    if request.method == 'POST':
        name = request.POST.get('name')
        city = request.POST.get('city')
        email = request.POST.get('email')
        Canteen.objects.create(name=name,city=city,email=email)
        return redirect('/canteens/')
    # book_obj = Book.objects.create(title="1", price=11, publishDate='2016-7-9', publish=pub_obj)
    return render(request, 'addcanteen.html', locals())
def DeleteCanteen(request,id):
    Canteen.objects.filter(nid=id).delete()
    return redirect('/canteens/')

def ChangeCanteen(request,id):
    canteen_obj = Canteen.objects.filter(nid=id).first()
    if request.method=="POST":
        name = request.POST.get('name')
        city = request.POST.get('city')
        email = request.POST.get('email')
        Canteen.objects.filter(nid=id).update(name=name,city=city,email=email)
        return redirect('/canteens/')
    return render(request,'changecanteen.html',locals())

def singalData(request):
    foods = Food.objects.all()
    salefoods = SaleFood.objects.all()
    b = []  # 菜品名字
    s = []  # 菜品产量
    '''
    统计销量时，使用一个状态码来进行标记这个销量是否已经被记录，
    所以开始设计成false后来再设计成true，如果是true说明已经被改变
    '''
    break_tag = False
    for food in foods:
        for bname in b:
            if bname == food.name:
                index = b.index(bname)
                print(index)  # 6
                sfood = SaleFood.objects.filter(foodsale=food.nid).first()
                if sfood:
                    snumber = sfood.snumber
                else:
                    snumber = 0
                print(s[index])  # 7
                print(sfood)
                s[index] += snumber
                break_tag = True
        if break_tag == False:
            b.append(food.name)
            sfood = SaleFood.objects.filter(foodsale=food.nid).first()
            if sfood:
                s.append(sfood.snumber)
            else:
                s.append(0)
                # 只用b就可以了，b是名字
    return render(request,'choosefoods.html',locals())

def showSigalData(request,foodname):
    #通过名字找餐厅
    foods = Food.objects.filter(name=foodname)
    print(foods)
    #1.先找到菜品的id
    #名字
    rname = []
    rnum  = []

    for food in foods:
        foodId = food.nid
        #print(foodId)
    #2.通过菜品找到餐厅的
        canteenId = food.canteen_id
        canteen = Canteen.objects.filter(nid=canteenId).first()
        #将同一个菜的不同店的销量进行展示
        #1名字,餐厅的名字
        rname.append(canteen.name)
        #2销量，每个餐厅的这个菜品的名字
        salefood = SaleFood.objects.filter(foodsale_id=foodId).first()
        print(salefood)
        #找出餐厅里面的菜品的销售产量。
        rnum.append(salefood.snumber)
    print(rname,rnum)
    return render(request,'showsingaldata.html',locals())