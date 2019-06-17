import socket
import sys


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Socket successfully created"
except socket.error as err:
    print "socket creation failed with error %s" %(err)

# default host and port TODO funftion that returns tuple
host = '127.0.0.1'
port = 42002

try:
    #connecting to the server
    s.connect((host, port))
    print "the socket has successfully connected to scratch on port == %s" %(host)
    while True:
        full_msg = ''
        msg = s.recv(1024)
        full_msg += msg.decode("utf-8")
        if len(full_msg) > 0:
            print(full_msg)
except socket.error as err:
    print "socket connection failed with error %s" %(err)
    print err.errno
    
    


