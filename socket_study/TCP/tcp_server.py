import socket


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind(("", 39328))  # 绑定
    tcp_socket.listen(128) # 使用socket创建的套接字默认是主动的，使用listen将其变为被动的，这样就可以接收别人的连接了
    while True:
        new_socket, client_addr = tcp_socket.accept()  # 等待客户端连接
        #print( tcp_socket.accept())  # 等待客户端连接
        """
        (<socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('10.0.0.6', 39318), 
        raddr=('222.131.153.176', 4053)>, ('222.131.153.176', 4053))
        """
        print("waiting client to connet ......")
        print(client_addr)
        while True:
            recv_data = new_socket.recv(1024)
            # recv解堵塞：1 客户端发送了数据；2 客户端调用close关闭了连接，返回值为空。
            recv_data = recv_data.decode("utf-8") # recv_data 里面只有数据，没有地址和端口（和udp的recvfrom接收到的数据不一样)
            if recv_data:
                print(recv_data)
                send_data = input("input info: ")
                new_socket.send(send_data.encode("utf-8"))
            else: # 如果recv_data为空，则证明客户端关闭了连接
                print("client is away.")
                break
        new_socket.close()
    tcp_socket.close()


if __name__ == '__main__':
    main()
