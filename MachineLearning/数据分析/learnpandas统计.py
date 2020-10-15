import pandas as pd
import numpy as np

file_path="./IMDB-Movie-Data.csv"
df= pd.read_csv(file_path)
print(df["Actors"])#有逗号-不能使用unique
print(df["Director"])#没有逗号-unique
print(df.info())
''' 10  Revenue (Millions)  872 non-null    float64
 11  Metascore           936 non-null    float64有缺失'''
print(df["Rating"].head(1))
#f分数
#获取电影的平均评分-rating的平均分
df_mean = df["Rating"].mean()
print(df_mean)
#将老师转换为列表
df_director = len(set(df["Director"].tolist()))
df_director2 = len(df["Director"].unique())#使用unique时，直接变成列表，直接len即可。
print(df_director)
print(df_director2)

#演员之间有逗号隔开
temp_df_actors_list = df["Actors"].str.split(",").tolist()#演员之间是使用，隔开的
df_actors_list = [i for j in temp_df_actors_list for i in j]
#（2）

actors_num = len(set(df_actors_list))
print(actors_num)
