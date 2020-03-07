
from queue import Queue
import random
import time
import threading

# q = Queue(4)
#
# for x in range(5):
#     try:
#         q.put(x, block=False)
#     except:
#         break
#
# if q.full():
#     print("满了")
#
# # print(q.qsize())
#
#
# for x in range(5):
#     try:
#         value = q.get(block=False)
#     except:
#         break
#     print(value)
#
# if q.empty():
#     print("空了")
#
# print("完成")




def add_value(q):
    while True:
        q.put(random.randint(0,10))
        time.sleep(1)


def get_value(q):
    while True:
        print("获取到的值：%d"%q.get())

def main():
    q = Queue(10)
    th1 = threading.Thread(target=add_value,args=[q])
    th2 = threading.Thread(target=get_value,args=[q])

    th1.start()
    th2.start()

if __name__ == '__main__':
    main()


