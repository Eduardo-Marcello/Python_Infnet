import socket
import sys
import os
import time
import psutil
import platform
import subprocess
import nmap
import sched
import pygame
import pickle


def machineInfo():
    def mostra_uso_memoria():
        req = 'mem'
        s.send(req.encode('utf-8'))
        s_msg = s.recv(1000)
        mem = pickle.loads(s_msg)
        larg = largura_tela - 2 * 20
        pygame.draw.rect(tela, azul, (20, 520, larg, 70))
        larg = larg * mem.percent / 100
        pygame.draw.rect(tela, vermelho, (20, 520, larg, 70))
        total = round(mem.total / (1024 * 1024 * 1024), 2)
        texto_barra = "Uso de Memória (Total: " + str(total) + "GB):"
        text = font.render(texto_barra, 1, branco)
        tela.blit(text, (20, 500))

    def mostra_uso_disco():
        req = 'disk'
        s.send(req.encode('utf-8'))
        s_msg = s.recv(1000)
        disk = pickle.loads(s_msg)
        larg = largura_tela - 2 * 20
        pygame.draw.rect(tela, azul, (20, 660, larg, 70))
        larg = larg * disk.percent / 100
        pygame.draw.rect(tela, vermelho, (20, 660, larg, 70))
        total = round(disk.total / (1024 * 1024 * 1024), 2)
        texto_barra = "Uso de Disco: (Total: " + str(total) + "GB):"
        text = font.render(texto_barra, 1, branco)
        tela.blit(text, (20, 630))

    def mostra_ip():
        req = 'ip'
        s.send(req.encode('utf-8'))
        s_msg = s.recv(1000)
        ip = s_msg.decode('utf-8')
        text_barra = "IP: " + ip
        text = font.render(text_barra, 1, branco)
        tela.blit(text, (20, 460))

    def mostra_info_cpu():
        s1.fill(branco)
        mostra_texto(s1, "Nome:", "brand_raw", 10)
        mostra_texto(s1, "Arquitetura:", "arch", 30)
        mostra_texto(s1, "Palavra (bits):", "bits", 50)
        mostra_texto(s1, "Frequência (MHz):", "freq", 70)
        mostra_texto(s1, "Núcleos (físicos):", "nuc", 90)
        tela.blit(s1, (0, 0))

    def mostra_texto(s1_def, nome, chave, pos_y):
        text = font.render(nome, True, preto)
        s1_def.blit(text, (10, pos_y))
        req = chave
        if chave == "freq":
            s.send(req.encode('utf-8'))
            s_msg = s.recv(1000)
            cpu_info = s_msg.decode('utf-8')
        elif chave == "nuc":
            s.send(req.encode('utf-8'))
            s_msg = s.recv(1000)
            cpu_info = s_msg.decode('utf-8')
        else:
            s.send(req.encode('utf-8'))
            s_msg = s.recv(1000)
            cpu_info = s_msg.decode('utf-8')
        text = font.render(cpu_info, True, cinza)
        s1_def.blit(text, (160, pos_y))

    def mostra_uso_cpu(s1):
        s1.fill(cinza)
        req = 'cpu'
        s.send(req.encode('utf-8'))
        s_msg = s.recv(1000)
        l_cpu_percent = pickle.loads(s_msg)
        num_cpu = len(l_cpu_percent)
        x = y = 10
        desl = 10
        alt = (s1.get_height() - 2 * y) / 3
        larg = (s1.get_width() - 2 * y - (num_cpu + 1) * desl) / num_cpu
        d = x + desl
        for i in l_cpu_percent:
            pygame.draw.rect(s1, vermelho, (d, y, larg, alt))
            pygame.draw.rect(s1, azul, (d, y, larg, (1 - i / 100) * alt))
            d = d + larg + desl
        tela.blit(s1, (0, altura_tela / 5))

    preto = (0, 0, 0)
    branco = (255, 255, 255)
    cinza = (100, 100, 100)
    azul = (40, 40, 255)
    vermelho = (255, 0, 0)

    largura_tela = 1000
    altura_tela = 800
    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption("Informações de CPU")
    pygame.display.init()
    s1 = pygame.surface.Surface((largura_tela, altura_tela))

    pygame.font.init()
    font = pygame.font.Font(None, 24)

    clock = pygame.time.Clock()
    cont = 60

    terminou = False
    while not terminou:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminou = True

        if cont == 60:
            mostra_info_cpu()
            mostra_uso_cpu(s1)
            mostra_ip()
            mostra_uso_memoria()
            mostra_uso_disco()
            cont = 0

        pygame.display.update()

        clock.tick(60)
        cont = cont + 1

    pygame.display.quit()
    return 0


