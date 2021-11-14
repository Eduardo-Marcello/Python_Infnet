import socket
import random

s_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

s_servidor.bind((host, port))
s_servidor.listen()
print(f"Servidor de nome {host} esperando conexão na porta {port}")
(s_cliente, addr) = s_servidor.accept()
print(f"Conexão estabelecida com:  {str(addr)}")
while True:
    msg = s_cliente.recv(1024)
    if 'sair' == msg.decode('utf-8').lower:
        print(f"Fechando conexão com:  {str(addr)} ...")
        s_cliente.close()
        break
    elif '?' in msg.decode('utf-8'):
        resp = random.randint(0,1)
        msg = 'Sim\n'
        if resp == 0:
            msg == 'Não\n'
    else:
        msg = "Ok..." + msg.decode('utf-8')
    s_cliente.send(msg.encode('utf-8'))
s_servidor.close()
print("Pressione qualquer tecla para sair...")
