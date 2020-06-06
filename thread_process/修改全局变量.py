import threading
import time

g_num = 100


def test1():
    global g_num
    g_num += 1  # 这样用 必须用global声明
    time.sleep(1)
#    g_num_2 = g_num+1  # 像这样只是引用g_num ，则前面不需要global声明g_num  (和libi站点上7天学会python的讲解一样)
    time.sleep(1)


def test2():
    print("------test2---g_num = %d-----" % g_num)


def main():
    print("--------main----g_num = %d ---" % g_num)
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    t1.start()
    t2.start()
    print("--------main--end----g_num = %d ---" % g_num)

if __name__ == "__main__":
    main()




