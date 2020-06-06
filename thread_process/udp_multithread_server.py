import socket
import threading

ip_port = ("119.45.0.4", 39318)

def recv_msg(udp_socket):
    global ip_port
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data[0].decode("utf-8"))
        ip_port = recv_data[1]


def send_msg(udp_socket):
    while True:
        msg = input("input info: ")
        udp_socket.sendto(msg.encode("utf-8"), ip_port)


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 39318))
    t1 = threading.Thread(target=recv_msg, args=(udp_socket,))
    #     t2 = threading.Thread(target=send_msg, args=(udp_socket, ip, port))  # 也可以这样传递参数
    t2 = threading.Thread(target=send_msg, args=(udp_socket,))
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()