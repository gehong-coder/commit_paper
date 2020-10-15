import tensorflow as tf
import pandas as pd
import numpy as np
from  matplotlib import pyplot as plt
from   matplotlib  import font_manager
#字体
my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc:")
print(format((tf.__version__)))
#深度学习的基础
'''读取数据集'''
file_path = "./ml.csv"
data = pd.read_csv(file_path)
print(data)
print(data.info())
'''#1.首先查看数据之间的关系，发现数据的教育成都与收入的关系是线性的关系'''
plt.scatter(data.Education,data.Income)
#求出线性关系F（x）=ax+b--求解a和b
plt.show()

#要求解a和b使得-最好的a和b那就使用目标函数-也就是损失函数--最小二乘拟合--均方差
#合适的a和b进行让均方差越小越好
#--使用梯度下降的算法进行计算
'''建立模型'''
x = data.Education
y = data.Income
'''1.顺序模型，搭建顺序-一层一层搭建'''
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(1,input_shape=(1,)))#顺序模型的输出和输入的层数的决定
#                          输出维度：1 输入维度：1
print(model.summary())
'''
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense (Dense)                (None, 1)                 2         #dense层的用处就是初始化我们的变量，进行输入，售出
=================================================================
Total params: 2
Trainable params: 2
Non-trainable params: 0
_________________________________________________________________
None
'''
'''2.编译模型-配置-计算最好的参数值-使用的优化算法是梯度下降算法'''
model.compile(
    #'''优化算法'''
    optimizer= 'adam',#自适应优化算法--随机初始化的位置是不确定的所以每次的loss都是不同的
    #'''目标函数'''-均方差
    loss = 'mse'
)

'''3训练模型'''
history = model.fit(x,y,epochs=5000)#训练的过程是一个循环的过程
print(history)
'''
Epoch 4999/5000
1/1 [==============================] - 0s 246us/step - loss: 134.2630
Epoch 5000/5000
1/1 [==============================] - 0s 237us/step - loss: 134.2184
'''
#到达第5000次的时候loss到达了134-

'''4.使用模型'''
x_predict = model.predict(x)
print(x_predict)

x_p =  model.predict(pd.Series([20]))
print(x_p)