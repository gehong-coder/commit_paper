#树脂拼接vstack
#水平分割hstack
import numpy as np
t5=np.eye(4)
print(t5)
print(np.argmax(t5,axis=0))#输出最大值所在的位置列方向
t5[t5==1]=-1
print(t5)
print(np.argmin(t5,axis=0))#输出最小值的位置
np.random.seed(10)

#inf --infinite 无限--是一个浮点类型
#两个inf

print(np.count_nonzero(t5))
#两个nan是不相等的
#np.nan!=np.nan
print(np.isnan(t5))
t6=np.arange(24).reshape(4,6)
print(t6)
np.sum(t6)
#全部的求和
print(np.sum(t6))
#这个是每一列上的元素进行求和，也就是在行上面求和
print(np.sum(t6,axis=0))#往上大跟行的形状相同
#这个是每一行进行求和，也就是列上面求和
print(np.sum(t6,axis=1))#往右大，跟列的形状相同
#一般来说如果其中有nan的话，要使用均值进行代替，防止数据出现欠你和的现象
#👎记住nan与任何值计算都是nan所以
t6=t6.astype("float")
print(t6.dtype)

print(t6.mean(axis=0))#每一列的平均值
print(t6.mean(axis=1))#每一行的平均值
print(t6.min(axis=0))#每一列的最小值
print(t6.min(axis=1))#没行
print(t6.std(axis=0))#每列上面的标准差
print(t6.std(axis=1))#每一行的上面的标准差-标准差越大，表示波动越大，不稳定