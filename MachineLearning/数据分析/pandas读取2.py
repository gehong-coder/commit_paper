from pymongo import MongoClient
import pandas as pd

#momng是外部传列数据库
client =MongoClient()
collection= client["douban"]["tv1"]
data= list(collection.find())
t1=data[0]
t1=pd.Series(t1)
print(t1)

#pandas可以现将数据读出来
