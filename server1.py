import socket

HOST = ''
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
# s.listen(1)
# conn, addr = s.accept()
# print 'Connected by', addr

def f(x):
    return {
        'a':1,
        'b':2
    }[x]

while 1:
    s.listen(1)
    conn, addr = s.accept()
    print 'Connected by', addr
    data = conn.recv(1024)
    # if not data:
    #     break
    # elif data == 'close':
    #     break
    if data == 'close':
        break
    else:
        conn.sendall(data + ' add server part')
        print data

conn.close()