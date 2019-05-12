
# programming in Python
import socket # for socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Socket successfully created"
except socket.error as err:
    print "socket creation failed with error %s" %(err)

#TODO this will be usefull when in a function that uses 
'''
try:
    host_ip = socket.gethostbyname('127.0.0.1')
    print host_ip
except socket.gaierror:

    # this means could not resolve the host
    print "there was an error resolving the host"
    sys.exit()
'''
# default host and port TODO funftion that returns tuple
host = '127.0.0.1'
port = 42001

try:
    #connecting to the server
    s.connect((host, port))
    print "the socket has successfully connected to scratch on port == %s" %(host)
    while True:
        print s.recv(32)
    
except socket.error as err:
    print "socket connection failed with error %s" %(err)
    print err.errno
    
    


