import socket
import sqlite3
import random
import subprocess
random.seed()
port=random.randint(1000,3000)
print port
uname=raw_input("Enter the username : ")
ans=raw_input("Press:\n1. New Room\n2. Join Room")
if ans=='1':
   process = subprocess.Popen('display.py', shell=True, stderr=subprocess.STDOUT)
#db.commit()
if ans=='2':
   process = subprocess.Popen('server2.py', shell=True, stderr=subprocess.STDOUT)
   

   '''host1="127.0.0.1"
   port1="2505"
   s1.connect((host1,port1))'''
a=raw_input('Waiting ...')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="127.0.0.1"
port =2503
s.connect((host,port))
def ts(s,str1):
   s.send(str1.encode()) 
   data = ''
   data = s.recv(1024).decode()
   #print (data)

while 2:
   r = raw_input()
   print "\033[A                             \033[A"
   r1=uname+" : "+r
   ts(s,r1)


s.close ()
