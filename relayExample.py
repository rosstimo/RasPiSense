#example from https://stackoverflow.com/questions/5279641/need-help-creating-a-tcp-relay-between-two-sockets
import asyncore
import socket

class User(asyncore.dispatcher_with_send):

    def __init__(self, sock, server):
        asyncore.dispatcher_with_send.__init__(self, sock)
        self.server = server

    def handle_read(self):
        data = self.recv(4096)
        # parse User auth protocol here, authenticate, set phase flag, etc.
        # if authenticated, send data to server
        if self.server:
            self.server.send(data)

    def handle_close(self):
        if self.server:
            self.server.close()
        self.close()

class Listener(asyncore.dispatcher_with_send):

    def __init__(self, listener_addr, server):
        asyncore.dispatcher_with_send.__init__(self)
        self.server = server
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(listener_addr)
        self.listen(1)

    def handle_accept(self):
        conn, addr = self.accept()
        # this listener only accepts 1 client. while it is serving 1 client
        # it will reject all other clients.
        if not self.server.user:
            self.server.user = User(conn, self.server)
        else:
            conn.close()

class Server(asyncore.dispatcher_with_send):

    def __init__(self, server_addr, listener_addr):
        asyncore.dispatcher_with_send.__init__(self)
        self.server_addr = server_addr
        self.listener_addr = listener_addr
        self.listener = None
        self.user = None

    def start(self):
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect(self.server_addr)

    def handle_error(self, *n):
        self.close()

    def handle_read(self):
        data = self.recv(4096)
        # parse SomeServer auth protocol here, set phase flag, etc.
        if not self.listener:
            self.listener = Listener(self.listener_addr, self)
        # if user is attached, send data
        elif self.user:
            self.user.send(data)

    def handle_close(self):
        if self.user:
            self.user.server = None
            self.user.close()
            self.user = None
        if self.listener:
            self.listener.close()
            self.listener = None
        self.close()
        self.start()

if __name__ == '__main__':
    app = Server(('someserver', 143), ('localhost', 8080))
    app.start()
    asyncore.loop()
