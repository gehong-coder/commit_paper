#逻辑回归是分类的模型，二分类比较常用-，0，1
#使用sigmoid值进行分类-映射分类（0，1）看成概率值，进行一个输出
'''说明，神经网络就是一个映射网络，'''
#损失函数的选择是--分类模型使用--交叉墒-有效-输出，放大两种分布之间的损失。，损失越小越好
'''使用tensorflow里面使用binary——crossentropy进行交叉墒的使用'''
import tensorflow as tf
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

file_path = "./credit-a.csv"
data = pd.read_csv(file_path,header=None)

#读数据
print(data.head())
print(data.info())
#1读取数据发现没有表头，需要补充表头,None
'''
   0      1      2   3   4   5   6     7   8   9   10  11  12   13     14  15
0   0  30.83  0.000   0   0   9   0  1.25   0   0   1   1   0  202    0.0  -1
1   1  58.67  4.460   0   0   8   1  3.04   0   0   6   1   0   43  560.0  -1
2   1  24.50  0.500   0   0   8   1  1.50   0   1   0   1   0  280  824.0  -1
前0-14列是特征，第15行是分类
'''
#进行分类汇总
data_count = data.iloc[:,-1].value_counts()
'''value_counts()是一种查看表格某列中有多少个不同值的快捷方法，并计算每个不同值有在该列中有多少重复值。
value_counts()是Series拥有的方法，一般在DataFrame中使用时，需要指定对哪一列或行使用'''
print(data_count)

#判断给列特征之后，是否会产生欺诈行为，提取x数据和y数据
x = data.iloc[:, :-1]#代表了0-14列的数据
y = data.iloc[:,-1].replace(-1,0)#代表了标签

#建立模型
model = tf.keras.Sequential()
#添加层数
#第一层
model.add(
    tf.keras.layers.Dense(4,input_shape=(15,),activation='relu')#隐藏层的第一层
)
#参数：15*4+4=64
#第二层
model.add(
    tf.keras.layers.Dense(4,activation='relu')#隐藏层的第二层
)
#参数：4*4+4=20
#输出层
model.add(tf.keras.layers.Dense(1,activation='sigmoid'))
#参数 4+1=5
model_summ = model.summary()
print(model_summ)
'''
Total params: 89
Trainable params: 89
Non-trainable params: 0
'''
#训练模型
model.compile(
    optimizer='adam',#优化算法
    loss='binary_crossentropy',#目标函数
    metrics=['acc']#测量数据  评价指标函数名称  混淆矩阵，等待
)
#训练
history = model.fit(x,y,epochs=100)
print(history)
#给这个数据的history进行绘图
hist = history.history.keys()
print(hist)
#将数据的展现
plt.plot(history.epoch,history.history.get("loss"))
plt.show()
#
plt.plot(history.epoch,history.history.get("acc"))
#
plt.show()
#loss逐渐下降