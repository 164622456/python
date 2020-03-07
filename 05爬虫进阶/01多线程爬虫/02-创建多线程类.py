import time
import threading


# def coding():
#     the_thread = threading.current_thread()
#     print(the_thread.name)
#     for x in range(3):
#         print("%s正在写代码..." % the_thread.name)
#         time.sleep(1)
#
#
# def drawing():
#     the_thread = threading.current_thread()
#     # print(the_thread.name)
#     for x in range(3):
#         print("%s正在画图..." % the_thread.name)
#         time.sleep(1)
#
#
# def multi_thread():
#     th1 = threading.Thread(target=coding,name='小明')
#     th2 = threading.Thread(target=drawing,name='小红')
#
#     th1.start()
#     th2.start()
#
#     print(threading.enumerate())


# if __name__ == '__main__':
#     multi_thread()


# =========================================================

class CodingThread(threading.Thread):
    def run(self):
        the_thread = threading.current_thread()
        for x in range(3):
            print("%s正在写代码..." % the_thread.name)
            time.sleep(1)

class DrawingThread(threading.Thread):
    def run(self):
        the_thread = threading.current_thread()
        for x in range(3):
            print("%s正在画图..." % the_thread.name)
            time.sleep(1)

def multi_thread():
    th1 = CodingThread()
    th2 = DrawingThread()

    th1.start()
    th2.start()

if __name__ == '__main__':
    multi_thread()