from socket import *
from time import ctime

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

udp_cli_sock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input('21 ')
    if not data:
        break
    udp_cli_sock.sendto(data, ADDR)
    data, ADDR = udp_cli_sock.recvfrom(BUFSIZE)
    if not data:
        break
    print(data, "12345")
udp_cli_sock.close()
