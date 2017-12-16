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
        print 'start ri chang ri wu'
        pass
    elif int(Cdata) > 1001 and int(Cdata) < 1005:
        # jin zhu shong li
        print 'jin zhu shong li'
        pass

    elif int(Cdata) > 1031 and int(Cdata) < 1040:
        # shen wei
        print 'shen wei'
        pass

    elif int(Cdata) > 1101 and int(Cdata) < 1259:
        # gua ji
        print 'gua ji'
        pass

    elif int(Cdata) > 1301 and int(Cdata) < 1310:
        # suo yao ta
        print 'suo yao ta'
        pass

    elif int(Cdata) > 1401 and int(Cdata) < 1434:
        # gua ji
        print 'gua ji'
        pass

    elif int(Cdata) > 1435 and int(Cdata) < 1440:
        # bi guan
        print 'bi guan'
        pass

    elif int(Cdata) > 1455 and int(Cdata) < 1730:
        # gua ji
        print 'gua ji'
        pass

    elif int(Cdata) > 1731 and int(Cdata) < 1740:
        # mo bai cheng zhu
        print 'mo bai cheng zhu'
        pass

    elif int(Cdata) > 1905 and int(Cdata) < 1910:
        # shi jie boss
        print 'shi jie boss'
        pass

    elif int(Cdata) > 1930 and int(Cdata) < 1950:
        # bi qi
        print 'bi qi'
        pass

    # Cdata = raw_input('please in put data: ')
    # if Cdata == 'q' or Cdata == 'quit':
    #
    #     BoolFlag = False
    #     break
    else:
        print 'gua ji'
        s.send(Cdata)
        data = s.recv(1024)
        print 'Received', repr(data)
s.close()