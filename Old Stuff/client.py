#!/usr/bin/python2.7.16
#https://pythonprogramming.net/sockets-tutorial-python-3/

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 42002))


while True:
    full_msg = ''
    while True:
        msg = s.recv(8)
        if len(msg) <= 0:
            break
        full_msg += msg.decode("utf-8")

    if len(full_msg) > 0:
        print(full_msg)
