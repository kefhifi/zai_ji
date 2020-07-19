import redis
import pymysql
from urllib import request
import json

class SystemStatus():
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






def main():
	saas_service = SystemStatus(url="https://semm.zhizhangyi.com:3000/emm", service_name="SEMM", db_host="127.0.0.1", db_port=3306, db_user="kef", db_password="kef_ls50", db_name="system_status",
						   redis_host="127.0.0.1", redis_port=39328, redis_password="123456")
	# if saas_service.fetch_status == None:
	saas_service.detect_status()
	# service.fetch_status




if __name__ == "__main__":
	main()
