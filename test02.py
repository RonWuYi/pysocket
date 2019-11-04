
import binascii
from socket import socket, AF_INET, SOCK_STREAM
s = socket(AF_INET, SOCK_STREAM)
motion_code = "00fe"
msg = "c207{}0055667788".format(motion_code)
s.connect(('10.131.86.90', 1234))
# s.connect(('172.16.66.231', 1234))
s.send(binascii.a2b_hex(msg))
print(s.recv(1024))