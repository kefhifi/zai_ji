from urllib import request
import time
import multiprocessing


url_sohu = "https://www.sohu.com"
url_douyu = "https://www.douyu.com/directory/all"
url_sina = "https://www.sina.com.cn"

data_sohu = 0
data_douyu = 0
data_sina = 0


def url_request(url):
    if url == url_sohu:
        data_sohu = request.urlopen(url)
    elif url == url_douyu:
        data_douyu = request.urlopen(url)
    elif url == url_sina:
        data_sina = request.urlopen(url)


def read_data(url, key, return_dict):
    data_sohu_1 = data_douyu_1 = data_sina_1 = 0
    if url == url_sohu:
        data_sohu_1 = data.read()
    elif url == url_douyu:
        data_douyu_1 = data.read()
    elif url == url_sina:
        data_sina_1 = data.read()


def main():
    time_start = time.time()
    p1 = multiprocessing.Process(target=url_request, args=(url_sohu,))
    p2 = multiprocessing.Process(target=url_request, args=(url_douyu,))
    p3 = multiprocessing.Process(target=url_request, args=(url_sina,))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    time_mid = time.time()
#    p4 = multiprocessing.Process(target=read_data, args=(url_sohu, "sohu", return_dict))
#    p5 = multiprocessing.Process(target=read_data, args=(url_douyu, "douyu", return_dict))
#    p6 = multiprocessing.Process(target=read_data, args=(url_sina, "sina", return_dict))
#    p4.start()
#    p5.start()
#    p6.start()
#    p4.join()
#    p5.join()
#    p6.join()
    time_end = time.time()
    print(time_mid-time_start)
    print(time_end-time_mid)




if __name__ == "__main__":
    main()


