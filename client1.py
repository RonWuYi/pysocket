import socket
import time
import urllib2

hh = socket.gethostname()

HOST = socket.gethostbyname(hh)
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    if time.localtime()[4] < 10:
        Cdata = str(time.localtime()[3]) + '0' + str(time.localtime()[4])
    else:
        Cdata = str(time.localtime()[3]) + str(time.localtime()[4])
    if Cdata == 'q' or Cdata == 'quit':
        break
    else:
        s.sendall(Cdata)
        data = s.recv(1024)
        print 'Received', repr(data)
s.close()