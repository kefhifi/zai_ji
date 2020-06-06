import threading
import time

g_num = 0


def test1(temp):
    global g_num
    for i in range(temp):
        mutex.acquire()
        g_num += 1  # 这样用 必须用global声明
        mutex.release()
    print("--------test1----g_num = %d ---" % g_num)


def test2(temp):
    global g_num
    for i in range(temp):
        mutex.acquire()
        g_num += 1  # 这样用 必须用global声明
        mutex.release()
    print("--------test2----g_num = %d ---" % g_num)

mutex = threading.Lock()

def main():
    t1 = threading.Thread(target=test1, args=(100000,))
    t2 = threading.Thread(target=test2, args=(100000,))
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()




