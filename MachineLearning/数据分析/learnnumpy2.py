#关于数组的位数

import  numpy as np

t1=np.array([12,3,4,45])
print(t1.shape)#一维度，因为shape中只有一个数字，相当于一个向量

t2=np.array([[12,3],[12,4]])
print(t2)
print(t2.shape)#有两行，相当于一个矩阵

t3=np.array([
    [[1,2,4],[1,5,6]],
    [[4,56,8],[6,88,3]]
])
print(t3)
print(t3.shape)#三维的数组(2, 2, 3)--块，行，列

t4=np.arange(24).reshape(2,3,4)
print(t4)

t4=t4.flatten()
print(t4)#降维度使用flatten进行使用。
t4=t4+2#所有的值全部都加2。
print(t4)
print(t4)
###两个数组相加时，或相乘时对应位置相加，相见，相乘
#就算不同行不同位置也会就对应位置进行计算，同行，同列
#如果对应位置都不同的时候，对应
