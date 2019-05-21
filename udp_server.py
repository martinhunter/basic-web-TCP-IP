from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

udp_ser_sock = socket(AF_INET, SOCK_DGRAM)
udp_ser_sock.bind(ADDR)

while True:
    data, addr = udp_ser_sock.recvfrom(BUFSIZE)
    print("linked", addr)
    udp_ser_sock.sendto('[%s] %s' %(ctime(), data), addr)
udp_ser_sock.close()
