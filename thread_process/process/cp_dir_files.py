
import multiprocessing
import time
import os

# 单文件拷贝
file_name1 = "test/123.txt"
file_name2 = "test2/123.txt"
with open(file_name2, "wb") as file_obj2:
    with open(file_name1, "rb") as file_obj1:
        while True:
            file_data = file_obj1.read(1024)
            if file_data:
                file_obj2.write(file_data)
            else:
                break

# 多文件拷贝
def cp_file(file_name1, file_name2):
    with open(file_name2, "wb") as file_obj2:
        with open(file_name1, "rb") as file_obj1:
            while True:
                file_data = file_obj1.read(1024)
                if file_data:
                    file_obj2.write(file_data)
                else:
                    break


def main():
    list_file = os.listdir("test")

    p1 = multiprocessing.Process(target=cp_file, args=(file_name1, file_name2))
    pool2 = multiprocessing.Pool(10)
    p1.start()
    p2.start()





if __name__ == "__main__":
    main():

