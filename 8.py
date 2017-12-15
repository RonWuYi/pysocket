import sys
import socket
import random

from AllWay import AW

HOST = ''
PORT = 50007
Running = True
BUF_SIZE = 1024

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print "socket failure : " + str(msg[0]) + " message: " + msg[1]

print "socket created!"
# re-use address
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    s.bind((HOST, PORT))
except socket.error, msg:
    print "Binding failure : " + str(msg[0]) + " message: " + msg[1]
    sys.exit()
print "socket Bind!"

s.listen(5)
print "socket listening!"
SPlay = AW()
while True:
    conn, addr = s.accept()
    print 'Connected by', repr(addr)
    while Running:
        try:
            data = conn.recv(1024)
            # if data == 'q' or data == 'quit':
            #     Running = False
            #     break
            if data == 'GuaJiFlag':
                conn.send(str(SPlay.GuaJiFlag))
            elif data == 'CurStatus':
                conn.send(SPlay.CurStatus)
            elif data == '937':
                print 'please do something'
            else:
                print 'received ', repr(data)
                print ' from client', repr(addr)
                conn.send('unuseness data')
        except socket.error, msg:
            print "Binding failure : " + str(msg[0]) + " message: " + msg[1]
            for i in msg:
                print i
            s.close()

            try:
                s.bind((HOST, PORT))
            except socket.error, msg:
                print "Binding failure again: " + str(msg[0]) + " message: " + msg[1]
                for i in msg:
                    print i
                sys.exit()
            print "socket Bind!"

            s.listen(5)
            print "socket listening!"

            conn, addr = s.accept()
            print 'Connected by', repr(addr)
            continue
    s.close()
# exc
    # finally:
    #     time.sleep(5)
    #     SPlay.GuaJi()
    #     time.sleep(3600)
    #
    #
    #
    #
    #
    # GuaJiFlag = True
    # SPlay.TabQieHuan()
    # # GuaJiFlag =False
    # time.sleep(1)
    # SPlay.JinYanGongXun()
    # time.sleep(1)
    # SPlay.TianFu()
    # time.sleep(1)
    # SPlay.TaFangJingYan()
    # SPlay.time.sleep(1)
    # SPlay.CaiLiaoFuBen()
    # time.sleep(1)
    # SPlay.ChuMoRenWu()
    # time.sleep(1)
    # SPlay.ChuangTianGuan()
    #
    # # while True:
    # #     if CTime == '110':
    # #         time.sleep(5)
    # #         JinYanGongXun()
    # #         time.sleep(5)
    # #         TianFu()
    # #         time.sleep(5)
    # #         TaFangJingYan()
    # #         time.sleep(5)
    # #         CaiLiaoFuBen()
    # #         time.sleep(5)
    # #         ChuMoRenWu()
    # #         time.sleep(5)
    # #         ChuangTianGuan()
    # #         time.sleep(5)
    # #         GuaJi()
    # #         time.sleep(3600)
    # #     else:
    # #         # time.sleep(3600)
    # #         time.sleep(5)
    # #         GuaJi()
    # #         time.sleep(3600)
    #     # GuaJi()
    #
    # time.sleep(5)
    # SPlay.GuaJi()
    # time.sleep(3600)