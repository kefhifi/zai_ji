import gevent
from gevent import monkey
import socket
import time
import threading
import re


monkey.patch_all()
# 怎么判断recv接收数据完成，里面的参数设置多大？？？
# 短链接 ：发送完数据就关闭连接，所以可使用数据为空来判断连接是否已经关闭。


def service_client(new_socket_list):
    print("........%d" % len(new_socket_list))
    all_recv_data = bytes("", "utf-8")
    for socket_item in new_socket_list:
        try:
            recv_data = socket_item.recv(1024)
        except:
            print("no recv data")
        else:
            if recv_data:
                all_recv_data += recv_data
                all_recv_data = all_recv_data.decode("utf-8")
                #  假定第一行时请求行 GET，POST，PUT 等等
                all_recv_data = all_recv_data.split("\r\n")
                request_file = re.findall(" (/.*)? ", all_recv_data[0])
                # GET / HTTP/1.1
                # 拼凑响应
                response = "HTTP/1.1 200 OK\r\n"
                # response += "\r\n"
                # socket_item.send(response.encode("utf-8"))
                if request_file[0] == "/":
                    request_file[0] = "/index.html"
                try:
                    with open("html"+request_file[0], "r") as file_obj:
                        content = file_obj.read()
                except:
                    content = "404 not found."
                con_len = str(len(content.encode("utf-8")))
                response = response + "Content-Length: " + con_len + "\r\n\r\n"
                # 这样header和body一起编码再发送会麻烦一些（冗余），因为前面已经utf-8编码求Content-Length了，这里又重复编码。
                response = (response + content).encode("utf-8")
                # 下面这种方式是不行的，会提示：TypeError: string argument without an encoding
                # response = bytes(response) + content
                socket_item.send(response)
            else:
                new_socket_list.remove(socket_item)
                socket_item.close()


def main():
    http_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 加上下面这行，是为了意外关闭server后，再次启动server时不会提示端口已经被占用了
    http_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    http_socket.setblocking(False)
    ip_port = ("", 39328)
    http_socket.bind(ip_port)
    http_socket.listen(128)
    new_socket_list = list()
    while True:
        try:
            new_socket, client_addr = http_socket.accept()
        except Exception as ret:
            print("no new client ")
        else:
            new_socket.setblocking(False)
            new_socket_list.append(new_socket)
        service_client(new_socket_list)
        time.sleep(1)
    http_socket.close()


if __name__ == "__main__":
    main()
