import psutil
import cpuinfo
import socket
import pickle


def options():
    if 'sair' in msg.decode('utf-8'):
        print("Encerrando o servidor...")
        return 0
    elif 'mem' in msg.decode('utf-8'):
        mem = psutil.virtual_memory()
        bytes = pickle.dumps(mem)
        s_cliente.send(bytes)
        return 1
    elif 'disk' in msg.decode('utf-8'):
        disk = psutil.disk_usage('.')
        bytes = pickle.dumps(disk)
        s_cliente.send(bytes)
        return 1
    elif 'ip' in msg.decode('utf-8'):
        dic_interfaces = psutil.net_if_addrs()
        ip = str(dic_interfaces['Ethernet'][0].address)
        s_cliente.send(ip.encode('utf-8'))
        return 1
    elif 'freq' in msg.decode('utf-8'):
        freq = str(round(psutil.cpu_freq().current, 2))
        s_cliente.send(freq.encode('utf-8'))
        return 1
    elif 'nuc' in msg.decode('utf-8'):
        nuc = str(psutil.cpu_count())
        nuc = nuc + " (" + str(psutil.cpu_count(logical=False)) + ")"
        s_cliente.send(nuc.encode('utf-8'))
        return 1
    elif 'brand_raw' in msg.decode('utf-8'):
        info_cpu = cpuinfo.get_cpu_info()
        brand_raw = str(info_cpu[msg.decode('utf-8')])
        s_cliente.send(brand_raw.encode('utf-8'))
        return 1
    elif 'arch' in msg.decode('utf-8'):
        info_cpu = cpuinfo.get_cpu_info()
        arch = str(info_cpu[msg.decode('utf-8')])
        s_cliente.send(arch.encode('utf-8'))
        return 1
    elif 'bits' in msg.decode('utf-8'):
        info_cpu = cpuinfo.get_cpu_info()
        bits = str(info_cpu[msg.decode('utf-8')])
        s_cliente.send(bits.encode('utf-8'))
        return 1
    elif 'cpu' in msg.decode('utf-8'):
        cpu = psutil.cpu_percent(interval=1, percpu=True)
        bytes = pickle.dumps(cpu)
        s_cliente.send(bytes)
        return 1


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
    flag = options()
    if flag != 1:
       s_cliente.close()
       break
s_servidor.close()
