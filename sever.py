import socket

# s = socket.socket()
#
# host = socket.gethostname()
host = ''
port = 12345
s = socket.socket()
s.bind((host, port))

s.listen(5)
# while True:
c, addr = s.accept()
# if s.accept():
if addr:
    print 'connect from ', addr
    c.send('welcome')
    c.close()
else:
    print 'no connection'
    c.close()

