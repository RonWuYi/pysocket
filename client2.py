import socket
import time
import urllib2
import sys
#
# hh = socket.gethostname()
#
# HOST = socket.gethostbyname(hh)
BUF_SIZE = 1024
HOST = '192.168.0.77'
PORT = 50007
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print "Creating socket failure: " + str(msg[0]) + " Message : " + msg[1]
    sys.exit()

s.connect((HOST, PORT))
while True:
    if time.localtime()[4] < 10:
        Cdata = str(time.localtime()[3]) + '0' + str(time.localtime()[4])
    else:
        Cdata = str(time.localtime()[3]) + str(time.localtime()[4])
    if Cdata == 'q' or Cdata == 'quit':
        break
    elif Cdata == '737':
        time.sleep(5)
        s.sendall(Cdata)
    else:
        time.sleep(3)
        s.sendall('Continue gua ji')
        # data = s.recv(1024)
        # print 'Received', repr(data)
s.close()