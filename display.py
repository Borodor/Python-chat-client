lst=list()
import socket
from threading import *
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class client(Thread):
    def __init__(self, socket, address,s2):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.s1=s2
        self.start()

    def run(self):
        
        
        while 1:
            host ="127.0.0.1"
            port =2505
            a=str(self.sock.recv(1024123).decode("utf-8"))
            print a
            #print "s1:",self.s1
            self.sock.send(a)
            
            '''if f==1:
                s.send(a) '''
            
            try:
                self.s1.connect((host,port))
                
                #self.s1.send(a)
            except:
                pass
            try:
                self.s1.send(a)
            except:
                pass
            #self.sock.send(b'Oi you sent something to me')

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 2503
print (host)
print (port)
serversocket.bind((host, port))
serversocket.listen(5)
print ('server started and listening')
while 1:
    
    clientsocket, address = serversocket.accept()
    lst.append(clientsocket)
    #print "Connected client :",clientsocket,address
    client(clientsocket, address,s)
