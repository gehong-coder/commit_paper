#名字要有意义
print("hello")
#注释：不会运行
'''多行注释'''
"""多行注释"""
'''两个单词使用_来分割
#切片：访问字符串的字串： 左闭右开原则'''
a="你好吗"
b=a.replace("吗","").replace("?","!")
print(b)

if False:
    print("true")
elif True:
    print("True")
else:
    print("else")
a = 1
b = 1
c = 1
print(id(a))
print(id(b))
print(id(c))

if "ab">"bc":
    print("1")
else :
    print("0")

'''
and 
or
not :取反
'''
print(1 and 0)
print(1 or 0)
print(not 0)

'''
身份运算
'''

a = [1,2,3,4]
b = a
c = [1,2,3,4]
print(a is b)
print(a is not b)

#list
list1=[1,2,3,4]
list2=[1,2,3,'gh',[1,34,2]]
print(list1)
print(list2)
print(list1[0:2])
'''左闭右开'''
list1.append(7)
print(list1)
#更新
#嵌套的使用
print(list2[4][2])