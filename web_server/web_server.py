
import gevent
from gevent import monkey
import socket
import time
import threading


def service_client(new_http_socket, i):
    recv_data = new_http_socket.recv(1024)
    if recv_data:
        recv_data = recv_data.decode("utf-8")
        # GET / HTTP/1.1
        print("Thread--", i, recv_data)
        time.sleep(3)
        # 拼凑响应
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        response += "<h1>Hahahaha</h1>"
        new_http_socket.send(response.encode("utf-8"))
        new_http_socket.close()


def main():
    http_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 加上下面这行，是为了意外关闭server后，再次启动server时不会提示端口已经被占用了
    http_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
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
