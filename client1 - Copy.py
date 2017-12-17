import socket
import time

HOST = '192.168.184.129'
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
BoolFlag = True

while BoolFlag:

    if time.localtime()[4] < 10:
        Cdata = str(time.localtime()[3]) + '0' + str(time.localtime()[4])
    else:
        Cdata = str(time.localtime()[3]) + str(time.localtime()[4])

    if int(Cdata) > 101 and int(Cdata) < 121:
        # ri chang ren wu
        print 'Client send TFFM'
        s.send('TFFM')
        time.sleep(1600)

    if int(Cdata) > 151 and int(Cdata) < 215:
        # ri chang ren wu
        print 'Client send GXRW'
        s.send('GXRW')
        time.sleep(1280)

    if int(Cdata) > 220 and int(Cdata) < 310:
        # ri chang ren wu
        print 'Client send JYRW'
        s.send('JYRW')
        time.sleep(2500)

    if int(Cdata) > 345 and int(Cdata) < 430:
        # ri chang ren wu
        print 'Client send CLFB'
        s.send('CLFB')
        time.sleep(1800)


    elif int(Cdata) > 1001 and int(Cdata) < 1005:
        # jin zhu shong li
        print 'Client send jin zhu shong li'
        # pass
        s.send('JZSL')

    elif int(Cdata) > 1031 and int(Cdata) < 1040:
        # shen wei
        print 'Client send shen wei'
        s.send('SW')
        time.sleep(100)

    elif int(Cdata) > 1101 and int(Cdata) < 1259:
        # gua ji
        print 'Client send gua ji'
        s.send('GJ')

    elif int(Cdata) > 1301 and int(Cdata) < 1310:
        # suo yao ta
        print 'Client send suo yao ta'
        s.send('SYT')

    elif int(Cdata) > 1401 and int(Cdata) < 1434:
        # gua ji
        print 'Client send gua ji'
        s.send('GJ')

    elif int(Cdata) > 1435 and int(Cdata) < 1440:
        # bi guan
        print 'Client send bi guan'
        s.send('BJ')

    elif int(Cdata) > 1455 and int(Cdata) < 1730:
        # gua ji
        print 'Client send gua ji'
        s.send('GJ')
        time.sleep(600)
        time.sleep(480)

    elif int(Cdata) > 1731 and int(Cdata) < 1740:
        # mo bai cheng zhu
        print 'Client send mo bai cheng zhu'
        s.send('MB')

    elif int(Cdata) > 1905 and int(Cdata) < 1910:
        # shi jie boss
        print 'Client send shi jie boss'
        s.send('SJBS')
        time.sleep(120)

    elif int(Cdata) > 1930 and int(Cdata) < 1950:
        # bi qi
        print 'Client send bi qi'
        s.send('BQ')
        time.sleep(1200)
    else:
        print 'Client send gua ji'
        s.send('GJ')
        data = s.recv(1024)
        print 'Received', repr(data)
        # time.sleep(3600)
s.close()