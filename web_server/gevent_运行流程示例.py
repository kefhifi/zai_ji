import gevent
import time

def f1(n):
    print("f1------")
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.1)

def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.1)


print("....1....")
gevent.spawn(f1, 5)
print("----------")
gevent.sleep(1)
print("....2....")
g2 = gevent.spawn(f2, 5)


g2.join()

"""
输出结果如下：
....1....
----------
f1------
<Greenlet at 0x14e39b8: f1(5)> 0
<Greenlet at 0x14e39b8: f1(5)> 1
<Greenlet at 0x14e39b8: f1(5)> 2
<Greenlet at 0x14e39b8: f1(5)> 3
<Greenlet at 0x14e39b8: f1(5)> 4
....2....
<Greenlet at 0x3370710: f2(5)> 0
<Greenlet at 0x3370710: f2(5)> 1
<Greenlet at 0x3370710: f2(5)> 2
<Greenlet at 0x3370710: f2(5)> 3
<Greenlet at 0x3370710: f2(5)> 4

"""