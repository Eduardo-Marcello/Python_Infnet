import socket

mysocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
mysocket.bind(('', 8888))

while True:
    pacote, dest = mysocket.recvfrom(1024)
    print(pacote.decode('utf-8'))
    mysocket.sendto('ACK'.encode('ascii'), dest)
mysocket.close()
