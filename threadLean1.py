import time
import random
import threading
from contextlib import contextmanager

# Thread-local state to stored information on locks already acquired
_local = threading.local()

@contextmanager
def acquire(*locks):
    # Sort locks by object identifier
    locks = sorted(locks, key=lambda x: id(x))

    # Make sure lock order of previously acquired locks is not violated
    acquired = getattr(_local,'acquired',[])
    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError('Lock Order Violation')

    # Acquire all of the locks
    acquired.extend(locks)
    _local.acquired = acquired

    try:
        for lock in locks:
            lock.acquire()
        yield
    finally:
        # Release locks in reverse order of acquisition
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks):]

x_lock=threading.Lock()
y_lock=threading.Lock()

def thread_1():
    while True:
        with acquire(x_lock, y_lock):
            print('Thread-1')


def thread_2():
    while True:
        with acquire(x_lock, y_lock):
            print('Thread-2')

while True:
    x = random.randint(1,2)
    if x==1:
        t1 =threading.Thread(target=thread_1)
        t1.daemon
        t1.start()
    else:
        t2 =threading.Thread(target=thread_2)
        t2.daemon
        t2.start()
    time.sleep(5)

#
# def philosopher(left, right):
#     while True:
#         with acquire(left, right):
#             print(threading.currentThread(), 'eating')
#
#
# NSTICS = 5
# chopsticks = [threading.Lock() for n in range(NSTICS)]
#
# for n in range(NSTICS):
#     t = threading.Thread(target=philosopher,
#                          args=(chopsticks[n], chopsticks[(n+1)%NSTICS]))
#     t.start()