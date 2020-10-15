from numpy import *
import operator
#创建数据
def createDateSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels
group,labels = createDateSet()
#k算法
def classify0(inX,dataSet,labels,k):

    #计算一直类别点与当前点的距离
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX,(dataSetSize,1))-dataSet
    sqDiffMat = diffMat**2#(xA0-XB0)^2
    sqDistances = sqDiffMat.sum(axis=1)#将一行数据里面的都求和
    distance = sqDistances ** 0.5#距离开根号
    # ile函数位于python模块 numpy.lib.shape_base中，
    # 他的功能是重复某个数组。比如tile(A,n)，功能是将数组A重复n次，
    # 构成一个新的数组，我们还是使用具体的例子来说明问题

    #将距离进行排序-一个x进来之后，与当前选中的点进行了距离的操作-
    sortedDistances = distance.argsort()
    classcount = {}

    #进行排序-选取k个点-分别进行
    for i in range(k):
        votelabel = labels[sortedDistances[i]]
        classcount[votelabel] = classcount.get(votelabel,0) +1

    sortedClasscount = sorted(classcount.items(),
                              key=operator.itemgetter(1),#排序逆序
                              reverse=True)
    return sortedClasscount[0][0]
#返回k个点中出现频率最高的类别作为当前点的预测分类
label = classify0([0,0],group,labels,3)
print(label)
#将数据的txt格式进行转换格式

def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOflines = len(arrayOLines)#一共多少行
    returnMat = zeros((numberOflines,3))#创建一个行为numberoflines行和3列的矩阵-特征矩阵
    classLabelVector = []#标签矩阵
    index =0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]#特征数据
        classLabelVector.append(int(listFromLine[-1]))#标签
        index = index+1
    return returnMat,classLabelVector
dataDataMat,datingLabels = file2matrix('datingTestSet.txt')
print(dataDataMat,datingLabels)

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(dataDataMat[:,1],dataDataMat[:,2])
plt.show()




