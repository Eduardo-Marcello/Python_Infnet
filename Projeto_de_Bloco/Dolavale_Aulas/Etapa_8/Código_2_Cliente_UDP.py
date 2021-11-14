import socket

host = socket.gethostname()  # Endereço ip do servidor
port = 9999  # Porta que o servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (host, port)

print("Digite 'sair' para encerrar: ")
msg = input("Mensagem: ")
udp.sendto(msg.encode('utf-8'), dest)
while msg.lower() != 'sair':
    (msg, servidor) = udp.recvfrom(1024)
    print(servidor, msg.decode('utf-8'))
    print("Digite 'sair' para encerrar a conexão")
    msg = input("Mensagem: ")
    print("")
    udp.sendto(msg.encode('utf-8'), dest)
udp.close()
