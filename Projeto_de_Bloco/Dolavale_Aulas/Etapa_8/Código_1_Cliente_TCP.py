import socket
import sys

# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Tenta se conectar ao servidor
    s.connect(("192.168.0.104", 9999))
except Exception as erro:
    print(str(erro))
    sys.exit(1)  # Termina o programa
print("Digite 'sair' para encerrar: ")
msg = input()
# Envia mensagem codificada em bytes para o servidor
s.send(msg.encode('utf-8'))
while msg.lower() != 'sair':
    msg = s.recv(1024)
    print(msg.decode('utf-8'))
    msg = input()
    # Envia mensagem codificada em bytes para o servidor
    s.send(msg.encode('utf-8'))
# Fecha conexão com o servidor
s.close()
