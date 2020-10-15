import pandas as pd
import numpy as np

df=pd.read_csv("./dogNames.csv")
print(df[(df["Count_AnimalName"]>800)&(df["Count_AnimalName"]<1000)])
print(df[(df["Count_AnimalName"]>800)&(df["Count_AnimalName"]<10000)])
#print(df["info"].str.split("/").tolist())#将信息进行切割，在转换成字符列表。
#关于缺失值的树立nan，0
'''
1》首先判断数据是否含有nan
'''
s1=pd.DataFrame(np.arange(12).reshape(3,4),index=list("abc"),columns=list("wxyz"))
d3=[{"name":"ghh","age":88},{"name":"hhh","tel":000},{"name":"kk","age":888,"tel":0000}]
d3=pd.DataFrame(d3)
print(d3)
t5=pd.isnull(d3)
print(t5)#boolean值
print(d3[pd.notnull(d3["name"])])

t7=d3.dropna(axis=0)#默认的how是nan是any是代表着只要有一个就是

print(t7)#只有最后一行没有nan所以不删除
t8=d3.dropna(axis=0,how="all")#只有全部都为nan才删除这一行
print(t8)
#将数据进行填充。
print(d3.fillna(99))#--
print(d3.fillna(d3.mean()))
d3["age"]= d3["age"].fillna(d3["age"].std())
print(d3)
'''
  name         age  tel
0  ghh   88.000000  NaN
1  hhh  565.685425  0.0
2   kk  888.000000  0.0
只让age进行替换-缺失值。

'''


###当数据中出现列0时，先处理成nan，在进行赋值--直接进行menan

