from matplotlib import pyplot as plt
import pandas as pd

file_path = "./books.csv"
df = pd.read_csv(file_path)
print(df.head(2))
print(df.info())
#判断是否有缺失，删除有缺失的数据，取出年份未缺失的数据
data1 = df[df.notnull(df["original_publication_year"])]
grouped = data1.groupby(by="original_publication_year ").count()["title"]

#不同年份的评分
data2 = df