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
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        print 'received ' + repr(data) +  ' from client ' + repr(addr)
        if data == 'exit' or not data:
            break
        elif data == 'GuaJiFlag':
            sock.send(str(SPlay.GuaJiFlag))
        elif data == 'CurStatus':
            sock.send(SPlay.CurStatus)
        elif data == '937':
            print 'please do something'
            sock.send('useful message, will do something')
        else:
            sock.send('useness data, do nothing')
    sock.close()
    print 'Connection from %s:%s closed' % addr

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "socket created!"
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
print "socket Bind!"
s.listen(5)
print "socket listening!"

SPlay = AW()

while True:
    conn, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(conn, addr))
    t.start()