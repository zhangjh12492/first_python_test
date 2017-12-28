import threading
import time

exitFlag = 0


class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print("退出线程：" + self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("{0} : {1}".format(threadName, time.ctime(time.time())))
        counter -= 1


thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)


# 开启新线程

# thread1.join()
# thread2.join()


if __name__ == '__main__':
    thread1.start()
    thread2.start()
    time.sleep(2)
    print(threading.currentThread().getName())
    print(threading.enumerate())
    print(threading.activeCount())
    # print("退出主线程")