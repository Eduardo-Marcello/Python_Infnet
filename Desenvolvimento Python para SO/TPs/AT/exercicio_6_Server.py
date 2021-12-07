import os
import socket
import pickle

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
porta = 9090

socket_servidor.bind((host, porta))
socket_servidor.listen()
print("Servidor de nome", host, "esperando conexão na porta", porta)
while True:
    (socket_cliente, addr) = socket_servidor.accept()
    print("Conectado a:", str(addr))
    msg = socket_cliente.recv(4069)
    dir = msg.decode('utf-8')
    if os.path.exists(dir):
        list = os.listdir(dir)
        list_arq = []
        for i in list:
            path = dir + str(i)
            if os.path.isfile(path):
                list_arq.append(i)
        socket_cliente.send(pickle.dumps(list_arq))
    else:
        msg = "The diretory doesn't exist."
        socket_cliente.send(msg.encode('utf-8'))
    socket_cliente.close()
socket_servidor.close()
