import threading
import time


def test1(temp):
    temp.append(33)
    print("-----------test1---temp= %s -" % str(temp))


def test2(temp):
    print("-----------test2---temp= %s -" % str(temp))

g_nums = [11, 22]

def main():
    print("--------main----g_num = %s ---" % str(g_nums))
    t1 = threading.Thread(target=test1, args=(g_nums,))   # args 里面是一个元组
    t2 = threading.Thread(target=test2, args=(g_nums,))
    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)
    print("-----------main---temp= %s -" % str(g_nums))

if __name__ == "__main__":
    main()




