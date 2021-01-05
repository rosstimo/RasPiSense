# Echo server program: https://docs.python.org/3.8/library/socket.html
import socket
import sys

HOST = None               # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = None

#server was listening on IPV6 had to add debug outpub to see
'''
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
                              socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    af, socktype, proto, canonname, sa = res
'''   

res = socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE)
af, socktype, proto, canonname, sa = res[1]# TODO  ('0.0.0.0', 50007) (HOST, PORT)

af = 2
socktype = 1
proto = 0


print(f'HOST: {HOST}')
print(f'PORT: {PORT}')
print(f'Address Family: {af}')
print(f'Socket Type: {socktype}')
print(f'Protocol: {proto}')
print(f'Connection Name: {canonname}')
print(sa)

try:
    print('try stuff')
    s = socket.socket(af, socktype, proto)
    print('stuff happend')
except OSError as msg:
    s = None
    print(msg)
    #continue
try:
    print('try listen')
    s.bind(sa)
    s.listen(1)
    print('seems ok')
    print(sa)
except OSError as msg:
    s.close()
    s = None
    print(msg)
    #continue
#break
if s is None:
    print('could not open socket')
    sys.exit(1)
conn, addr = s.accept()
with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data: break
        conn.send(data)