from wsgiref.simple_server import make_server
#这个模块就是可以给自己造服务器

# 3.
def application(environ,start_response):
    #按照协议解析数据
    #按照协议封装数据
    print(environ)
    print(type(environ))

    #因为解析数据之后，每个人请求的数据的地址都是不一样的，所以，拿到解析之后的数据的请求路径
    print("path", environ.get("PATH_INFO"))
    #当前请求路径
    path = environ.get("PATH_INFO")
    start_response("200 ok",[])
    #判断数请求数据的路径是那个
    #路由分发
    def login():
        with open("index.html", "rb") as f:
            data = f.read()
            f.close()
        return data

    def reg():
        with open("userlist.html", "rb") as f:
            data = f.read()
            f.close()
        return data
    url_patren = [
        ("/login", login),
        ("/reg", reg),
    ]
    func = None
    for item in url_patren:
        if path==item[0]:
            func=item[1]
            break



#1。
httped = make_server('',8080,application)
#服务器的地址，端口，响应函数

#2。
httped.serve_forever()

