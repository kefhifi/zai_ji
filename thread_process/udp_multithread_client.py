import socket
import threading
import time
ip_port = ("119.45.0.4", 39318)  # 是一个元组类型的


def send_msg(udp_socket, ip_port):
    while True:
        send_data = input("input info: ")
        if send_data == "quit":
            break
        udp_socket.sendto(send_data.encode("utf-8"), ip_port)


def recv_msg(udp_socket, ip_port):
    # 不加下面这行报错（recv_data = udp_socket.recvfrom(1024)，SError: [WinError 10022] 提供了一个无效的参数。）为什么？
    udp_socket.sendto("hi".encode("utf-8"), ip_port)
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data[0].decode("utf-8"))
        threads_nums = len(threading.enumerate())
        if threads_nums == 2:
            break


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    t1 = threading.Thread(target=send_msg, args=(udp_socket, ip_port))
    t2 = threading.Thread(target=recv_msg, args=(udp_socket, ip_port))
    t1.start()
    t2.start()
    time.sleep(5)
    print(threading.enumerate())

if __name__ == "__main__":
    main()
