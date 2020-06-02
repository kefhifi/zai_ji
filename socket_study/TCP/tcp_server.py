import socket


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind(("", 39318))  # 绑定
    tcp_socket.listen(128) # 使用socket创建的套接字默认是主动的，使用listen将其变为被动的，这样就可以接收别人的连接了
    new_socket, client_addr = tcp_socket.accept()  # 等待客户端连接
    #print( tcp_socket.accept())  # 等待客户端连接
    """
    (<socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('10.0.0.6', 39318), 
    raddr=('222.131.153.176', 4053)>, ('222.131.153.176', 4053))
    """
    print("waiting client to connet ......")
    print(client_addr)
    recv_data = new_socket.recv(1024)
    print(recv_data.decode("utf-8"))
    new_socket.send("Hi".encode("utf-8"))
    new_socket.close()
    tcp_socket.close()


if __name__ == '__main__':
    main()
