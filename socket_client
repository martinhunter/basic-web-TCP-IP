from socket import *

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

while True:
    tcp_cli_sock = socket(AF_INET, SOCK_STREAM)
    tcp_cli_sock.connect(ADDR)
    data = raw_input('>> ')
    if not data:
        break
    tcp_cli_sock.send('%s\r\n' %data)
    data = tcp_cli_sock.rec(BUFSIZE)
    if not data:
        break
    print(data.strip())
    tco_cli_sock.close()
    
