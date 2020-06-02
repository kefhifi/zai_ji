import socket


def main():
    while True:
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.connect(("119.45.0.4", 39318))
        while True:
            send_data = input("Please input message('quit' to exit): ")
            if send_data != "quit":
                tcp_socket.send(send_data.encode("utf-8"))
                recv_data = tcp_socket.recv(1024)
                print(recv_data.decode("utf-8"))
                """
                recv_data 里的数据和udp协议里面的不一样，不能那样解码
                print("From Server: " + recv_data[1][0] + ":" + str(recv_data[1][1]) + ":  " + recv_data[0].decode("utf-8"))
                """
            else:
                break
        tcp_socket.close()

if __name__ == '__main__':
    main()
