import redis
import pymysql
from urllib import request


class SystemStatus():
    def __init__(self, url, name, db_host, db_port, db_password, db_database, redis_host, redis_port, redis_password):
        self.__status = -1
        self.__url = url
        self.__name = name
        self.__db_host = db_host
        self.__db_port = db_port
        self.__db_password = db_password
        self.__db_database = db_database
        self.__redis_host = redis_host
        self.__redis_port = redis_port
        self.__redis_password = redis_password

    def __status_detect(self):
        try:
            result = request.urlopen(self.__url, timeout=5)
        except Exception as ret:
            print(ret)
            self.__status = 0
        else:
            # print(type(result.status), result.reason)  # 打印 响应头的状态码、状态
            # result = result.read()
            # result = str(result, encoding="utf-8")
            # print(result)
            if result.status == 200:
                self.__status = 1
            else:
                self.__status = 0

    def __read_mysql(self):
        pass

    def __write_redis(self):
        pass

    def fetch_status(self):
        pass


    def detect_status(self):
        self.__status_detect()






def main():
    service = SystemStatus("https://semm.zhizhangyi.com:3000/emm", "SEMM", "127.0.0.1", 3306, "123456", "system_status",
                           "127.0.0.1", 39328, "123456")
    if fetch_status == None:
        service.detect_status()
        fetch_status




if __name__ == "__main__":
    main()
