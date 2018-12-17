import time
import threading

class c(threading.Thread):
    def __init__(self, n):
        threading.Thread.__init__(self)
        self.n = n
    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -=1
            time.sleep(5)

class b(threading.Thread):
    def __init__(self, n):
        threading.Thread.__init__(self)
        self.n = n
    def run(self):
        while self.n > 0:
            print('B-minus', self.n)
            self.n -=1
            time.sleep(5)

if __name__ == '__main__':
    # import threading
    # import time
    #
    # exitFlag = 0


    # class myThread(threading.Thread):
    #     def __init__(self, threadID, name, counter):
    #         threading.Thread.__init__(self)
    #         self.threadID = threadID
    #         self.name = name
    #         self.counter = counter
    #
    #     def run(self):
    #         print "Starting " + self.name
    #         print_time(self.name, self.counter, 5)
    #         print "Exiting " + self.name
    #
    #
    # def print_time(threadName, dely, counter):
    #     while counter:
    #         if exitFlag:
    #             (threading.Thread).exit()
    #         time.sleep(dely)
    #         print "%s: %s" % (threadName, time.ctime(time.time()))
    #         counter -= 1
    #
    #
    # thread1 = myThread(1, "Thread-1", 1)
    # thread2 = myThread(2, "Thread-2", 2)
    #
    # thread1.start()
    # thread2.start()
    #
    # print "Exiting Main Thread"
    test = c(9)
    # t = myThread(target=test.countdown(), args=(10,))
    test1 = b(7)
    # t2 = myThread(target=test1.countdown(), args=(8,))
    test.start()
    test1.start()
    # if t.is_alive():
    #     print('running')
    # else:
    #     print('completed')
