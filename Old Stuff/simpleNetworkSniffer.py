import socket
# Example from https://docs.python.org/2/library/socket.html

# the public network interface
HOST = socket.gethostbyname(socket.gethostname())

# create a raw socket and bind it to the public interface
#windows TODO make this a try block to resolve
#s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

#Linux
s = socket.socket(socket.AF_UNIX, socket.SOCK_RAW, socket.IPPROTO_IP)
#s.bind((HOST, 0))
#s.bind(HOST)
s.bind('127.0.0.1')

# Include IP headers
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# receive all packages
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# receive a package
print(s.recvfrom(65565))

# disabled promiscuous mode
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
