import socket
def f1():#用户可以传递#静态页面，html的操作
    #return b'f1'#返回的数据可以是数据库，可以是heml
    f = open('index.html','rb')
    data = f.read()
    f.close()
    return data
def f2(request):
    return b'f2'


def f3():#动态页面--数据库的连接操作
    import pymysql
    #创建连接--数据库操作
    conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',db='db1')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select id,username,password from userinfo")
    user_list = cursor.fetchall()
    cursor.close()
    conn.close()

    #将数据库的数据进行拼接称一个表格
    content_list = []
    for row in user_list:
        tp = "<tr><td>%s</td><td>%s</td><td>%s</td></tr>"%(row['id'],row['username'],row['password'])
        content_list.append(tp)
    content = ''.join(content_list)

    #替换操作
    f = open('userlist.html', 'r',encoding="utf-8")
    template = f.read()
    f.close()

    data = template.replace("@@rr@@", content)
    return bytes(data,encoding='utf-8')



routers =[
    ('/xxx',f1),
    ('/ooo',f2),
    ('/userlist.html',f3)
]

def run():

    sock = socket.socket()
    sock.bind(('127.0.0.1',8080))
    sock.listen(5)
    while True:
        conn,addr = sock.accept()

        data = conn.recv(8096)
        print(data)
        #将数据进行处理，转换成字符串形式的
        data = str(data,encoding="utf-8")
        #响应的数据包括响应头和响应体进行切开
        headers,bodys = data.split('\r\n\r\n')#直到遇到两个请求体就遇到了请求内容
        #头中的按照url进行切开
        temp_list  = headers.split('\r\n')
        method,url,protocal = temp_list[0].split(' ')
        conn.send(b'HTTP/1.1 200 OK\r\n\r\n')

        #请求端口发来请求时，需要先进行查看请求的端口是那个：
        funcname = None
        for item in routers:
            if item[0] == url:#请求端的url就是这个，与自己已经存在的进行比较，
                funcname = item[1]#这个item是个函数，放了要响应的东西
                break
        if funcname:
            response = funcname()
        else:
            response = b'404'
        conn.send(response)
        conn.close()

if __name__ =='__main__':
    run()



'''
get请求没有qing
b'GET /userlist.html%EF%BC%9Fname=d&sdg=sd HTTP/1.1\r\nHost: 127.0.0.1:8080\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\n
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nSec-Fetch-Site: none\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-User: ?1\r\n
Sec-Fetch-Dest: document\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9\r\n\r\n'
#发现geturl后面请求中就含有内容，而

post才有post请求体
b'GET /userlist.html%EF%BC%9Fname=d&sdg=sd HTTP/1.1\r\n
Host: 127.0.0.1:8080\r\nConnection: keep-alive\r\n
Upgrade-Insecure-Requests: 1\r\n
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36\r\n
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n
Sec-Fetch-Site: none\r\n
Sec-Fetch-Mode: navigate\r\n
Sec-Fetch-User: ?1\r\n
Sec-Fetch-Dest: document\r\n
Accept-Encoding: gzip, deflate, br\r\n
Accept-Language: zh-CN,zh;q=0.9\r\n\r\n'

\b'POST / HTTP/1.1\r\nHost: 127.0.0.1:8080\r\n
Connection: keep-alive\r\n
Content-Length: 0\r\n
Cache-Control: max-age=0\r\n
Upgrade-Insecure-Requests: 1\r\n
Origin: http://127.0.0.1:8080\r\n
Content-Type: application/x-www-form-urlencoded\r\n
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36\r\n
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n
\Sec-Fetch-Site: same-origin\r\nSec-Fetch-Mode: navigate\r\n
Sec-Fetch-User: ?1\r\n
Sec-Fetch-Dest: document\r\n
Referer: http://127.0.0.1:8080/xxx\r\n
Accept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9\r\n\r\n'


age: zh-CN,zh;q=0.9\r\n\r\nuser=sd&pass=ds'
前面如果没有名字就不会显示

b'GET /favicon.ico HTTP/1.1\r\nHost: 127.0.0.1:8080\r\nConnection: keep-alive\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36\r\nAccept: image/webp,image/apng,image/*,*/*;q=0.8\r\nSec-Fetch-Site: same-origin\r\nSec-Fetch-Mode: no-cors\r\nSec-Fetch-Dest: image\r\nReferer: http://127.0.0.1:8080/xxx\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9\r\n\r\n'
'''