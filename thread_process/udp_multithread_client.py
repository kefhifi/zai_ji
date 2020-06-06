

import socket
import threading

ip_port = ("119.45.0.4", 39318)  # 是一个元组类型的
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def send_msg(udp_socket, ip_port):
    while True:
        send_data = input("input info: ")
        udp_socket.sendto(send_data.encode("utf-8"), ip_port)


def recv_msg(udp_socket):
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data[0].decode("utf-8"))


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM）
    t1 = threading.Thread(target=send_msg, args = (udp_socket, ip_port))
    t2 = threading.Thread(target=recv_msg, args = (udp_socket,))
    t1.start()
    t2.start()
    udp_socket.close()

if __name__ == "__main__":
    main()
