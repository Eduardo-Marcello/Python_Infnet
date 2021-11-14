import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORTA = 9001
MENSAGEM = "OI eu sou cliente do Eduardo"
try:
    s.connect(('192.168.1.3', PORTA))
    s.send(MENSAGEM.encode("utf-8"))

    info_bytes = s.recv(1024)
    print(info_bytes.decode('ascii'))

    s.close()
except Exception as erro:
    print(str(erro))
