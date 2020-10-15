from urllib.parse import parse_qs
def login():
    with open("index.html","rb") as f:
        data = f.read()
        f.close()
    return data
def reg():
    with open("userlist.html","rb") as f:
        data = f.read()
        f.close()
    return data