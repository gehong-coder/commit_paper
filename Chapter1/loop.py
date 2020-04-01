#循环
list1= [1,2,3]
for l in list1:
    print(l)
'''in后面是迭代条件'''
'''冒泡排序：一次冒一次'''

a=[3,77,1,99,8]
a=[3,77,1,99,8]
for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[i] > a[j+1]:
            a[i], a[j+1]=a[j+1],a[i]


print(a)