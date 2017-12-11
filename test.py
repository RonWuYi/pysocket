import socket

hh = socket.gethostname()

h = socket.gethostbyname(hh)

print h