import time
import threading

def coding():
    for x in range(3):
        print("%d正在写代码..."%x)
        time.sleep(1)

def drawing():
    for x in range(3):
        print("%d正在画图..." % x)
        time.sleep(1)

def single_thread():
    coding()
    drawing()

def multi_thread():
    th1 = threading.Thread(target=coding)
    th2 = threading.Thread(target=drawing)

    th1.start()
    th2.start()


if __name__ == '__main__':
    # single_thread()
    multi_thread()