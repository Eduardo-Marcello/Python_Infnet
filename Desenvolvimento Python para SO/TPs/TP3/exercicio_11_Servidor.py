import socket
import os

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
porta = 9090

socket_servidor.bind((host, porta))
socket_servidor.listen()
print("Servidor de nome", host, "esperando conexão na porta", porta)
while True:
    (socket_cliente,addr) = socket_servidor.accept()
    print("Conectado a:", str(addr))
    msg = socket_cliente.recv(2048)
    nome_arq = msg.decode('ascii')
    if os.path.isfile(nome_arq):
        tamanho = os.stat(nome_arq).st_size
        socket_cliente.send(str(tamanho).encode('ascii'))
        arq = open(nome_arq, 'rb')
        bytes = arq.read(4096)
        while bytes:
            socket_cliente.send(bytes)
            bytes = arq.read(4096)
        arq.close()
    else:
        print("Não encontrou o arquivo")
        socket_cliente.send('-1'.encode('ascii'))
    socket_cliente.close()
print("Encerrando o servidor...")
socket_servidor.close()
