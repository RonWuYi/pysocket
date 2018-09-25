import time

def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -=1
        time.sleep(5)

if __name__ == '__main__':
    from threading import Thread
    t = Thread(target=countdown, args=(10,))
    t.start()
    if t.is_alive():
        print('running')
    else:
        print('completed')
