from matplotlib import pyplot as plt
import pandas as pd
import  numpy as np
from matplotlib import font_manager

#字体
my_font = font_manager.FontProperties(fname="/System/Library/Fonts/SFNS.ttf")
#
file_path = "./starbucks_store_worldwide.csv"
df = pd.read_csv(file_path)

#数据
data = df[df["Country"] == "CN"]
#选好中国的数据进行按照数据分组
data1 = data.groupby(by="City").count()["Brand"].sort_values(ascending=False)[:15]
_x = data1.index
_y = data1.values

plt.figure(figsize=(20,8),dpi=80)

plt.bar(range(len(_x)),_y)
plt.xticks(range(len(_x)),_x)
plt.show()
