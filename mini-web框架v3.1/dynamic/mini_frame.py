import time

#
# def login():
#     return "....login....%s" % time.ctime()
#
#
# def register():
#     return "....register....%s" % time.ctime()
#
#
# def quit():
#     return "....quit....%s" % time.ctime()
#
#
# def application(file_name):
#     if file_name == "/login.py":
#         return login()
#     elif file_name == "/register.py":
#         return register()
#     elif file_name == "/quit.py":
#         return quit()
#     else:
#         return "not found the page!"

def login():
    return "这是登录页面"


def index():
    return "这是主页"


def application(environ, set_response_header):
    set_response_header("200 OK", [("Content-Type", "text/html;charset=utf-8")])
    file_name = environ["PATH_INFO"]
    if file_name == "/login.py":
        return login()
    elif file_name == "/index.py":
        return index()
    else:
        return "Hello World %s 测试" % time.ctime()

