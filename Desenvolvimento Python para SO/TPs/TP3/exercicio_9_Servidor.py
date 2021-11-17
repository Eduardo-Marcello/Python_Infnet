import socket
import pickle
import psutil

host = ''
port = 9991
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (host, port)

udp.bind(orig)
print(f"Esperando receber na porta {port} ...")
while True:
    (msg, cliente) = udp.recvfrom(1024)
    if 'sair' == msg.decode('utf-8').lower():
        print(f"Fechando conexão com:  {str(cliente)} ...")
        cliente.close()
        break
    elif '?' in msg.decode('utf-8'):
        if 'disco' in msg.decode('utf-8'):
            msg = []
            mem = psutil.virtual_memory()
            msg.append(round(mem.total / (1024 * 1024 * 1024), 2))
            msg.append(round(mem.used / (1024 * 1024 * 1024), 2))
            mem_disp = (mem.total - mem.used) / (1024 * 1024 * 1024)
            msg.append(round(mem_disp, 2))
            mem_percent = (mem.used/mem.total) / (1024 * 1024 * 1024)
            msg.append(round(mem_percent, 2))
    else:
        msg = "Desculpe, não entendi o seu pedido...tente novamente!"
    bytes_msg = pickle.dumps(msg)
    udp.sendto(bytes_msg, cliente)
print("Pressione qualquer tecla para sair...")
udp.close()
