import psutil
import cpuinfo
import os
import subprocess
import platform
import nmap
import socket
import pickle


def options():
    if 'sair' in list_msg:
        print("Encerrando o servidor...")
        return 0
    elif '1' in list_msg:
        machineInfo()
        return 1
    elif '2' in list_msg:
        Files_DirectoriesAndProcess()
        return 1
    elif '3' in list_msg:
        ipAndSub()
        return 1
    elif '4' in list_msg:
        redesInfo()
        return 1


def machineInfo():
    if 'mem' in list_msg:
        mem = psutil.virtual_memory()
        bytes = pickle.dumps(mem)
        s_cliente.send(bytes)
    elif 'disk' in list_msg:
        disk = psutil.disk_usage('.')
        bytes = pickle.dumps(disk)
        s_cliente.send(bytes)
    elif 'ip' in list_msg:
        dic_interfaces = psutil.net_if_addrs()
        ip = str(dic_interfaces['Ethernet'][0].address)
        s_cliente.send(ip.encode('utf-8'))
    elif 'freq' in list_msg:
        freq = str(round(psutil.cpu_freq().current, 2))
        s_cliente.send(freq.encode('utf-8'))
    elif 'nuc' in list_msg:
        nuc = str(psutil.cpu_count())
        nuc = nuc + " (" + str(psutil.cpu_count(logical=False)) + ")"
        s_cliente.send(nuc.encode('utf-8'))
    elif 'brand_raw' in list_msg:
        info_cpu = cpuinfo.get_cpu_info()
        brand_raw = str(info_cpu[list_msg[1]])
        s_cliente.send(brand_raw.encode('utf-8'))
    elif 'arch' in list_msg:
        print(list_msg[1])
        info_cpu = cpuinfo.get_cpu_info()
        arch = str(info_cpu[list_msg[1]])
        s_cliente.send(arch.encode('utf-8'))
    elif 'bits' in list_msg:
        info_cpu = cpuinfo.get_cpu_info()
        bits = str(info_cpu[list_msg[1]])
        s_cliente.send(bits.encode('utf-8'))
    elif 'cpu' in list_msg:
        cpu = psutil.cpu_percent(interval=1, percpu=True)
        bytes = pickle.dumps(cpu)
        s_cliente.send(bytes)


def Files_DirectoriesAndProcess():
    if 'files' in list_msg:
        filesAndDirectories = os.listdir()
        dic_files = {}
        dic_direct = {}
        for i in filesAndDirectories:
            if os.path.isfile(i):
                dic_files[i] = []
                dic_files[i].append(os.stat(i).st_size)
                dic_files[i].append(os.stat(i).st_atime)
                dic_files[i].append(os.stat(i).st_mtime)
            else:
                dic_direct[i] = []
                dic_direct[i].append(os.stat(i).st_size)
                dic_direct[i].append(os.stat(i).st_atime)
                dic_direct[i].append(os.stat(i).st_mtime)
        list_bytes = []
        list_bytes.append(dic_files)
        list_bytes.append(dic_direct)
        bytes = pickle.dumps(list_bytes)
        s_cliente.send(bytes)
    elif 'process' in list_msg:
        process = psutil.pids()
        bytes = pickle.dumps(process)
        s_cliente.send(bytes)


def ipAndSub():
    def retorna_codigo_ping(hostname):
        plataform = platform.system()
        args = []
        if plataform == "Windows":
            args = ["ping", "-n", "1", "-l", "1", "-w", "100", hostname]
        else:
            args = ['ping', '-c', '1', '-W', '1', hostname]
        ret_cod = subprocess.call(args,
                                  stdout=open(os.devnull, 'w'),
                                  stderr=open(os.devnull, 'w'))
        return ret_cod

    if 'nmap' in list_msg:
        nm = nmap.PortScanner()
        s_cliente.send(pickle.dumps(nm))
    elif type(list_msg[1]) == str:
        print("Mapping IP\r")
        host_validos = []
        return_codes = dict()
        for i in range(1, 255):
            return_codes[list_msg[1] + '{0}'.format(i)] = retorna_codigo_ping(list_msg[1] + '{0}'.format(i))
            if i % 20 == 0:
                print(".", end="")
            if return_codes[list_msg[1] + '{0}'.format(i)] == 0:
                host_validos.append(list_msg[1] + '{0}'.format(i))
        print("\nMapping ready...")
        s_cliente.send(pickle.dumps(host_validos))


def redesInfo():
    if 'interfaces1' in list_msg:
        inter = psutil.net_if_addrs()
        s_cliente.send(pickle.dumps(inter))
    elif 'interfaces2' in list_msg:
        status = psutil.net_if_stats()
        s_cliente.send(pickle.dumps(status))
    elif 'statusFace' in list_msg:
        io_status = psutil.net_io_counters(pernic=True)
        s_cliente.send(pickle.dumps(io_status))
    elif 'process1' in list_msg:
        pids = psutil.pids()
        s_cliente.send(pickle.dumps(pids))
    elif 'process2' in list_msg:
        p = psutil.Process(list_msg[2])
        conn = p.connections()
        s_cliente.send(pickle.dumps(conn))


s_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

s_servidor.bind((host, port))
s_servidor.listen()
print(f"Servidor de nome {host} esperando conexão na porta {port}")
(s_cliente, addr) = s_servidor.accept()
print(f"Conexão estabelecida com:  {str(addr)}")
while True:
    msg = s_cliente.recv(4096)
    list_msg = pickle.loads(msg)
    flag = options()
    if flag != 1:
        s_cliente.close()
        break
s_servidor.close()
