import numpy as np

us_path="us"

t1=np.loadtxt(us_path,delimiter=",",dtype="int")
t2=np.loadtxt(us_path,delimiter=",",dtype="int",unpack=True)#看清晰，转置unpack
#每一行，是一个人的信息，将一行信息进行

print(t1)
print(t2)

t3= np.arange(24).reshape(4,6)
print(t3)
t4=t3.transpose()#对所创建的数据进行转置
t5=t4.T#同样是转置
print(t4)
print(t5)

'''unpack，transpose T 转置分析'''