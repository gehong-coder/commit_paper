#是一个多分类的问题，概率之和为1，，在多分类中，所使用的为标题【-有两个交叉墒函数可以使用。
#使用fashionminst来使用
import pandas as pd
import numpy as np
import tensorflow as tf
from matplotlib import pyplot as plt

#读取数据集--使用。load
(train_image,train_label),(test_image,test_label)=tf.keras.datasets.fashion_mnist.load_data()
print(test_label)#[9 2 1 ... 8 1 5]用数字进行编码
print(train_image.shape)#三个维度代表有三个特征
print(test_image.shape,test_label.shape)#测试数据的特征以及测试数据的标签
#print(train_image[0])
plt.imshow(train_image[0])
plt.show()# 鞋子的图片
print(train_image[0])#

#数据进行归一化
train_image = train_image/255
test_image = test_image/255
#(60000, 28, 28)，图片共有60000，每一张的大小为28*28
#建立模型
model = tf.keras.Sequential()
#添加层数,层数要先将进行扁平化的数据
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))#隐藏层之间的关系
#输入层之间的第一层
model.add(tf.keras.layers.Dense(128,activation='relu'))
model.add(tf.keras.layers.Dense(10,activation='softmax'))#变成一个概率值，10个概率，进行

#编译
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',#当标签是使用的数字进行编码的时候使用sparse——category进行
    #当label使用的是度热编码的时候使用的是categoric作为目标函数
    metrics=['acc']
)
#训练
model_sum = model.fit(train_image,train_label,epochs=5)
print(model_sum)
'''
Epoch 1/5
1875/1875 [==============================] - 3s 1ms/step - loss: 0.4943 - acc: 0.8258
Epoch 2/5
1875/1875 [==============================] - 3s 1ms/step - loss: 0.3739 - acc: 0.8663
Epoch 3/5
1875/1875 [==============================] - 3s 1ms/step - loss: 0.3390 - acc: 0.8767
Epoch 4/5
1875/1875 [==============================] - 3s 1ms/step - loss: 0.3130 - acc: 0.8865
Epoch 5/5
1875/1875 [==============================] - 3s 1ms/step - loss: 0.2965 - acc: 0.8909
'''

#评价模型--
model_t = model.evaluate(test_image,test_label)
print(model_t)
'''
313/313 [==============================] - 0s 1ms/step - loss: 0.3460 - acc: 0.8769
[0.3460359573364258, 0.8769000172615051]
'''

#独热编码的使用：【1，0，0】
            #【0，1，0】
#将编码进行转换,使用文本进行转换的时候。
train_label_du = tf.keras.utils.to_categorical(train_label)
test_label_du = tf.keras.utils.to_categorical(test_label)
print(train_label_du)