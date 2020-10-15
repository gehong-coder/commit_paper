#numpy能够帮助我们处理数值，但是pandas除了处理数值之外(基于numpy)，还能够帮助我们处理其他类型的数据
#series一维数据
#datafame二维数据
import pandas as pd
t=pd.Series([1,2,3,58])
print(type(t))
print(t)
'''
<class 'pandas.core.series.Series'>
0     1
1     2
2     3
3    58
索引类型的数据 前面是索引
'''
t2=pd.Series([1,53,5,6],list("adcd"))
print(t2)
'''
dtype: int64
a     1
d    53
c     5
d     6
可以指定索引的类型，可以是数字，也可以是字符串
'''
#字典创建
temp_dict={"name":"gehong","age":49,"tel":88888}
t5=pd.Series(temp_dict)
print(t5)
'''
name    gehong
age         49
tel      88888
dtype: object可以使用字典类型的方式进行使用 '''

#可以通过索引找值
print(t5["age"])
print(t5["tel"])
print(t5["name"])
print(t5[0])
'''可以通过索引也可以通过0，1，2进行寻找'''
print(t5[0:,])
'''
88888
gehong
gehong多列数据
'''
print(t5[["age","name"]])#取多行数据，加两个方括号即可

for i in t5.index:
    print(i)
    print(type(i))
    '''name
    <class 'str'>
    age
    <class 'str'>
    tel
    <class 'str'>索引可以使用循环进行查找'''

print(len(t5.index))#3
print(t5.values)
print(type(t5.values))
'''
['gehong' 49 88888]
<class 'numpy.ndarray'>
'''