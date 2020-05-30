
import socket

# 创建套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 准备接收方地址和端口
address=("192.168.0.6", 8080)  # 是一个元组类型的
while True:
    send_data = input("Please input info: ")  # 从键盘获取数据
    if send_data == "quit":
        break
    # 发送数据
    udp_socket.sendto(send_data.encode("utf-8"), address)
    # 接收对方发送过来的数据
    recv_data = udp_socket.recvfrom(1024)
    # 显示接收到的数据
    # 接收到的数据是一个元组类型的，第一个元素是对方发送的数据，第二个元素是对方的地址和端口
    print("From Server: " + recv_data[1][0] + ":" + str(recv_data[1][1]) + ":    " + recv_data[0].decode("utf-8"))
    address = recv_data[1]

udp_socket.close()

