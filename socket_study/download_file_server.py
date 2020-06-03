import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", 39328))
server_socket.listen(128)
while True:
    new_socket, client_addr = server_socket.accept()
    file_name = new_socket.recv(1024)
    print("Client (%s) download file: %s " %  (str(client_addr), file_name.decode("utf-8")))
    # with 这种方式适合能打开的情况(万一文件不存在，就打不开了)，比如以w的模式打开。如果以读的模式打开就用open
    try:
        file_obj = open(file_name, "rb")
    except Exception as ret:
        print("open file failed.")
    else:
        file_content = file_obj.read(1024*1024)
        file_obj.close()
        new_socket.send(file_content)
    new_socket.close()
server_socket.close()



