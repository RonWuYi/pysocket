from random import randint

from socket import socket, AF_INET, SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)
s.connect(('192.168.0.119', 20000))
# s.connect(('10.131.86.100', 4000))
from threading import Thread
x = randint(100, 1000)
while x > 500:
    t = Thread(target=s.send(b'Hello' + bytes(x)))
    #s.send(b'Hello' + bytes(x))
    t.daemon = True
    t.start()
    #s.recv(8192)
    x-=1
# s.close()
