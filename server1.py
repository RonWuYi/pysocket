import socket

HOST = ''
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
# s.listen(1)
# conn, addr = s.accept()
# print 'Connected by', addr

# def f(x):
#     return {
#         'a':1,
#         'b':2
#     }[x]

s.listen(5)
conn, addr = s.accept()

while 1:
    # s.listen(1)
    # conn, addr = s.accept()
    try:
        print 'Connected by', addr
        data = conn.recv(1024)
        # if not data:
        #     break
        # elif data == 'close':
        #     break
        if data == 'q' or data == 'quit':
            break
        else:
            print 'received ' + data + ' from client'
            conn.sendall(data + ' add server part')
            # print data
    except socket.error as ex:
        print ex
        # conn.shutdown()
        conn.close()
        s.listen(5)
        conn, addr = s.accept()
        print 'Connected by', addr
        continue

    except IOError as ex:
        print ex
        # conn.shutdown()
        # conn.close()
        # s.listen(5)
        # conn, addr = s.accept()
        conn.close()
        s.listen(5)
        conn, addr = s.accept()
        print 'Connected by', addr
        continue
        # conn.close()
        # s.listen(1)
        # conn, addr = s.accept()
        # while addr:
        #     continue
    # except IOError, e:
    #     if e.errno == error.EPIPE:
    #         pass
    #     else:
    #         pass
# conn.shutdown()
conn.close()