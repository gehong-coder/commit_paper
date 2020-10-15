#多层感知器--使用激活函数
# 1-relu(最常用的不会导致梯度消失)
# -2-sigmoid(-导致梯度消失)
# -tanh映射（-1 +1）

import tensorflow as tf
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager
#广高的宣传力度与销量问题
file_path = "./Advertising.csv"
data = pd.read_csv(file_path)
print(data.info())
print(data.head())
#绘图看看
plt.scatter(data.radio,data.sales)
#绘制散点图展示关系-线性关系
plt.show()
plt.scatter(data.newspaper,data.sales)
plt.show()

#有三个特征，建立模型-预测销量-
#准备数据
x = data.iloc[:,1:-1]
y = data.iloc[:,-1]

#建立模型-顺序模型
model = tf.keras.Sequential(
    #中间层（神经元个数，特征，激活函数，）
    [tf.keras.layers.Dense(10,input_shape=(3,),activation='relu'),
    #10个神经元，3个特征-w的参数共有30个再加上10个bias--共有40个变量
     tf.keras.layers.Dense(1)]
    #10个神经元—+1个偏置
    #层数,dense的第一个维度为输出维度（隐含层），以及输出的shape.并且对于每一层的数据要进行激活，
    # dense的第二个维度是（）为输出成
)
print(model.summary())
'''
     Layer (type)                 Output Shape              Param #   
=================================================================
dense (Dense)                (None, 10)                40        
_________________________________________________________________
dense_1 (Dense)              (None, 1)                 11        
================================================================='''

#训练模型
model.compile(
    #优化函数
    optimizer = 'adam',
    #目标函数
    loss = 'mse'
)

mode_f = model.fit(x,y,epochs=100)
print(mode_f)

#预测模型
test = data.iloc[:10,1:-1]
x_pre = model.predict(test)
print(x_pre)
test1 = data.iloc[:10,-1]
print(test1)

'''
1.绘图
2. 展示数据
3  模型选择（神经元数，层数，输出个数）
4  训练模型
5  使用模型

'''