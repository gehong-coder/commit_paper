from matplotlib import pyplot as plt
from matplotlib import font_manager

'''绘制多个图形'''

#字体设置
my_font=font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

#设置x与y(也就是拿出数据）
x=range(11,31)#因为要到30岁所以后面要写到31
y1=[1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y2=[7,0,1,0,2,4,8,2,3,4,4,5,6,5,4,3,3,1,9,1]

#设置图形大小
plt.figure(figsize=(20,8),dpi=80)

#描点,为什么要添加label呢，因为可以为图形添加图例使用。
#可以指定颜色进行传输,在描点的时候进行描述，线的风格，直线，虚线
plt.plot(x,y1,label="自己",color="orange",linestyle=':')
plt.plot(x,y2,label="同桌",color="cyan",linestyle='--')

#换x符号
_xtick_lables=["{}岁".format(i) for i in range(11,31)]

#换出x或y
plt.xticks(list(x),_xtick_lables,rotation=45,fontproperties=my_font)
plt.yticks(range(0,9))

#添加图片信息
plt.xlabel("岁数",fontproperties=my_font)
plt.ylabel("交朋友个数",fontproperties=my_font)
plt.title("女朋友交友趋势",fontproperties=my_font)

#给点加上网格。所以显示更加清晰
plt.grid(alpha=0.4,linestyle=':')
#调整网格的粗细和质感通过alpha调整

#因为现在有两跳线需要进行标注，哪一条线是谁的，进行标记，添加legend-图例，显示中文的属性-添加图例
plt.legend(prop=my_font,loc="upper left")
#调整图例信息的位置


#画图在一个图中画出两条折线
plt.show()