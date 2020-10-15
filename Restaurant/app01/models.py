from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

#厨师详情
class CookerDetail(models.Model):
    nid = models.AutoField(primary_key=True)
    birthday=models.DateField()
    telephone=models.BigIntegerField()
    addr=models.CharField( max_length=64)
#厨师
class Cooker(models.Model):
    nid = models.AutoField(primary_key=True)
    name=models.CharField( max_length=32)
    age=models.IntegerField()
    # 与AuthorDetail建立一对一的关系
    cookerDetail=models.OneToOneField(to="CookerDetail",on_delete=models.CASCADE)
    #创建关联表的时候，加上引号就可以是一个全局

#餐馆
class Canteen(models.Model):
    #food的nid
    nid = models.AutoField(primary_key=True)
    name=models.CharField( max_length=32)
    city=models.CharField( max_length=32)
    email=models.EmailField()
    def __str__(self):
        return self.name

'''一对多的关系的建立表关系，这个book表是多的那一方，'''
'''一对一关系的建立之坐着'''
class Food(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField( max_length=32)
    designDate=models.DateField()
    price=models.DecimalField(max_digits=5,decimal_places=2)
    # 与信息表建立一对多的关系,外键字段建立在多的一方-生成的字段
    canteen=models.ForeignKey(to="Canteen",to_field="nid",on_delete=models.CASCADE)
    # 与canteen表建立多对多的关系,ManyToManyField可以建在两个模型中的任意一个，自动创建第三张表
    cookers =models.ManyToManyField(to='Cooker',)#
    def __str__(self):
        return self.name
#借书表
class SaleFood(models.Model):
    sid =  models.AutoField(primary_key=True)
    snumber = models.IntegerField()
    # 与book建立一对一的关系,外键字段建立在多的一方-生成的字段
    foodsale = models.OneToOneField(to="Food",on_delete=models.CASCADE)