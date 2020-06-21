import socket
import time
import re
import select


# 怎么判断recv接收数据完成，里面的参数设置多大？？？
# 短链接 ：发送完数据就关闭连接，所以可使用数据为空来判断连接是否已经关闭。


def service_client(epl, new_socket_dict, socket_item, fd):
    try:
        recv_data = socket_item.recv(1024)
    except Exception as ret:
        print(ret)
        print("为啥微软edge浏览器关闭连接后，这里异常了")
        exit(0)
    if recv_data:
        recv_data = recv_data.decode("utf-8")
        print(recv_data)
        #  假定第一行时请求行 GET，POST，PUT 等等
        recv_data = recv_data.split("\r\n")
        request_file = re.findall(" (/.*)? ", recv_data[0])
        # GET / HTTP/1.1
        # 拼凑响应
        response_header = "HTTP/1.1 200 OK\r\n"
        # response += "\r\n"
        # socket_item.send(response.encode("utf-8"))
        if request_file[0] == "/":
            request_file[0] = "/index.html"
        try:
            with open("html"+request_file[0], "rb") as file_obj:
                content = file_obj.read()
        except:
            content = "404 not found.".encode("utf-8")
        response_body = content
        # con_len = str(len(response_body))
        # response_header = response_header + "Content-Length: " + con_len + "\r\n\r\n"
        response_header += "Content-Length: %d\r\n\r\n" % len(response_body)
        response_all = response_header.encode("utf-8") + response_body
        # 下面这种方式是不行的，会提示：TypeError: string argument without an encoding
        # response = bytes(response) + content
        socket_item.send(response_all)
    else:
        epl.unregister(fd)  # 可以销毁在main函数里面注册的fd
        del new_socket_dict[fd]  # 可以删除掉main函数对应字典里面的元素
        socket_item.close()


def main():
    http_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 加上下面这行，是为了意外关闭server后，再次启动server时不会提示端口已经被占用了
    http_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 创建一个epoll对象
    epl = select.epoll()
    # 将监听套接字对应的fd注册到epoll中
    epl.register(http_socket.fileno(), select.EPOLLIN)

    ip_port = ("", 39328)
    http_socket.bind(ip_port)
    http_socket.listen(128)
    new_socket_dict = {}
    # new_socket_dict = dict()
    while True:
        fd_event_list = epl.poll()  # 默认堵塞，直到OS检测到数据到来，通过事件通知方式告诉这个程序，此时解堵塞
        # [(fd, event),(套接字对应的文件描述符，这个文件描述符到底是什么事件，例如：可以调用recv接收等)]
        for fd, event in fd_event_list:
            if fd == http_socket.fileno():
                new_socket, client_addr = http_socket.accept()
                epl.register(new_socket.fileno(), select.EPOLLIN)
                new_socket_dict[new_socket.fileno()] = new_socket
            else:
                service_client(epl, new_socket_dict, new_socket_dict[fd], fd)
                # 下面7行是调试信息，可以删掉
                # time.sleep(10)
                # print("......浏览器关闭一个连接后，看看主函数的字典里面还有没有对应的键值（因为是在子函数里面删除的），....")
                # print(new_socket_dict)
                # print("....打印字典完成....")
                # print("......查看删除了的fd.还存在不？因为也是在子函数里面删除的.......")
                # print("------------", epl)
                # print("....打印epl完成....")
        time.sleep(1)
    epl.close()
    http_socket.close()


if __name__ == "__main__":
    main()
