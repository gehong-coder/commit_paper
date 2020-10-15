

from matplotlib import pyplot as plt
#倒入
x = range(2,26,2)
y = [15,13,4,5,6,7,9,20,15,44,66,99]#x,y都已经放入的
#画图之前设置图片大小
plt.figure(figsize=(20,8),dpi=80)#大小和清晰度
#染个刻度\
_xticks_label=[i+0.5 for i in range(2,59)]#传的什么就显示什么，就说明可以了n
plt.xticks(_xticks_label)
plt.plot(x,y)#描点
#保存的地方
#plt.savefig("./t1.png")#绝对路径的保存，让保存更好一些。
plt.show()#画图
#让数据更清晰-figure


