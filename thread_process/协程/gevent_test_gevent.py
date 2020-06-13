from urllib import request
import time
import sys
print(sys.path)


import gevent
from gevent import monkey


monkey.patch_all()

url_sohu = "https://www.sohu.com"
url_douyu = "https://www.douyu.com/directory/all"
url_sina = "https://www.sina.com.cn"
data_sohu = data_douyu = data_sina = 0

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
    gevent.joinall([
        gevent.spawn(url_request, url_sohu),
        gevent.spawn(url_request, url_douyu),
        gevent.spawn(url_request, url_sina)

    ])
    time_mid = time.time()
    gevent.joinall([
        gevent.spawn(read_data, url_sohu),
        gevent.spawn(read_data, url_douyu),
        gevent.spawn(read_data, url_sina)

    ])
    time_end = time.time()
    print(time_mid-time_start)
    print(time_end-time_mid)




if __name__ == "__main__":
    main()


