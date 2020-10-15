import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#读的数据
file_path = "./starbucks_store_worldwide.csv"
df = pd.read_csv(file_path)
print(df.head(1))
print(df.info())

#使用matplot展示前十的国家
data1 = df.groupby(by="Country").count()["Brand"].sort_values(ascending=False)[:10]# 取前十
#数据
_x = data1.index
_y = data1.values
plt.figure(figsize=(20,8),dpi=80)
plt.bar(range(len(_x)),_y)
plt.xticks(range(len(_x)),_x)
plt.show()