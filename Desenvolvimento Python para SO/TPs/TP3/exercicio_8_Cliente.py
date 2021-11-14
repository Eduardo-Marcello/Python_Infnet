import socket
import pickle
import time

host = socket.gethostname()  # Endereço ip do servidor
port = 9991  # Porta que o servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (host, port)

print("Digite 'sair' para encerrar: ")
msg = input("Mensagem: ")
udp.sendto(msg.encode('utf-8'), dest)
while msg.lower() != 'sair':
    (msg, server) = udp.recvfrom(1024)
    if list != 0:
        print('\n{:>6}'.format('%Total') + '{:>6}'.format('%Used') + '{:>6}'.format('%Free'))
        list = pickle.loads(msg)
        print(list)
        time.sleep(4)
    print("Digite 'sair' para encerrar a conexão")
    msg = input("Mensagem: ")
    print("")
    udp.sendto(msg.encode('utf-8'), dest)
udp.close()
