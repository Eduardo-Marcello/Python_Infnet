import socket
import sys
import os


# Imprime o status de download
def imprime_status(bytes, tam):
    kbytes = bytes/1024
    tam_bytes = tam/1024
    texto = 'Baixando... '
    texto = texto + '{:<.2f}'.format(kbytes) + ' KB '
    texto = texto + 'de ' + '{:<.2f}'.format(tam_bytes) + ' KB'
    print(texto)


# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

nome_arq = input('Entre com o nome do arquivo: ')

# D:\Users\Eduardo\VSC-Programms\Python\Infnet\Focalor.png
# D:\Users\Eduardo\Downloads\Diego's-World.png
try:
    # Tenta se conectar ao servidor
    s.connect((socket.gethostname(), 9090))
    # Envia o nome do arquivo:
    s.send(nome_arq.encode('ascii'))
    # Recebe o tamanho do arquivo:
    msg = s.recv(12)
    tamanho = int(msg.decode('ascii'))
    # Checa se o arquivo existe no servidor:
    if tamanho >= 0:
        # Gera o arquivo na pasta local
        nome_arq = os.path.basename(nome_arq)
        print(nome_arq)
        arq = open(nome_arq, "wb")
        soma = 0
        bytes = s.recv(4096)
        # Escreve o arquivo
        while bytes:
            arq.write(bytes)
            # Impressão do status de download
            soma = soma + len(bytes)
            os.system('cls')
            imprime_status(soma, tamanho)
            bytes = s.recv(4096)
        # Fecha o arquivo
        arq.close()
    else:
        print('Arquivo não encontrado no servidor!')
except Exception as erro:
    print(str(erro))
    sys.exit(1)
# Fecha o socket
s.close()
input("Pressione qualquer tecla para sair...")
