#Written By A.Z Dhebar Mail : azdhebar@gmail.com
import socket
from colorama import *
s = socket.socket()
s.settimeout(2)
print(Fore.GREEN+"Please Enter Web Address:\n")
target = raw_input(Fore.WHITE)

try:    
    s.connect((target,80))
    s.send('HEAD / HTTP\nHost:'+target+'\n\n')
    print(Fore.YELLOW)    
    print(s.recv(1024))
except:
    print(Fore.RED+"Web Address is Wrong or Offline")
    
s.close()
 
