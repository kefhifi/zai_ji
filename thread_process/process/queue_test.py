import multiprocessing
import time


def download_data(q):
    data = [11, 22, 33, 44, 55, 66]  # 模拟下载数据
    for tmp in data:
        q.put(tmp)
    print("downloaded data")


def analysis_data(q):
    done_data = list()  # 也是定义一个空列表
    # done_data = []
    while True:
        data = q.get()
        done_data.append(data)
        if q.empty():
            break
    print(" %s ... done data" % str(done_data))


def main():
    q = multiprocessing.Queue(10)
    p1 = multiprocessing.Process(target=download_data, args=(q,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()
