import socket
import time

hh = socket.gethostname()

HOST = socket.gethostbyname(hh)
# HOST = 'daring.cwi.nl'
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    # s.connect((HOST, PORT))
    s.sendall(str(time.localtime()[3]) + str(time.localtime()[4]))
    data = s.recv(1024)
    # s.close()
    print data
    time.sleep(2)
    if data[:3] == '444':
        break
s.close()
time.sleep(2)
# print 'Received', repr(data)