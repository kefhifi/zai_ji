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


a = [1, 2, 3, 4, 5, 6]
b = [i * i for i in a ]
print(b)

def squ(i):
    return i**3

print(list(map(squ, a)))


