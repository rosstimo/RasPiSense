# Echo client program: https://docs.python.org/3.8/library/socket.html
import socket
import sys
import json 
#HOST = '192.168.0.249'    # The remote host
#PORT = 50007              # The same port as used by the server
HOST = '127.0.0.1'
PORT = 55055
s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    print(af, socktype, proto, canonname, sa)
    try:
        print('try stuff')
        s = socket.socket(af, socktype, proto)
        print('stuff happend')
    except OSError as msg:
        s = None
        print(msg)
        continue
    try:
        print('try connect')
        print(sa)
        s.connect(sa)
        print('seems ok')
        break
    except OSError as msg:
        s.close()
        s = None
        print(msg)
        continue
if s is None:
    print('could not open socket')
    sys.exit(1)

with s:
    x=json.dumps({"Name":123})
    s.send(bytes(x, 'utf-8') )

    #s.sendall(b'Hello, world')
    data = s.recv(1024)
print('Received', repr(data))
print(str(data, 'utf-8'))
test = res = json.loads(str(data, 'utf-8'))
print(test["Name"])