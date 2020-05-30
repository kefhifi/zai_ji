import socket


def send_msg(udp_socket):
    msg = input("input content: ")
    ip = input("对方的ip：")
    port = int(input("对方的端口号： "))
    udp_socket.sendto(msg.encode("utf-8"),(ip,port))

def recv_msg(udp_socket):
    recv_data = udp_socket.recvfrom(1024)
    ip = recv_data[1]
    port= recv_data[1]
    msg = recv_data[0].decode("utf-8")
    print(type(recv_data[1]))

    print(">>> %s: %s " % (str(ip), msg))

def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address=("192.168.0.6", 8080)
    # udp_socket.bind(address)
    udp_socket.bind(("", 8080))  # 参数也是元组类型的
    while True:
        op_num = input("输入选择的功能序号(1 发送消息，2 接收消息： ")
        if op_num == "1":
            send_msg(udp_socket)
        elif op_num == "2":
            recv_msg(udp_socket)
        else:
            print("input error")


if __name__ == '__main__':
    main()










