import socket
import time

HOST = ''
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

# def f(x):
#     return {
#         'a':1,
#         'b':2
#     }[x]

s.listen(5)
conn, addr = s.accept()

while 1:
    try:
        print 'Connected by', addr
        data = conn.recv(1024)
        if data == 'q' or data == 'quit':
            break
        else:
            print 'received ', repr(data)
            print ' from client', repr(addr)
            conn.sendall(data + ' add server part')

            conn.sendall(' ANOTHER DATA ')
    except socket.error as ex:
        print ex
        conn.close()
        s.listen(5)
        conn, addr = s.accept()
        print 'Connected by', addr
        continue
    # except IOError as ex:
    #     print ex
    #     conn.close()
    #     s.listen(5)
    #     conn, addr = s.accept()
    #     print 'Connected by', addr
    #     continue
    # finally:
    #     print 'from final'
    #     break
conn.close()