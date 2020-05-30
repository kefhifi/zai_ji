import socket

def send_msg(udp_socket, ip_port):
    msg = input("input send message: ")
    udp_socket.sendto(msg.encode("utf-8"), ip_port)

def recv_msg(udp_socket):
    recv_data = udp_socket.recvfrom(1024)
    msg = recv_data[0].decode("utf-8")
    ip_port = recv_data[1]  # 是一个元组类型
    print("From Client: " + ip_port[0] + ":" + str(ip_port[1])+ ":     " + msg)
    return ip_port
#    print(type(recv_data[1]))
#     print(">>> %s: %s " % (str(ip), msg))

def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address=("192.168.0.6", 8080)
    # udp_socket.bind(address)
    udp_socket.bind(("", 8080))  # 参数也是元组类型的
    while True:
        client_ip_port = recv_msg(udp_socket)
        send_msg(udp_socket, client_ip_port)

if __name__ == '__main__':
    main()










