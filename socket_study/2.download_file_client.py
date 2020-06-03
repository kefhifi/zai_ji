import socket

def main():
    download_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = input("inpu server ip: ")
    port = input("input server port: ")
    if not addr:
        addr = "119.45.0.4"
    if not port:
        port = 39328
    else:
        port = int(port)
    addr_port = (addr, port)
    download_socket.connect(addr_port)
    file_name = input("input file name: ")
    download_socket.send(file_name.encode("utf-8"))
    with open("file_name", "wb") as file_obj:
        while True:
            recv_data = download_socket.recv(1024)
            if recv_data:
                file_obj.write(recv_data)
    download_socket.close()

if __name__ == "__main__":
    main()
