#是一个多分类的问题，概率之和为1，，在多分类中，所使用的为标题【-有两个交叉墒函数可以使用。
#使用fashionminst来使用
import pandas as pd
import numpy as np
import tensorflow as tf
from matplotlib import pyplot as plt

#读取数据集--使用。load
(train_image,train_label),(test_image,test_label)=tf.keras.datasets.fashion_mnist.load_data()

#数据进行归一化
train_image = train_image/255
test_image = test_image/255
#(60000, 28, 28)，图片共有60000，每一张的大小为28*28
'''独热化数据'''
#独热编码的使用：【1，0，0】
            #【0，1，0】
#将编码进行转换,使用文本进行转换的时候。
train_label_du = tf.keras.utils.to_categorical(train_label)
test_label_du = tf.keras.utils.to_categorical(test_label)
print(train_label_du)
'''
[[0. 0. 0. ... 0. 0. 1.]
 [1. 0. 0. ... 0. 0. 0.]
 [1. 0. 0. ... 0. 0. 0.]
 ...
 [0. 0. 0. ... 0. 0. 0.]
 [1. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]]'''

#建立模型
model = tf.keras.Sequential()
#添加层数,层数要先将进行扁平化的数据
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))#隐藏层之间的关系
#输入层之间的第一层
model.add(tf.keras.layers.Dense(128,activation='relu'))
model.add(tf.keras.layers.Dense(10,activation='softmax'))#变成一个概率值，10个概率，进行

#编译
model.compile(
    #有两种方式选择优化算法
    #optimizer='adam',
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
    loss='categorical_crossentropy',
    #当标签是使用的数字进行编码的时候使用sparse——category进行
    #当label使用的是度热编码的时候使用的是categoric作为目标函数
    metrics=['acc']
)
#训练
model_sum = model.fit(train_image,train_label_du,epochs=5)
print(model_sum)
'''
Epoch 1/5
1875/1875 [==============================] - 3s 1ms/step - loss: 0.4982 - acc: 0.8254
Epoch 2/5
1875/1875 [==============================] - 3s 2ms/step - loss: 0.3762 - acc: 0.8642
Epoch 3/5
1875/1875 [==============================] - 3s 1ms/step - loss: 0.3390 - acc: 0.8760
Epoch 4/5
1875/1875 [==============================] - 3s 2ms/step - loss: 0.3134 - acc: 0.8853
Epoch 5/5
1875/1875 [==============================] - 3s 1ms/step - loss: 0.2970 - acc: 0.8902
'''

#评价模型--
model_t = model.evaluate(test_image,test_label_du)
print(model_t)
print(model_t)
'''
313/313 [==============================] - 0s 1ms/step - loss: 0.3460 - acc: 0.8769
[0.3460359573364258, 0.8769000172615051]
'''
#预测
model_pre = model.predict(test_image)
print(model_pre)
print(model_pre[0])
print(np.argmax(model_pre[0]))
print(test_label[0])

'''
多层感知器
如果是连续的：无需激活函数
如果是二分类问题：sigmiod
如果是多分类问题:relu

正确的学习速率的是比较稳定，并且逐步下降-越小越好
反向传播算法的使用--梯度下降法的使用 

优化器：可以进行速率的调试
sgd
rmprop
rnn
adam-鲁棒不敏感-自适应优化--lr

网络容量的意思：
神经单元数越多，超参数越多，层数越多，神经网络的拟合能力非常厉害
容易过拟合
网络容量变大--神经元的个数
1。增加层数-深度--网络越来越多
2。增加隐藏神经单元数-神经元数不能太小，容易丢弃信息
--但是同时训练参数也会非常的慢，由于慢

过拟合的使用：

'''