import threading, queue, os

class Worker(threading.Thread):
    def __init__(self, work_queue, number):
        super().__init__()
        self.work_queue = work_queue
        self.number = number

    def process(self, elemt):
        print("\n{0} task: --------{1}".format(self.number, elemt))

    def run(self):
        while True:
            try:
                elemt = self.work_queue.get()
                self.process(elemt)
            finally:
                self.work_queue.task_done()

def main(inargs):
    work_queue = queue.Queue()

    for i in range(3):
        worker = Worker(work_queue, i)
        worker.daemon = True
        worker.start()
    for elemt in inargs:
        work_queue.put(elemt)
    work_queue.join()

# From https://blog.csdn.net/weixin_33897722/article/details/92427243
if __name__ == '__main__':
    main(os.listdir("."))

