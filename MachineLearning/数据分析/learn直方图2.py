#绘制已经被统计过的数据
#使用bar来描述直方图
#描述分布的状态
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font=font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

#数据
interval = [0,5,10,15,20,25,30,35,40,45,60,90]#x
width = [5,5,5,5,5,5,5,5,5,15,30,60]#组距
quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]#共有多少个长条

plt.figure(figsize=(20,8),dpi=80)
#描点
plt.bar(range(len(quantity)),quantity,width=1)#每个的width都有默认值
#设置刻度
_x=[i-0.5 for i in range(13)]#共有多少个刻度,不能忘记最后一个的值，更改
_xtables=interval+[150]#本来已经是一个列表，所以使用列表进行

plt.xticks(_x,_xtables)

plt.show()