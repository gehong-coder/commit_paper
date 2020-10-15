from matplotlib import pyplot as plt
import random
from matplotlib import font_manager


#my_font=font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

my_font=font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")#直接将路径进行放入
#实例化一个字体


x = range(0,120)
y = [random.randint(20,35) for i in range(120)]

plt.figure(figsize=(20,9),dpi=80)
plt.plot(x,y)

''''# 在画完图之后进行，调整x的疏密和刻度'''
_xtick_labels_=["10点{}分".format(i) for i in range(60)]
_xtick_labels_+=["11点{}分".format(i) for i in range(60)]#+=的意思是接住之前的坐标继续绘制徒刑
plt.xticks(list(x)[::3],_xtick_labels_[::3],rotation=270,fontproperties=my_font)#将实例化的字体进行使用
#现在的所对应的是成都一致
#1取步长，步长只有列表才能取步长
#发现太长，使用旋转进行使用rotation，30，45，90，270
#在matplotlab里面不能显示中文
'''给图片添加信息'''
plt.xlabel("时间",fontproperties=my_font)
plt.ylabel("温度 单位（C）",fontproperties=my_font)
plt.title("温度信息",fontproperties=my_font)
plt.show()

