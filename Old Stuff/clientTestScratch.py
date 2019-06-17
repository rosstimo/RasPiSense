#https://pythonprogramming.net/sockets-tutorial-python-3/

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 42001

s.connect((host, port))
full_msg = ''
while True:
    msg = s.recv(1024)
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8")
if len(full_msg) > 0:
    print(full_msg)
s.close()
