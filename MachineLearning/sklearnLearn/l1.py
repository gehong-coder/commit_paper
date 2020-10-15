from sklearn import tree
from sklearn.datasets import load_wine
#分训练集和测试集
from sklearn.model_selection import train_test_split#随机划分数据
#名字的设置注意
import pandas as pd
#树模型
import graphviz
#使用matplotlib进行话图
from matplotlib import pyplot as plt


wine = load_wine()
print(wine)
print(wine.feature_names)#特征的名字
print(wine.target_names)#标签的名字
print("*"*100)
print(wine.target)
#将数据纵向连接
data_1 = pd.concat([pd.DataFrame(wine.data),pd.DataFrame(wine.target)],axis=1)
print(data_1)
'''
4    13.24  2.59  2.87  21.0  118.0  2.80  ...  1.82   4.32  1.04  2.93   735.0   0
..     ...   ...   ...   ...    ...   ...  ...   ...    ...   ...   ...     ...  ..
173  13.71  5.65  2.45  20.5   95.0  1.68  ...  1.06   7.70  0.64  1.74   740.0   2
特征+标签确定
'''
#将数据进行分类
X_train,X_test,Y_train,Y_test = train_test_split(wine.data,wine.target,test_size=0.3)
print(X_test.shape,X_train.shape,Y_test.shape,Y_train.shape)

#建模--分类树
test = []
for i in range(10):
    clf = tree.DecisionTreeClassifier( max_depth=i+1
                                      ,criterion='entropy'
                                      ,random_state=30
                                      #随机分支里面的参数，高维数据比较明显
                                      #,splitter="random"
                                      #防止过拟合
                                      #,max_depth=3#为列防止过拟合，则采用为了控制最大深度的方法1
                                      #,min_samples_leaf=10#当叶子的分割结点小于10 不分割
                                      #,min_impurity_split=60#当分割结点的总数小于60的时候部分--使得决策树变小
                                    )#信息墒的纯度选择的是entropy

    #训练模型
    clf = clf.fit(X_train,Y_train)
    #评估模型
    score = clf.score(X_test, Y_test)
    test.append(score)

plt.plot(range(1,11),test,color="red",label="max_depth")#学习曲线的确定-使用曲线进行确定
plt.legend()
plt.show()


score1 = clf.score(X_train,Y_train)
print(score1)#1.0
print(score)
feature_name = ['酒精','苹果酸','灰','灰的碱性','镁','总酚','类黄酮','非黄莞类酚类','花青素','颜色强度','色调','od280/od315稀释葡萄酒','脯氨酸']


'''#化成一棵树'''
dot_data = tree.export_graphviz(
    clf
    ,feature_names=feature_name#特征名
    ,class_names=["琴酒","雪梨","贝尔摩德"]
    ,filled=True#图表显示的颜色
    ,rounded=True#圆的形状
)

graph = graphviz.Source(dot_data)
graph.render('./iris')

#对于决策树的使用是，特征会排序
print(clf.feature_importances_)
'''
[0.         0.         0.         0.         0.02062511 0.
 0.43731963 0.01423504 0.         0.21077385 0.         0.
 0.31704638]
'''
print(
    [*zip(feature_name,clf.feature_importances_)]#特征的重要的性
)

'''因为测试集的准确度已经到达类1.O,所以已经出现了过拟合的现象，所以对于过拟合的现象的解决的方法是
树————剪枝
1。限制树的高度-3
2。分出结点必须要包含至少min_samples_split个结点，才会发生分支，否则不会发横分支界定
怎么确定值-使用超参数的值的曲线进行分子确定值

'''
clf_app = clf.apply(X_test)
clf_appy = clf.predict(X_test)
print(clf_app)
print(clf_appy)
