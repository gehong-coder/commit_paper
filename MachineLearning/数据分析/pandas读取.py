#pandas读取csv文件
import pandas as pd
import numpy as np

#定义路径
df=pd.read_csv("./dogNames.csv")
print(df)

#读取狗的名字，分析谁的名字出现的次数最高
print(df.head())
print(df.info())
print(df.describe())
#统计次数的话，那就使用排序进行使用。
#排序的方法
df_paixu=df.sort_values(by="Count_AnimalName")
print(df_paixu)
print(df_paixu.tail(10))#可以
dfpaixu2=df.sort_values(by="Count_AnimalName",ascending=False)
print(dfpaixu2)
print(dfpaixu2.head(10))
#pandas的切片和索引
'''按照某一列进行排序'''
print(df[:20])
print(df["Row_Labels"][:20])#先取出属于rowlablels列的所有数据，在进行取出前20
print(type(df["Row_Labels"]))#编变成了一行一列的属性，所以变成了series

''''''
#数据的索引p---loc
t3= pd.DataFrame(np.arange(12).reshape(3,4),index=list("abc"),columns=list("wxyz"))
print(t3)
'''
   w  x   y   z
a  0  1   2   3
b  4  5   6   7
c  8  9  10  11
创建时直接指定列索引和杭苏音
'''
t5=t3.loc["a","z"]#进行定位数字
print(t5)
print(t3.loc["a",:])#取出a的整行进行操作
print(t3.loc[:,"w"])#取出a的一整列的操作
#去多行多列
print(t3.loc[["a","c"],:])#取出多行数据，使用【【
print(t3.loc[:,["w","z"]])#取出多列数据进行

print(t3.loc[["a","c"],["w","z"]])
#取出指定的数据进行展示。使用loc可以选中所选的数据

'''索引值----iloc'''

print(t3.iloc[1,:])
print(t3.iloc[:,[1,2]])
print(t3.iloc[[1,2],[2,1]])#说明是dataframe类型所以数据选中2*2=4
