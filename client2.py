import socket
import time
import urllib2
import sys
#
# hh = socket.gethostname()
#
# HOST = socket.gethostbyname(hh)
BUF_SIZE = 1024
HOST = '192.168.184.129'
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
    if int(Cdata) == 1720:
        print 'start SBGJ'
        s.send('SBGJ')
    if int(Cdata) == 1705:
        print 'start SJBS'
        s.send('WorldBoss')
    elif Cdata == '7371':
        time.sleep(5)
        s.sendall(Cdata)
    else:
        time.sleep(10)
        s.sendall('Continue gua ji')
        # data = s.recv(1024)
        # print 'Received', repr(data)
s.close()