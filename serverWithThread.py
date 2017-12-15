import sys
import socket
import time
import threading

from AllWay import AW

HOST = ''
PORT = 50007
Running = True
BUF_SIZE = 1024

def tcplink(sock, addr):
    print 'Accept new connection from %s:%s...' %addr
    sock.send('Welcome!')
    while True:
        # try:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            # Running = False
            break
        elif data == 'GuaJiFlag':
            sock.send(str(SPlay.GuaJiFlag))
        elif data == 'CurStatus':
            sock.send(SPlay.CurStatus)
        elif data == '937':
            print 'please do something'
            sock.send('useful message')
        else:
            print 'received ', repr(data)
            print ' from client', repr(addr)
            sock.send('unuseness data')
        # except socket.error, msg:
        #     print "Binding failure : " + str(msg[0]) + " message: " + msg[1]
        #     for i in msg:
        #         print i
        #     s.close()
        #
        #     try:
        #         s.bind((HOST, PORT))
        #     except socket.error, msg:
        #         print "Binding failure again: " + str(msg[0]) + " message: " + msg[1]
        #         for i in msg:
        #             print i
        #         sys.exit()
        #     print "socket Bind!"
        #
        #     s.listen(5)
        #     print "socket listening!"
        #
        #     conn, addr = s.accept()
        #     print 'Connected by', repr(addr)
        #     continue
    sock.close()
    print 'Connection from %s:%s closed' % addr

# try:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# except socket.error, msg:
#     print "socket failure : " + str(msg[0]) + " message: " + msg[1]
print "socket created!"
# re-use address
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# try:
s.bind((HOST, PORT))
# except socket.error, msg:
#     print "Binding failure : " + str(msg[0]) + " message: " + msg[1]
#     sys.exit()
print "socket Bind!"

s.listen(5)
print "socket listening!"
SPlay = AW()
while True:
    conn, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(conn, addr))
    t.start()