import threading
import random
import time

gMoney = 0
gCondition = threading.Condition()
gTimes = 0


class Producer(threading.Thread):
    def run(self) -> None:
        global gMoney
        global gTimes
        while True:
            gCondition.acquire()
            if gTimes >= 10:
                gCondition.release()
                break
            money = random.randint(0, 100)
            gMoney += money
            gTimes += 1
            print("%s生产了%d元钱，剩余%d元钱"%(threading.current_thread().name,money,gMoney))
            gCondition.notify_all()
            gCondition.release()
            time.sleep(1)


class Consumer(threading.Thread):
    def run(self) -> None:
        global gMoney
        while True:
            gCondition.acquire()
            money = random.randint(0,100)
            while gMoney < money:
                if gTimes >= 10:
                    print("%s想消费%d元钱，但是余额只有%d元钱了，并且生产者已经不再生产了！"%(threading.current_thread().name,money,gMoney))
                    gCondition.release()
                    return
                print("%s想消费%d元钱，但是余额只有%d元钱了，消费失败！"%(threading.current_thread().name,money,gMoney))
                gCondition.wait()
            gMoney -= money
            print("%s消费了%d元钱，剩余%d元钱"%(threading.current_thread().name,money,gMoney))
            gCondition.release()
            time.sleep(1)


def main():
    for x in range(5):
        th = Producer(name="生产者%d号"%x)
        th.start()

    for x in range(5):
        th = Consumer(name="消费者%d号"%x)
        th.start()

if __name__ == '__main__':
    main()