from urllib import request
import time
import threading
import multiprocessing


url_sohu = "https://www.sohu.com"
url_douyu = "https://www.douyu.com/directory/all"
url_sina = "https://www.sina.com.cn"

def main():
    time_start = time.time()
    data_sohu = request.urlopen(url_sohu)
    data_douyu = request.urlopen(url_douyu)
    data_sina = request.urlopen(url_sina)
    time_mid = time.time()
    data_sohu = data_sohu.read()
    data_douyu = data_douyu.read()
    data_sina = data_sina.read()
    time_end = time.time()
    print(time_mid-time_start)
    print(time_end-time_mid)




if __name__ == "__main__":
    main()


