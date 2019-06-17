
#example from https://stackoverflow.com/questions/5279641/need-help-creating-a-tcp-relay-between-two-sockets
#adding a bunch of debug stuff
import asyncore
import socket

class User(asyncore.dispatcher_with_send):

    def __init__(self, sock, server):
        print('user __init__')
        asyncore.dispatcher_with_send.__init__(self, sock)
        self.server = server
        

    def handle_read(self):
        print('handle_read')
        data = self.recv(4096)
        # parse User auth protocol here, authenticate, set phase flag, etc.
        # if authenticated, send data to server
        if self.server:
            self.server.send(data)
            print ('User: ' + data.decode("utf-8"))
        else:
            print( 'in handle read but not self.server')
            print( 'data = '  + data.decode("utf-8"))

    def handle_close(self):
        print('handle_close')
        if self.server:
            self.server.close()
        self.close()
        

class Listener(asyncore.dispatcher_with_send):
    #TODO accept from multiple clients and ports
    #create relay funnel to scratch
    def __init__(self, listener_addr, server):
        print('Listener __init__')
        asyncore.dispatcher_with_send.__init__(self)
        self.server = server
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(listener_addr)
        self.listen(1)
        print( 'listener __init__  listener_addr = ' + listener_addr[0])

    def handle_accept(self):
        print('handle_accept')
        conn, addr = self.accept()
        # this listener only accepts 1 client. while it is serving 1 client
        # it will reject all other clients.
        if not self.server.user:
            self.server.user = User(conn, self.server)
            print( 'self.server.user')
        else:
            print ('Not self.server.listenter')
            conn.close()

class Server(asyncore.dispatcher_with_send):

    def __init__(self, server_addr, listener_addr):
        print('Server __init__')
        asyncore.dispatcher_with_send.__init__(self)
        self.server_addr = server_addr
        self.listener_addr = listener_addr
        self.listener = None
        self.user = None
        print('Server __init__ listener_addr = ' + listener_addr[0]   + 'server_addr = ' + server_addr[0])

    def start(self):
        print('start')
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect(self.server_addr)
        print('start')
        
    def handle_error(self, *n):
        print('error handled')
        print(n)
        #self.close()
        

    def handle_read(self):
        print('handle_read')
        data = self.recv(4096)
        # parse SomeServer auth protocol here, set phase flag, etc.
        if not self.listener:
            self.listener = Listener(self.listener_addr, self)
        # if user is attached, send data
        elif self.user:
            self.user.send(data)
            print ('Server: ' + data.decode("utf-8"))

    def handle_close(self):
        print('handle_close')
        if self.user:
            self.user.server = None
            self.user.close()
            self.user = None
            print( 'self.user closed')
        if self.listener:
            self.listener.close()
            self.listener = None
            print ('self.listener closed')
        self.close()
        self.start()

if __name__ == '__main__':
    app = Server(('127.0.0.1', 42001), ('localhost',42002))
    print 'hello'
    app.start()
    asyncore.loop()
