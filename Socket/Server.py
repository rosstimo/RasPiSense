# Echo server program: https://docs.python.org/3.8/library/socket.html
import socket
import sys

class Server:

    def __init__(self, HOST = '127.0.0.1', PORT = 55055, addressFamily = 2, socketType = 1, protocol = 0):
        self.HOST = HOST
        self.PORT = PORT
        self.addressFamily = addressFamily
        self.socketType = socketType
        self.protocol = protocol
        self.socket=None
        self.Connect()
        if self.socket is not None:
            self.run(self.socket)

    @property
    def HOST(self):
        return self._HOST
    @HOST.setter
    def HOST(self, HOST):
        self._HOST = HOST

    @property
    def PORT(self):
        return self._PORT
    @PORT.setter
    def PORT(self, PORT):
        self._PORT = PORT

    @property
    def addressFamily(self):
        return self._addressFamily
    @addressFamily.setter
    def addressFamily(self, addressFamily):
        self._addressFamily = addressFamily

    @property
    def socketType(self):
        return self._socketType
    @socketType.setter
    def socketType(self, socketType):
        self._socketType = socketType

    @property
    def protocol(self):
        return self._protocol
    @protocol.setter
    def protocol(self, protocol):
        self._protocol = protocol

    @property
    def socket(self):
        return self._socket
    @socket.setter
    def socket(self, socket):
        self._socket = socket

    def SetDefaults(self):
        self.HOST = '127.0.0.1'
        self.PORT = 55055
        self.addressFamily = 2
        self.socketType = 1
        self.protocol = 0
        self.socket=None

    def ShowInfo(self):
        for info in socket.getaddrinfo(self.HOST, self.PORT, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
            addressFamily, socketType, protocol, connectionName, stuff = info
            #print(f'HOST: {self.HOST}')
            #print(f'PORT: {self.PORT}')
            print(f'Address Family: {addressFamily}')
            print(f'Socket Type: {socketType}')
            print(f'Protocol: {protocol}')
            print(f'Connection Name: {connectionName}')
            print(f'Additional {stuff}')

    def Connect(self):
        try:
            s = socket.socket(self.addressFamily, self.socketType, self.protocol)
            print(f'Connected to {self.HOST} on port {self.PORT}')
            try:
                s.bind((self.HOST, self.PORT))
                s.listen(1)
                print('Binding ok')
            except OSError as msg:
                s.close()
                s = None
                print(msg)
        except OSError as msg:
            s = None
            print(msg)

        if s is None:
            print('could not open socket')
        else:
            self.socket = s

    #@classmethod
    #def Start(cls, HOST, PORT):
    #    pass

    def run(self,socket):
        while True:
            conn, addr = socket.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)#TODO do something with query "data" maybe buffer???
                    if not data: break
                    conn.send(data)#TODO do something with returned "data" reply to each with th correct response

if __name__ == "__main__":
    thing = Server()