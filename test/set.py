'''set ：无序的，不重复的序列，
可以使用打括号{}'''
#建立
set_param={'1','2'}
print(set_param)
print(type(set_param))
#CRUD
print('1' in set_param)
#集合的交并补运算
a =set('ghgh')
b = set('ghhhk')
print(a | b)
print(a & b)

#集合里面放多个语言（（））
my_set = set(('hhh','ggg','yyy'))
print(my_set)
my_set.add('gehong')
print(my_set)
my_set.remove("ggg")#移除的时候是移除的元素要把元素给放进去
print(my_set)

print(len(my_set))

#clear清除所有元素
my_set.clear()#已经变空
#remove清除制定元素
print(my_set)

#字典dist:
'''可变的容器类型，可以放任何类型的数据 key=value'''
d={1:'1',2:'zhangsan'}
'''操作习惯为由键访问值，因为都是通过key找value'''
print(d)
keys= d.keys()
print(keys)
#可以单独访问
print(d[2])
for i in keys:
    print(i)
d.setdefault(3,'ggg')
print(d)
#更新 无则添加，有则更新
d[3]="kkl"
print(d)
#pop可以pop出任一个元素，中间的也可以
r=d.pop(2)
print(r)
print(d)
#关键字
del d[3]
print(d)