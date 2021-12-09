import socket

mysocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
mysocket.settimeout(0.0001)
dest = (socket.gethostname(), 8888)

user_input = input("Entre com o texto a ser enviado: ")
while user_input:
    mysocket.sendto(user_input.encode('utf-8'), dest)
    acknowledged = False
    # spam dest until they acknowledge me (sounds like my kids)
    while not acknowledged:
        try:
            ACK, address = mysocket.recvfrom(1024)
            acknowledged = True
        except socket.timeout:
            mysocket.sendto(user_input.encode('utf-8'), dest)
    print (ACK.decode('ascii'))
    user_input = input("Entre com o texto a ser enviado: ")
mysocket.close()
