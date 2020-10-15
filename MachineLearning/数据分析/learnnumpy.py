from random import random

import numpy as np

#使用numpy进行实用
t1 = np.array([1,2,3,])

print(t1)
print(type(t1))#numpy的数组类型

t2=np.array(range(1,6))
print(type(t2))

t3=np.arange(4,10,2)#10是娶不到的

print(t3)

print(t3.dtype)#所装入数据的类型。

t4=np.array(range(1,4),dtype=int)
print(t4)
print(t4.dtype)

#修改数据类型
t4=t4.astype("float")
print(t4.dtype)

