import pandas as pd
import numpy as np

df = pd.DataFrame({'a':range(7),'b':range(7,0,-1),'c':["one","two","uuu","iii","mmm","ppp","ooo"],'d':list("jjjklsq")})
print(df)
b = df.set_index(["c","d"])#双索引
c = b["a"]
print(b)
print("8"*100)
print(c)
print(type(c))
print(c["one"]["j"])

print(c["one"])
#交换索引
d = df.set_index(["d","c"])["a"]
print(d)
print(d.index)
d=d.swaplevel()["one"]
print(d.index)