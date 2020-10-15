import pandas as pd
import numpy as np

'''数据的合并--行索引'''
df1 = pd.DataFrame(np.ones((2,4)),index=["A","B"],columns=list("abcd"))
print(df1)#数据是二维的所以注意np.ones是（（））
df2 = pd.DataFrame(np.zeros((3,3)),index=["A","B","C"],columns=list("xyz"))
print(df2)
df3 = df1.join(df2)#  以df1为准则
df4 = df2.join(df1)#  以df2为准则，没有的用nan代替
print(df3)
print(df4)
'''数据饿的合并--列索引'''

df5 = pd.DataFrame(np.arange(9).reshape(3,3),columns=list("fax"))
print(df5)
df6 = df1.merge(df5,on="a")
print(df6)#只要df5中的某行与df1中的某行相同则进行匹配，则进行连接
df7 = df5.merge(df1,on="a")
print(df7)
#内链接
df8 = df1.merge(df5,on="a",how="outer")#全联接以后，去掉重复的部分
print(df8)
df9 = df1.merge(df5,on="a",how="left")
print(df9)#以左边为准则
df210 = df1.merge(df5,on="a",how="right")
print(df5)
print(df210)
#统计例子
file_path = "./starbucks_store_worldwide.csv"
dff1 = pd.read_csv(file_path)
print(dff1.head(1))
print(dff1.info())
#统计美国的信息与美国的进行分组

pd_grouped = dff1.groupby("Country")
print(pd_grouped)

'''for i,j in pd_grouped:
    print(i)
    print("_"*100)
    print(j,type(j))
    print("*"*100)'''
#按照国家进行统计
pd_grouped_count = pd_grouped["Brand"].count()#统计个位数
print(pd_grouped_count)
print(pd_grouped_count["US"])#数量
print(pd_grouped_count["CN"])#数量

#按照中国的省份进行统计
china_data = dff1[dff1["Country"] == "CN"]### 看清楚这个地方是
china_data_grouped = china_data.groupby(by="State/Province").count()["Brand"]
grouped_cn = dff1["Brand"].groupby(by=[dff1["Country"],dff1["State/Province"]]).count()#按照两个进行分组后的结果，所以有两个列
print(grouped_cn)
print(china_data_grouped)
group2 = dff1.groupby(by=[dff1["Country"],dff1["State/Province"]])[["Brand"]].count()
print(group2)
