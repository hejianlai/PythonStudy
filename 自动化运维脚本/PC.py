import socket
myname = socket.getfqdn(socket.gethostname())
myadder = socket.gethostbyname(myname)
print(myname)
print(myadder)