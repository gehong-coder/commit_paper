#所使用的包
import requests
#设置url
url = "https://www.baidu.com/"

#使用url找到页面
response = requests.get(url)

#设置字符编码
response.encoding = 'utf-8'

#输出内容
print(response.text)