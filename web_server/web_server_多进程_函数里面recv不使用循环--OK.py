
import gevent
from gevent import monkey
import socket
import time
import threading
import re
import multiprocessing

# 怎么判断recv接收数据完成，里面的参数设置多大？？？
# 短链接 ：发送完数据就关闭连接，所以可使用数据为空来判断连接是否已经关闭。

def service_client(new_http_socket, i):
    all_recv_data = bytes("", "utf-8")
    recv_data = new_http_socket.recv(1024)
    if recv_data:
        all_recv_data += recv_data
        all_recv_data = all_recv_data.decode("utf-8")
        #  假定第一行时请求行 GET，POST，PUT 等等
        all_recv_data = all_recv_data.split("\r\n")
        request_file = re.findall(" (/.*)? ", all_recv_data[0])
        # GET / HTTP/1.1
        time.sleep(0.1)
        # 拼凑响应
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        new_http_socket.send(response.encode("utf-8"))
        if request_file[0] == "/":
            request_file[0] = "/index.html"
        try:
            with open("html"+request_file[0], "rb") as file_obj:
                content = file_obj.read()
        except:
            content = "404 not found.".encode("utf-8")
        new_http_socket.send(content)
    new_http_socket.close()


def main():
    http_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 加上下面这行，是为了意外关闭server后，再次启动server时不会提示端口已经被占用了
    http_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    ip_port = ("", 39328)
    http_socket.bind(ip_port)
    http_socket.listen(128)
    i = 1
    while True:
        # 有下面这两行，这个循环里面不用先关闭新产生的套接字，浏览器访问也不会转圈，为什么？（因为str_socket 下面这行被重新赋值了，
        # 再来一个客户端的话，accept又重新给str_socket赋值时，此时浏览器停止转圈）
#        str_socket = "http_socket_" + str(i)
#        thread_num = "Process_" + str(i)
        str_socket, client_addr = http_socket.accept()
        process_num = multiprocessing.Process(target=service_client, args=(str_socket, i))
        process_num.start()
        # 采用多进程实现，此处需要调用close，而采用多线程实现则不能调用close（因为多线程没有像多进程那样要复制一份变量到子进程里面）。
        str_socket.close()
        i += 1
    http_socket.close()


if __name__ == "__main__":
    main()
