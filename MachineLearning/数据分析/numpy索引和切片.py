import numpy as np

us_path="./us"

t1=np.loadtxt(us_path,delimiter=",",dtype="int")

#取出某一行
print(t1)

print("*"*100)
print(t1[0])

print("*"*100)
print(t1[2:])

#取连续的多行时使用两个方括号进行使用
print("*"*100)
print(t1[[1,3,5]])#多个
#取列
print("*"*100)
'''前行后列'''
print(t1[:,0])#后面是列，前面行
print("*"*10)

#取连续的多列
print(t1[:,1:])

#取不连续的多列
print(t1[:,[0,2]])

#只要第2行
print(t1[1,:])

print("*"*10)
#从第四行开始就使用全部放上
print(t1[4:,:])

#取多行多列
a=t1[0,1]
print(a)
print(type(a))
#  取出多行多列
print(t1[0:2,0:2])#左闭右开

#取出多个不相邻的点
#【1，2，3】【3，4，5】--【1，3】【2，4】【3，5】
# 前面是行，后面是列
b=t1[[0,1,2],[0,1,1]]
print(b)

#numpy修改值时，🧵取出来在进行比较】
t2=t1<400#布尔索引
print(t2)

t1[t1<1000]=3#布尔类型的赋值
print(t1)
t5=np.where(t1<800,0,900)#三元运算符
print(t5)