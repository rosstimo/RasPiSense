#this work see https://en.scratch-wiki.info/wiki/Communicating_to_Scratch_via_Python
# programming in Python
import socket # for socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Socket successfully created"
except socket.error as err:
    print "socket creation failed with error %s" %(err)

# default port for socket
port = 42001

while True:
    try:
        host_ip = socket.gethostbyname(socket.gethostname())
        print('the host name is: ' + host_ip)
        print('the port is: ' + str(port))
        # connecting to the server
        s.connect((host_ip, port))
        dummy = 'sensor-update "dummy" 99'
        #the next two line pad the begining of dummy with 3 byte of 0x00h
        n = len(dummy)
        b = (chr((n >> 24) & 0xFF)) + (chr((n >> 16) & 0xFF)) + (chr((n >> 8) & 0xFF)) + (chr(n & 0xFF))
        print('sending: ' + str(n) + dummy)
        s.send(b + dummy)
        print "the socket has successfully connected to scratch on port == %s" %(host_ip)
        s.close()
    except socket.gaierror:

        # this means could not resolve the host
        print "there was an error resolving the host"
        sys.exit()
        
    except socket.error as e:
        print('it looks like the server doesn\'t want to talk')
        print(e)
        break
        
        

        
    

