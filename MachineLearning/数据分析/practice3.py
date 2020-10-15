from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font=font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

#数据
a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]
#绘制多个图形在一起时，需要x的移动越来越往右移动。

x_14=list(range(len(a)))
x_15=[i+0.2 for i in x_14]
x_16=[i+0.4 for i in x_14]
plt.barh(range(len(a)),b_14,height=0.2,label="14日")
plt.barh(x_15,b_15,height=0.2,label="15日")
plt.barh(x_16,b_16,height=0.2,label="16日")

#设置y上的刻度
plt.yticks(x_15,a,fontproperties=my_font)#将y放在中间，所以将她放在中间

#设置图例
plt.legend(prop=my_font)
plt.grid(alpha=0.5)
plt.show()