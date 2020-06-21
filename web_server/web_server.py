
import gevent
from gevent import monkey
import socket
import time
import threading
import re

# 怎么判断recv接收数据完成，里面的参数设置多大？？？
# 短链接 ：发送完数据就关闭连接，所以可使用数据为空来判断连接是否已经关闭。

def service_client(new_http_socket, i):
    all_recv_data = bytes("", "utf-8")
    while True:
        print("......while True...start.")
        # 阻塞在这里不是长连接的问题，是因为客户端没有断开连接，所以不会收到空数据。
        recv_data = new_http_socket.recv(10)
        print(recv_data.decode("utf-8"))
        print("....after....recv.....")
        if recv_data:
            all_recv_data += recv_data
        else:
            print("....", recv_data)
            break
    print(all_recv_data.decode("utf-8"))
    print("333333")
    all_recv_data = all_recv_data.decode("utf-8")
    #  假定第一行时请求行 GET，POST，PUT 等等
    all_recv_data = all_recv_data.split("\r\n")
    request_file = re.findall(" (/.*)? ", all_recv_data[0])
# 调试到这里了
    if request_file:
        print("request_file: ", request_file[0])
        # GET / HTTP/1.1
        print("Thread--", i, recv_data)
        time.sleep(1)
        # 拼凑响应
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        response += "<h1>Hahahaha</h1>"
        new_http_socket.send(response.encode("utf-8"))
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
        str_socket = "http_socket_" + str(i)
        thread_num = "Thread_" + str(i)
        str_socket, client_addr = http_socket.accept()
        thread_num = threading.Thread(target=service_client, args=(str_socket, i))
        thread_num.start()
        i += 1
    http_socket.close()


if __name__ == "__main__":
    main()
