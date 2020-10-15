import pandas as pd
import numpy as np

t1=pd.DataFrame(np.arange(12).reshape(3,4))
print(t1)
'''
   0  1   2   3 columns索引axis=1纵向
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
index索引（行）axis=0
在dataframe中，既有行索引，又有列索引
就讲矩阵的形式展现出来
因为series是多个组成了dataframe

'''

d1={"name":["xiaoming","ghhg"],"age":[44,55],"tel":[11111,22222]}#一个字典使用列表
d3=[{"name":"ghh","age":88},{"name":"hhh","tel":000},{"name":"kk","age":888,"tel":0000}]
d2=pd.DataFrame(d1)
d4=pd.DataFrame(d3)

print(d1)
print(d2)#成为了索引，和数据多个横键和多个竖键
print(d3)
print(d4)
'''

  name    age  tel
0  ghh   88.0  NaN
1  hhh    NaN  0.0
2   kk  888.0  0.0
没有的地使用nan进行替代。
'''
print(t1.index)
print(t1.columns)
print(t1.ndim)#2
print(t1.head(1))#   0  1  2  3
                #  0  0  1  2  3
print(t1.tail(1))#展示尾部数据
print(t1.info())
print(t1.describe())
'''
RangeIndex(start=0, stop=3, step=1)
RangeIndex(start=0, stop=4, step=1)
区间发生改列
info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   0       3 non-null      int64
 1   1       3 non-null      int64
 2   2       3 non-null      int64
 3   3       3 non-null      int64
dtypes: int64(4)
memory usage: 224.0 bytes
所有的信息均可展示

#describe:
         0    1     2     3
count  3.0  3.0   3.0   3.0
mean   4.0  5.0   6.0   7.0
std    4.0  4.0   4.0   4.0
min    0.0  1.0   2.0   3.0
25%    2.0  3.0   4.0   5.0
50%    4.0  5.0   6.0   7.0
75%    6.0  7.0   8.0   9.0
max    8.0  9.0  10.0  11.0
统计数据数字列的数据均值，属性，

'''