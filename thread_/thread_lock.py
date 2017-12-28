import threading
import time


class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开启线程：" + self.name)
        # 获得锁，用于线程同步
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # 释放锁， 开启下一个线程
        threadLock.release()


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("{0}: {1} ".format(threadName, time.ctime(time.time())))
        counter -= 1


threadLock = threading.Lock()
threads = []

# 开启新线程
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "thread-2", 2)

thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")
