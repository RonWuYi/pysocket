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
        print 'Server received ' + repr(data) +  ' from client ' + repr(addr)
        if data == 'exit' or not data:
            break
        elif data == 'TFFM':
            sock.send('Server start TFFM')
            time.sleep(1)
            SPlay.TaFangFengMo()
        elif data == 'GXRW':
            sock.send('Server start GXRW')
            time.sleep(1)
            SPlay.GongXunRenWu()
        elif data == 'JYRW':
            sock.send('Server start JYRW')
            time.sleep(1)
            SPlay.JingYingRenWu()
        elif data == 'CLFB':
            sock.send('Server start CLFB')
            time.sleep(1)
            SPlay.CaiLiaoFuBen()
        # elif data == 'GXRW':
        #     sock.send('server start GXRW')
        #     # time.sleep(1)
        #     # SPlay.ChuMoRenWu()
        # elif data == 'GXRW':
        #     sock.send('server start GXRW')
        #     time.sleep(1)
        #     SPlay.ChuangTianGuan()
        #     while True:
        #          if SPlay.Complete == True:
        #              break
        #     continue
        elif data == 'JZSL':
            sock.send('Server start JinZhuSongLi')
            SPlay.JinZhuSongLi()
            while True:
                 if SPlay.Complete == True:
                     break
            continue
        elif data == 'SWMY':
            sock.send('Server start shen wei')
            SPlay.ShenWei()
            while True:
                 if SPlay.Complete == True:
                     break
            continue
        elif data == 'SYT':
            sock.send('Server start suo yao ta')
            SPlay.WorldBoss()
            while True:
                 if SPlay.Complete == True:
                     break
            continue
        elif data == 'BJ':
            sock.send('Server start bi guan')
            SPlay.WorldBoss()
            time.sleep(126)
            while True:
                 if SPlay.Complete == True:
                     break
            continue
        elif data == 'MB':
            sock.send('Server start MoBaiChengZhu')
            SPlay.MoBaiChengZhu()
            while True:
                 if SPlay.Complete == True:
                     break
            continue
        elif data == 'SJBS':
            sock.send('Server start WorldBoss')
            SPlay.WorldBoss()
            while True:
                 if SPlay.Complete == True:
                     break
            continue
        elif data == 'BQ':
            sock.send('Server start YeZhanBiQi')
            SPlay.YeZhanBiQi()
            while True:
                 if SPlay.Complete == True:
                     break
            continue
        elif data == 'GJ':
            if SPlay.GuaJiFlag == False:
                sock.send('start gua ji')
                SPlay.GuaJi()
                time.sleep(240)
            else:
                sock.send('keep the sam status')
                time.sleep(240)
        # elif data == 'SBGJ':
        #     sock.send('start SB gua ji')
        #     SPlay.ShuangBeiGuaJi()
        #     while not SPlay.GuaJiFlag:
        #         time.sleep(5)
        #         if SPlay.Complete == True:
        #             break
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
        elif data == 'WorldBoss':
            sock.send('Server start shi jie boss')
            SPlay.WorldBoss()
        elif data == '':
            if SPlay.GuaJiFlag == False:
                sock.send('Server start gua ji')
                SPlay.HuiShou()
                SPlay.GuaJi()
                time.sleep(240)
            else:
                sock.send('keep the sam status')
                time.sleep(240)
        else:
            if SPlay.GuaJiFlag == False:
                sock.send('Server start gua ji')
                SPlay.HuiShou()
                SPlay.GuaJi()
                time.sleep(240)
            else:
                sock.send('keep the sam status')
                time.sleep(240)



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