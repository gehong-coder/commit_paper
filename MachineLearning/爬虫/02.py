import requests
url = "https://www.tudouip.com/"

# 添加头信息-请求头信息--以字典的形式写入请求头
header = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0'
}

#什么时候会用到header呢，当某个网站在浏览器上可以进行使用时
# 但是在python中访问不可以使用的时候，使用的是改变头信息中的信息进行修改哦
#依次按照一下的顺序进行修改-useragent，referral-cookie
response = requests.get( url, headers=header)



#保存html信息
with open('xicidaili.html','wb') as f:
    f.write(response.content)