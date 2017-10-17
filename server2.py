import socket
from threading import *
class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            a=str(self.sock.recv(1024123).decode("utf-8"))
            print a
            self.sock.send(a)

            #self.sock.send(b'Oi you sent something to me')

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 2505
print (host)
print (port)
serversocket.bind((host, port))

serversocket.listen(5)
print ('server started and listening')
while 1:
    clientsocket, address = serversocket.accept()
    #print "Connected client :",clientsocket,address
    client(clientsocket, address)