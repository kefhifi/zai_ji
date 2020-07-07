import redis
import pymysql
from urllib import request
import json
import multiprocessing
import gevent
from gevent import monkey


monkey.patch_all()
class System_Monitor():
	def __init__(self, url, service_name, db_host, db_port, db_user, db_password, db_name, redis_host, redis_port, redis_password):
		self.__status = -1
		self.__url = url
		self.__service_name = service_name
		self.__db_host = db_host
		self.__db_port = db_port
		self.__db_user = db_user
		self.__db_password = db_password
		self.__db_name = db_name
		self.__redis_host = redis_host
		self.__redis_port = redis_port
		self.__redis_password = redis_password
		redis_obj = StrictRedis(host=redis_host, port=redis_port, db=0, decode_responses=True, password=redis_password)
    #def __del__(self):
        


	def __status_detect(self):
		try:
			result = request.urlopen(self.__url, timeout=5)
		except Exception as ret:
			print(ret)
			self.__status = 0
		else:
			# print(type(result.status), result.reason)  # 打印 响应头的状态码、状态
			return result.status,result.reason,json.dumps(result.getheaders())  # result.getheaders 字典类型的响应头, 再转换成json字符串
			#for header_key,header_value in result.getheaders():
				#print("%s: %s" % (header_key,header_value))
			# result = result.read()
			# result = str(result, encoding="utf-8")
			# print(result)
			# if result.status == 200:
				#self.__status = 1
			#else:
				#self.__status = 0

	def __write_mysql(self, state, state_description, response_headers):
		mysql_obj = pymysql.connect(host=self.__db_host, port=self.__db_port, user=self.__db_user, password=self.__db_password, database=self.__db_name, charset="utf-8")
        mysql_cursor = mysql_obj.cursor()
        count = mysql_cursor.execute("update service_address set last_detect_state=%d,last_detect_state_description=%s, last_detect_response_header=%s where service_name=%s",state, state_description, response_headers)
        mysql_obj.commit()
        mysql_cursor.close()
        mysql_obj.close()

	def __read_mysql(self):
		pass

	def __write_redis(self, state, state_description):
		# redis_obj.set(service_name + "_state", str(state))
		redis_obj.set(service_name + "_state", state)
		redis_obj.set(service_name + "_state_description", state_description)

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
		state, state_description, response_headers = self.__status_detect()
        self.__write_redis(state, state_description)
        self.__write_mysql(state, state_description, response_headers)


	def update_service_status()
		service_detect()
		update_mysql()
		update_redis()


	def update_mysql_and_redis_stat():
		service_name, service_url = select_mysql()
		for service_name in service_names:
			update_service_status(service_name, service_url)
		self.__mysql_update_obj.commit()




	def __get_config():
		with open("server.conf") as file_obj:
			conf_info = file_obj.read()
		conf_info = eval(conf_info)  # 通过 eval 把 conf_info 转换成字典了
		try:
			# 初始化实例属性: mysql连接对象
			self.__mysql_update_obj = pymysql.connect(host=conf_info["db_host"], port=conf_info["db_port"], user=conf_info["db_user"], password=conf_info["db_password"], database=conf_info["db_name"], charset="utf-8")
		except Exception as ret:
			print(ret,"could not connect to mysql.")
			exit(1)
		else:
			# 初始化实例属性: mysql游标
			self.__mysql_update_cursor = self.mysql_update_obj.cursor()
		try:
			# 初始化实例属性: redis连接对象
			self.__redis_update_obj = StrictRedis(host=conf_info["redis_host"], port=conf_info["redis_port"], db=0, decode_responses=True, password=conf_info["redis_password"])
			self.__redis_get_obj = StrictRedis(host=conf_info["redis_host"], port=conf_info["redis_port"], db=0, decode_responses=True, password=conf_info["redis_password"])
		except Exception as ret:
			print(ret,"could not connect to redis.")
			exit(1)
		#self.__db_host = conf_info["db_host"]
		#self.__db_port = conf_info["db_port"]
		#self.__db_user = conf_info["db_user"]
		#self.__db_password = conf_info["db_password"]
		#self.__db_name = conf_info["db_name"]
		#self.__redis_host = conf_info["redis_host"]
		#self.__redis_port = conf_info["redis_port"]
		#self.__redis_password = conf_info["redis_password"]
		#self.__redis_db = 0


		frame = __import__(modu_name)
		app = getattr(frame, app_name)
		sys.path.append(conf_info["dynamic_path"])  # 添加模块查找路径
		wsgi_server = WSGIServer(port, app, conf_info["static_path"])
		wsgi_server.run_forever()



	def go():
		self.__get_config()

		update_process = multiprocessing.Process(target=update_mysql_and_redis_stat, args=(,))
		server_process = multiprocessing.Process(target=web_server, args=(,))
		update_process.start()
		server_process.start()




def main():
	# saas_service = SystemStatus(url="https://semm.zhizhangyi.com:3000/emm", service_name="SEMM", db_host="127.0.0.1", db_port=3306, db_user="kef", db_password="kef_ls50", db_name="system_status",
	#					   redis_host="127.0.0.1", redis_port=39328, redis_password="123456")
	# if saas_service.fetch_status == None:
	#saas_service.detect_status()
	# service.fetch_status
	saas_service = System_Monitor()
	saas_service.go()


if __name__ == "__main__":
	main()