def dirAndFilesAndProcess():
    def show_files_directories(list_def):
        dic_files = {}
        dic_direct = {}
        for i in list_def:
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
        title = '{:11}'.format("Size")
        title = title + '{:27}'.format("Modification Date")
        title = title + '{:27}'.format("Creation Date")
        title = title + "Name"
        if len(dic_files) > 0:
            print(" ---Files---")
            print(title)
            for i in dic_files:
                kb = dic_files[i][0] / 1000
                size = '{:10}'.format(str('{:.2f}'.format(kb) + ' KB'))
                print(size, time.ctime(dic_files[i][2]), " ", time.ctime(dic_files[i][1]), " ", i)
            print(" ")
        if len(dic_direct) > 0:
            print(" ---Directories---")
            print(title)
            for i in dic_direct:
                kb = dic_direct[i][0] / 1000
                size = '{:10}'.format(str('{:.2f}'.format(kb) + ' KB'))
                print(size, time.ctime(dic_direct[i][2]), " ", time.ctime(dic_direct[i][1]), " ", i)
            print(" ")

    def show_info(pid):
        try:
            p = psutil.Process(pid)
            text = '{:6}'.format(pid)
            text = text + '{:11}'.format(p.num_threads())
            text = text + " " + time.ctime(p.create_time()) + " "
            text = text + '{:8.2f}'.format(p.cpu_times().user)
            text = text + '{:8.2f}'.format(p.cpu_times().system)
            text = text + '{:10.2f}'.format(p.memory_percent()) + " MB"
            rss = p.memory_info().rss / 1024 / 1024
            text = text + '{:10.2f}'.format(rss) + " MB"
            vms = p.memory_info().vms / 1024 / 1024
            text = text + '{:10.2f}'.format(vms) + " MB"
            text = text + " " + p.exe()
            print(text)
        except:
            pass

    def show_all_process(list_process):
        title = '{:^7}'.format("PID")
        title = title + '{:^11}'.format("# Threads")
        title = title + '{:^26}'.format("Creation")
        title = title + '{:^9}'.format("T. Usu.")
        title = title + '{:^9}'.format("T. Sis.")
        title = title + '{:^12}'.format("Mem. (%)")
        title = title + '{:^12}'.format("RSS")
        title = title + '{:^12}'.format("VMS")
        title = title + " Name"
        print(title)
        for i in list_process:
            show_info(i)

    def print_long_event(name):
        if name == 'first call':
            print('Calling:', time.ctime(), name)
            show_files_directories(list_files_direct)
            time.sleep(3)
            input("Press Enter to continue and show all process")
            print('First calling END:', time.ctime(), name)
        else:
            print('Calling:Linsting all Process...', time.ctime(), name)
            show_all_process(list_process)
            time.sleep(3)
            print('Second calling END:', time.ctime(), name)

    scheduler = sched.scheduler(time.time, time.sleep)
    list_files_direct = os.listdir()
    list_process = psutil.pids()
    now = time.time()
    print('Callings Start:', time.ctime(now))
    scheduler.enterabs(now + 2, 1, print_long_event, ('first call',))
    scheduler.enterabs(now + 4, 1, print_long_event, ('second call',))
    print('Callings END:', time.ctime(now))
    scheduler.run()
    input("Press Enter to come back to the menu...\n")


def ipsAndSub():
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

    def obter_hostnames(host_validos):
        nm = nmap.PortScanner()
        for i in host_validos:
            try:
                nm.scan(i)
                print(nm[i].hostname())
                for proto in nm[i].all_protocols():
                    print('----------')
                    print('Protocol : %s' % proto)

                    lport = nm[i][proto].keys()
                    # lport.sort()
                    for port in lport:
                        print('Port: %s\t State: %s' % (port, nm[i][proto][port]['state']))
            except:
                pass

    def verifica_hosts(base_ip):
        print("Mapping\r")
        host_validos = []
        return_codes = dict()
        for i in range(1, 255):
            return_codes[base_ip + '{0}'.format(i)] = retorna_codigo_ping(base_ip + '{0}'.format(i))
            if i % 20 == 0:
                print(".", end="")
            if return_codes[base_ip + '{0}'.format(i)] == 0:
                host_validos.append(base_ip + '{0}'.format(i))
        print("\nMapping ready...")
        return host_validos

    ip_string = input("Entre com o ip alvo: ")
    ip_lista = ip_string.split('.')
    base_ip = ".".join(ip_lista[0:3]) + '.'
    print("O teste sera feito com a base: ", base_ip)
    host_validos = verifica_hosts(base_ip)
    print("Os host válidos são: ", host_validos)
    obter_hostnames(host_validos)
    input("Press Enter to come back to the menu...")


