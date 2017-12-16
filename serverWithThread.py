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
        # SPlay.TabQieHuan()
        if data == 'exit' or not data:
            break
        elif data == 'GuaJiFlag':
            sock.send(str(SPlay.GuaJiFlag))
        elif data == 'CurStatus':
            sock.send(SPlay.CurStatus)
        elif data == 'Complete':
            sock.send(SPlay.Complete)
        elif data == '937':
            print 'please do something'
            sock.send('useful message, will do something')
        elif data == '937':
            print 'please do something'
            sock.send('useful message, will do something')
        elif data == 'TFFM':
            sock.send('start TaFangJingYan')
            SPlay.TaFangFengMo()
        elif data == 'CLFB':
            sock.send('start cai liao fb')
            SPlay.CaiLiaoFuBen()
        elif data == 'GJ':
            sock.send('start gua ji')
            SPlay.GuaJi()
        elif data == 'SBGJ':
            sock.send('start SB gua ji')
            SPlay.ShuangBeiGuaJi()
            while not SPlay.GuaJiFlag:
                time.sleep(5)
                if SPlay.Complete == True:
                    break
        elif data == 'MBCJ':
            sock.send('start mo bai cheng zhu')
            SPlay.MoBaiChengZhu()
            while not SPlay.GuaJiFlag:
                time.sleep(5)
                if SPlay.Complete == True:
                    break
        elif data == 'HS':
            sock.send('start hui shou')
            SPlay.HuiShou()
            SPlay.GuaJi()
        elif data == 'YCBQ':
            sock.send('start hui shou')
            SPlay.HuiShou()
            SPlay.GuaJi()
        elif data == 'SWMY':
            sock.send('start hui shou')
            SPlay.HuiShou()
            SPlay.GuaJi()
        elif data == 'WorldBoss':
            sock.send('start hui shou')
            SPlay.HuiShou()
            SPlay.GuaJi()
        elif data == '':
            sock.send('start hui shou & gua ji')
            SPlay.HuiShou()
            SPlay.GuaJi()
        else:
            sock.send('useness data, do nothing')
            time.sleep(1)
            # SPlay.TaFangFengMo()
            # time.sleep(1)
            # SPlay.GongXunRenWu()
            # time.sleep(1)
            # SPlay.JingYingRenWu()
            # time.sleep(1)
            # SPlay.WeiWangRenWu()
            time.sleep(1)
            SPlay.CaiLiaoFuBen()
            # time.sleep(1)
            # SPlay.ChuMoRenWu()
            # time.sleep(1)
            # SPlay.ChuangTianGuan()
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
time.sleep(5)
SPlay.TabQieHuan()
while True:
    conn, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(conn, addr))
    t.start()