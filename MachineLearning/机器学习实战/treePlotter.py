import matplotlib.pyplot as plt
#定义文本框和箭头格式
decisionNode = dict(boxstyle = "sawtooth" ,fc ="0.8")
leafNode = dict(boxstyle = "round4",fc= "0.8")
arrow_args = dict(arrowstyle = "<-")
#定义带箭头的注解
def plotNode(nodeTxt,centerPt,parentPt,nodeType):
    createPlot.ax1.annotate(nodeTxt,xy = parentPt, xycoords = "axes fraction",
                            xytext = centerPt,textcoords ='axes fraction',
                           va = "center",ha = "center",bbox = nodeType,arrowprops = arrow_args)
#定义画图
def createPlot():
    fig = plt.figure(1,facecolor='white')#画板
    fig.clf()#
    createPlot.ax1 = plt.subplot(111, frameon=False)#在这个画板上面画图
    plotNode(U"决策节点",(0.5,0.1),(0.1,0.5),decisionNode)#有决策节点
    plotNode(U"叶节点",(0.8,0.1),(0.3,0.8),leafNode)#有叶节点。
    plt.show()#画图