def redesInfo():
    def interfacesInfo():
        interfaces = psutil.net_if_addrs()
        nomes = []
        for i in interfaces:
            nomes.append(str(i))
        for i in nomes:
            print(i + ":")
            for j in interfaces[i]:
                print("\t" + str(j))
        print("------------------------------------------------------------\n")
        status = psutil.net_if_stats()
        for i in nomes:
            print(i)
            print("\t" + str(status[i]))
        input("\nPress Enter to come back to the menu...")

    def interfacesStatus():
        io_status = psutil.net_io_counters(pernic=True)
        nomes = []
        for i in io_status:
            nomes.append(str(i))
        for j in nomes:
            print(j)
            print("\t" + str(io_status[j]))
        for i in range(4):
            time.sleep(1)
            io_status = psutil.net_io_counters(pernic=True)
            for j in nomes:
                print(j)
                print("\t" + str(io_status[j]))
        input("\nPress Enter to come back to the menu...")

    def process():
        def obtem_nome_familia(familia):
            if familia == socket.AF_INET:
                return "IPv4"
            elif familia == socket.AF_INET6:
                return "IPv6"
            elif familia == socket.AF_UNIX:
                return "Unix"
            else:
                return "-"

        def obtem_tipo_socket(tipo):
            if tipo == socket.SOCK_STREAM:
                return "TCP"
            elif tipo == socket.SOCK_DGRAM:
                return "UDP"
            elif tipo == socket.SOCK_RAW:
                return "IP"
            else:
                return "-"

        for i in psutil.pids():
            p = psutil.Process(i)
            conn = p.connections()
            if len(conn) > 0:
                if conn[0].status.ljust(13) != "ESTABLISHED  ":
                    endl = conn[0].laddr.ip.ljust(11)
                    portl = str(conn[0].laddr.port).ljust(5)
                    endr = conn[0].laddr.ip.ljust(13)
                    portr = str(conn[0].laddr.port).ljust(5)
                print(str(i).ljust(5),
                      " End.  Type   Status        Adress    Local   Port L.        Remote Adress  Port R.")
                print("      ", obtem_nome_familia(conn[0].family), " " + obtem_tipo_socket(conn[0].type),
                      "   " + conn[0].status.ljust(13), endl, portl, "  " + endr, "  " + portr)
                print(" ")
        input("\nPress Enter to come back to the menu...")

    def msgMenuProcess():
        print("Menu De Opções: \n"
              "[1] - Informações das Interfaces \n"
              "[2] - Status das Interfaces \n"
              "[3] - Dados dos Processos \n"
              "[9] - Voltar para o Menu Principal \n")
        return input("Digite a opção desejada: ")

    def menuProcess(optionp):
        if optionp == '1':
            interfacesInfo()
            return 1
        elif optionp == '2':
            interfacesStatus()
            return 1
        elif optionp == '3':
            process()
            return 1
        elif optionp == '9':
            return 0

    flag_process = 1
    while flag_process == 1:
        optionp = msgMenuProcess()
        flag_process = menuProcess(optionp)


def msgMenu():
    print("Menu Principal: \n"
          "[1] - Informações de Participação da Máquina \n"
          "[2] - Informações Referentes aos Diretórios e Arquivos \n"
          "[3] - Informações Referentes as Sub-Redes e suas Portas \n"
          "[4] - Informações Referentes a Rede \n"
          "[9] - Encerrar o programa \n")
    return input("Digite a opção desejada: ")


def menuPrincipal(option):
    if option == '1':
        controll = 1
        while controll == 1:
            controll = machineInfo()
        return 1
    elif option == '2':
        dirAndFilesAndProcess()
        return 1
    elif option == '3':
        ipsAndSub()
        return 1
    elif option == '4':
        redesInfo()
        return 1
    elif option == '9':
        msg = 'sair'
        s.send(msg.encode('utf-8'))
        return 0


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
flag = 1

try:
    # Tenta se conectar ao servidor
    s.connect(("192.168.1.9", 9999))
except Exception as erro:
    print(str(erro))
    sys.exit(1)  # Termina o programa

while flag == 1:
    option = msgMenu()
    flag = menuPrincipal(option)
print("Encerrando o Programa...")
s.close()