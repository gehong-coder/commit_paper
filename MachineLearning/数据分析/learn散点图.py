#散点图的绘制，使用的是plt.scatter

from matplotlib import pyplot as plt
from matplotlib import font_manager

#字体
my_font=font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

#数据--将图形分开
x_3=range(1,32)
x_10=range(51,82)

y_3=[11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y_10=[26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]
#设置图形大小
plt.figure(figsize=(20,8),dpi=80)

#描点--散点图的绘制
plt.scatter(x_3,y_3,label="3月分")
plt.scatter(x_10,y_10,label="10月份")

#调整x的刻度
_x=list(x_3)+list(x_10)
_xtick_label=["3月{}号".format(i) for i in x_3]
_xtick_label+=["10月{}号".format(i-50) for i in x_10]

#替换刻度,步长一定要相似，注意在：：3
plt.xticks(_x[::3],_xtick_label[::3],rotation=45,fontproperties=my_font)

#添加图片信息
plt.xlabel("月份",fontproperties=my_font)
plt.ylabel("y值",fontproperties=my_font)
plt.title("嫉妒销售",fontproperties=my_font)

#添加图例
plt.legend(loc="upper left",prop=my_font)

#展示
plt.show()