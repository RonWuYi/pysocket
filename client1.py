import socket
import time
import urllib2

hh = socket.gethostname()

HOST = socket.gethostbyname(hh)
# HOST = 'daring.cwi.nl'
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    # s.connect((HOST, PORT))
    # Cdata = raw_input("please input a message: ")
    if time.localtime()[4] < 10:
        Cdata = str(time.localtime()[3]) + '0' + str(time.localtime()[4])
    else:
        Cdata = str(time.localtime()[3]) + str(time.localtime()[4])
    # s.sendall(str(time.localtime()[3]) + str(time.localtime()[4]))
    if Cdata == 'q' or Cdata == 'quit':
        break
    else:
        s.sendall(Cdata)
        data = s.recv(1024)
        # s.close()
        # print data
        # time.sleep(2)
        # if data[:3] == '76':
        #     break
        # else:
        print 'Received', repr(data)
# s.shutdown()
s.close()
# time.sleep(2)
# print 'Received', repr(data)