import socket
list = socket.getaddrinfo('localhost', 8080)

for thing in list:
    print(thing)

print(socket.gethostbyname(socket.gethostname()))