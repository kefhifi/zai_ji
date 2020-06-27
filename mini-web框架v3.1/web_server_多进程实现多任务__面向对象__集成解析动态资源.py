
import gevent
from gevent import monkey
import socket
import time
import threading
import re
import multiprocessing
import mini_frame

# 怎么判断recv接收数据完成，里面的参数设置多大？？？
# 短链接 ：发送完数据就关闭连接，所以可使用数据为空来判断连接是否已经关闭。

class WSGIServer():
    def __init__(self):
        self.http_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 加上下面这行，是为了意外关闭server后，再次启动server时不会提示端口已经被占用了
        self.http_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.ip_port = ("", 39328)
        self.http_socket.bind(self.ip_port)
        self.http_socket.listen(128)
    def service_client(self, new_http_socket):
        all_recv_data = bytes("", "utf-8")
        recv_data = new_http_socket.recv(1024)
        if recv_data:
            all_recv_data += recv_data
            all_recv_data = all_recv_data.decode("utf-8")
            print(all_recv_data)
            #  假定第一行时请求行 GET，POST，PUT 等等
            all_recv_data = all_recv_data.split("\r\n")
            request_file = re.findall(" (/.*)? ", all_recv_data[0])
            # 判断是否以.py结尾，以确定是否是动态资源，静态资源：html/css/js/png/jpg等
            if not request_file[0].endswith(".py"):
                # GET / HTTP/1.1
                time.sleep(0.1)
                if request_file[0] == "/":
                    request_file[0] = "/index.html"
                try:
                    with open("html"+request_file[0], "rb") as file_obj:
                        content = file_obj.read()
                except:
                    header = "HTTP/1.1 404 NOT FOUND\r\n\r\n".encode("utf-8")
                    content = "404 not found.".encode("utf-8")
                else:
                    header = "HTTP/1.1 200 OK\r\n\r\n".encode("utf-8")
                new_http_socket.send(header + content)
            # 动态资源
            else:
                # endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False
                header = "HTTP/1.1 200 OK\r\n\r\n"
                body = mini_frame.application(request_file[0])
                response = header + str(body)
                new_http_socket.send(response.encode("utf-8"))


        new_http_socket.close()

    def run_forever(self):
        while True:
            # 有下面这两行，这个循环里面不用先关闭新产生的套接字，浏览器访问也不会转圈，为什么？（因为str_socket 下面这行被重新赋值了，
            # 再来一个客户端的话，accept又重新给str_socket赋值时，此时浏览器停止转圈）
            # str_socket = "http_socket_" + str(i)
            # thread_num = "Process_" + str(i)
            str_socket, client_addr = self.http_socket.accept()
            process_num = multiprocessing.Process(target=self.service_client, args=(str_socket,))
            process_num.start()
            # 采用多进程实现，此处需要调用close，而采用多线程实现则不能调用close（因为多线程没有像多进程那样要复制一份变量到子进程里面）。
            str_socket.close()
        self.http_socket.close()


def main():
    wsgi_server = WSGIServer()
    wsgi_server.run_forever()


if __name__ == "__main__":
    main()
