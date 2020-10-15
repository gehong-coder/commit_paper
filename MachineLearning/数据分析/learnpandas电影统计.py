import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager
#字体
my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

#杜读数据
file_path = "./IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)
print(df.info())

#对数据进行查看，进行查看rating，runtime(评分和时间)分布情况，选择一种图形-直方图
#准备数据

runtime_data = df["Runtime (Minutes)"].values#series-变成一个数组[]
print(runtime_data)
max_runtime = max(runtime_data)
min_runtime = min(runtime_data)
print(max_runtime,min_runtime)
#直方图要进行分组
#组数
#numbers = (max_runtime-min_runtime)//5#10分钟作为组距
numbers_list = [0.5,1.6]
i = 1.6
while(i<max_runtime):
    i+=0.5
    numbers_list.append(i)

print(max_runtime-min_runtime)
'''数据和组数都已经存在接下来进行画图'''

plt.figure(figsize=(20,8),dpi=80)
plt.hist(runtime_data,numbers_list)


#将数据变成以间距为0.5开始


#此时的x已经是一个完整的列表

#替换坐标
plt.xticks(numbers_list)#开始，结束，艰巨
plt.show()
