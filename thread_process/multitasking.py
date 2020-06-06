import time
import threading

def sing():
    for i in range(5):
        print("....singing....")
        time.sleep(1)


def dance():
    for i in range(5):
        print("....dancing....")
        time.sleep(1)


def main():
    t1 = threading.Thread(target=sing)  # 函数名，不带括号
    t2 = threading.Thread(target=dance)  # 函数名，不带括号
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()
