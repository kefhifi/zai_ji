
import gevent
from gevent import monkey
import socket
import time
import threading
import re
import multiprocessing

# 怎么判断recv接收数据完成，里面的参数设置多大？？？
# 短链接 ：发送完数据就关闭连接，所以可使用数据为空来判断连接是否已经关闭。

def service_client(new_http_socket):
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
        new_socket, client_addr = http_socket.accept()
        process_num = multiprocessing.Process(target=service_client, args=(new_socket,))
        process_num.start()
        # 父进程和子进程的new_socket相当于两个硬链接，都指向文件描述符，
        # 所以在父进程里面先关掉new_socket，不影响子进程里面的套接字指向的文件描述符。
        new_socket.close()
    http_socket.close()


if __name__ == "__main__":
    main()
