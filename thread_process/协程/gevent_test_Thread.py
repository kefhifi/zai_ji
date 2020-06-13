from urllib import request
import time
import threading


url_sohu = "https://www.sohu.com"
url_douyu = "https://www.douyu.com/directory/all"
url_sina = "https://www.sina.com.cn"
data_sohu = 0
data_douyu = 0
data_sina = 0


def url_request(url):
    global data_sohu, data_douyu, data_sina
    if url == url_sohu:
        data_sohu = request.urlopen(url)
    elif url == url_douyu:
        data_douyu = request.urlopen(url)
    elif url == url_sina:
        data_sina = request.urlopen(url)


def read_data(url):
    global data_sohu, data_douyu, data_sina
    if url == url_sohu:
        data_sohu = data_sohu.read()
    elif url == url_douyu:
        data_douyu = data_douyu.read()
    elif url == url_sina:
        data_sina = data_sina.read()


def main():
    time_start = time.time()
    t1 = threading.Thread(target=url_request, args=(url_sohu,))
    t2 = threading.Thread(target=url_request, args=(url_douyu,))
    t3 = threading.Thread(target=url_request, args=(url_sina,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    time_mid = time.time()
    t4 = threading.Thread(target=read_data, args=(url_sohu,))
    t5 = threading.Thread(target=read_data, args=(url_douyu,))
    t6 = threading.Thread(target=read_data, args=(url_sina,))
    t4.start()
    t5.start()
    t6.start()
    t4.join()
    t5.join()
    t6.join()
    time_end = time.time()
    print(time_mid-time_start)
    print(time_end-time_mid)


if __name__ == "__main__":
    main()


