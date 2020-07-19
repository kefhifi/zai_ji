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

g_fun_dict = dict()


def route(uri):
    def set_fun(func):
        g_fun_dict[uri] = func
        # g_fun_dict["/index.html"] = index
        def call_fun(*args, **kwargs):
            return func(*args, **kwargs)
        return call_fun
    return set_fun


@route("/login.html")
def login():
    return "这是登录页面"


@route("/index.html")
def index():
    return "这是主页"


def application(environ, set_response_header):
    set_response_header("200 OK", [("Content-Type", "text/html;charset=utf-8")])
    file_name = environ["PATH_INFO"]
    """
    if file_name == "/login.html":
        return login()
    elif file_name == "/index.html":
        return index()
    else:
        return "Hello World %s 测试" % time.ctime()
    """
    try:
        # fun = g_fun_dict[file_name]
        # return fun()
        return g_fun_dict[file_name]()
    except Exception as ret:
        return "产生了异常：%s" % str(ret)


