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


def application(env, set_response_header):
    set_response_header("200 OK", [("Content-Type", "text/html")])
    return "Hello World %s" % time.ctime()

