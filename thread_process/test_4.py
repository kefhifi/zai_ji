import time

print(type((2,)))   # tuple   加逗号就是元组
print(type((2)))  # int


a=(1,)
print(type(a))  # 输出 <class 'tuple'>

a=(1)
print(type(a))   # 输出 <class 'int'>


print(time.time())

import sys
print(sys.path)
