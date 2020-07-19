import redis
import pymysql
from urllib import request
import time
import multiprocessing


class SystemStatus():
    def __init__(self, url, service_name, db_host, db_port, db_password, db_database, redis_host, redis_port, redis_password):
        self.__status = -1
        self.__url = url
        self.__service_name = service_name
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
            print(type(result.status), result.reason)  # 打印 响应头的状态码、状态
            # result = result.read()
            # result = str(result, encoding="utf-8")
            # print(result)
            if result.status == 200:
                self.__status = 1
            else:
                self.__status = 0

    def __write_mysql(self):
        pass

    def __read_mysql(self):
        pass

    def __write_redis(self):
        pass

    def fetch_status(self):
        try:
            redis_obj = StrictRedis(host="119.45.0.4", port=39328, db=0, decode_responses=True, password="H3z5udsuz7ze_Pk7w8qp2")
        except Exception as ret:
            print(ret)
        else:
    	    if not redis_obj.get("SEMM"):
                print("redis set error!")
                exit(1)
            print(redis_obj.get("hello"))



    def detect_status(self):
        pass
        #self.__status_detect()


def update_mysql_and_redis_stat():
	# 查询数据库中所有saas环境的服务状态情况，并更新mysql和redis对应的状态
	while True:
		update_mysql_redis_data()
		time.sleep(60)


def web_server()
	# 接收http请求，查询redis中状态, 并更新页面内容，返回页面内容(动态和静态页面)
	while True:
		tcp_server_listen()
		get_redis_info()
		update_dynamic_pages()
		send_dynamic_pages()



def main():
    ## saas_service = SystemStatus("https://semm.zhizhangyi.com:3000/emm", "SEMM", "127.0.0.1", 3306, "123456", "system_status",
    #                       "127.0.0.1", 39328, "123456")
    # if saas_service.fetch_status == None:
    ## saas_service.detect_status()
    # service.fetch_status
	# 面向过程
	
	update_process = multiprocessing.Process(target=update_mysql_and_redis_stat, args=(,)) 
	server_process = multiprocessing.Process(target=web_server, args=(,))   
	update_process.start()
	server_process.start()	
		



if __name__ == "__main__":
    main()
