import socket
PORTA = 9001

# Cria o socket
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname("")
socket_servidor.bind((host, PORTA))

socket_servidor.listen()

print("Servidor de nome", host, "esperando conexão na porta", PORTA)

while True:
    (socket_cliente,addr) = socket_servidor.accept()
    print("Conectado a:", str(addr))
    msg_do_cliente = socket_cliente.recv(1024)
    msg_do_cliente = msg_do_cliente.decode('utf-8')
    print(msg_do_cliente)
    socket_cliente.send("Oi, eu sou o servidor".encode('utf-8'))
    socket_cliente.close()
