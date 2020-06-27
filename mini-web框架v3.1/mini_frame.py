import time

def login():
    return "....login....%s" % time.ctime()


def register():
    return "....register....%s" % time.ctime()


def quit():
    return "....quit....%s" % time.ctime()


def application(file_name):
    if file_name == "/login.py":
        login()
    elif file_name == "/register.py":
        register()
    elif file_name == "/quit.py":
        quit()
    else:
        return "not found the page!"

