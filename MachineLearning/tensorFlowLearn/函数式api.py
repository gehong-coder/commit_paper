import tensorflow as tf
from tensorflow import keras
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#导入数据
fashion_mnist = keras.datasets.fashion_mnist
(train_images,train_label),(test_images,test_label) = fashion_mnist.load_data()
#归一化数据
train_images = train_images/255.0
test_images = test_images/255.0

#模型的书写-建立模型
input1 = keras.Input(shape=(28,28))
input2 = keras.Input(shape=(28,28))
x1 = keras.layers.Flatten()(input1)#将上面的二维数据进行低纬度转换
x2 = keras.layers.Flatten()(input2)
x = keras.layers.concatenate([x1,x2])
x = keras.layers.Dense(32,activation='relu')(x)#将上面的单元数进行实例化
x = keras.layers.Dropout(0.5)(x)#防止过拟合
x = keras.layers.Dense(64,activation='relu')(x)
output = keras.layers.Dense(10,activation='sigmoid')(x)#每一层之间进行迭代进行使用
model = keras.Model(inputs=[input1,input2], outputs=output)

model = keras.Model(inputs=input,outputs=output)
model_sum = model.summary()
print(model_sum)

'''
函数式的使用是一层一层之间进行调用的
Model: "model"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
input_1 (InputLayer)         [(None, 28, 28)]          0         
_________________________________________________________________
flatten (Flatten)            (None, 784)               0         
_________________________________________________________________
dense (Dense)                (None, 32)                25120     
_________________________________________________________________
dropout (Dropout)            (None, 32)                0         
_________________________________________________________________
dense_1 (Dense)              (None, 64)                2112      
_________________________________________________________________
dense_2 (Dense)              (None, 10)                650       
=================================================================
'''
