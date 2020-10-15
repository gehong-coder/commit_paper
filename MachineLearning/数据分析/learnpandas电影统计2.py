import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager
#字体
my_font=font_manager.FontProperties(fname="")
#统计每个种类型的电影的个数有多少action，scary；；；
file_path="./IMDB-Movie-Data.csv"
df= pd.read_csv(file_path)
print(df.info())
print(df.head(1))
df_genre= df["Genre"]
print(df_genre)
#输出后发现数据之间是通过，隔开的所以通过split切开
temp_list = df_genre.str.split(",").tolist()#注意切开之后，这个是[[],[]]多个列表嵌套的所以使用set进行统计
#将所有题材的类型的电影进行放到一个列表里
genre_list= list(set([i for j in temp_list for i in j]))

#统计时，使用一个全0的数组进行统计
zero_df = pd.DataFrame(np.zeros((df.shape[0],len(genre_list))),columns=genre_list)
#                               行索引actor       列索引（电影）
#zero_df = pd.DataFrame(np.zeros((df.shape[0],len(genre_list))),columns=genre_list
print(zero_df)
#统计
for i in range(df.shape[0]):#某行电影数据
    zero_df.loc[i,temp_list[i]]=1#第几行第几列的数据为

print(zero_df)
#将每个电影数据的出现的地方均已标记为1
#按照行进行统计王上打0
count = zero_df.sum(axis=0)
print(count)
#将数据进行排序
count= count.sort_values()
_x = count.index
_y = count.values

#画图：使用条形图，因为数据与数据之间是没有关系的
plt.figure(figsize=(20,8),dpi=80)
plt.bar(range(len(_x)),_y)

plt.xticks(range(len(_x)),_x)
plt.show()