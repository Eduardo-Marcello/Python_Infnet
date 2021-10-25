import pygame
import psutil
import cpuinfo
import time
import os


def mostra_uso_memoria(s2):
    s2.fill(cinza)
    mem = psutil.virtual_memory()
    # larg = s2.get_width() - 2 * 20
    larg = largura_tela - 2 * 20
    pygame.draw.rect(tela, azul, (20, 520, larg, 70))
    # larg = s2.get_width() * mem.percent / 100
    larg = larg * mem.percent / 100
    pygame.draw.rect(tela, vermelho, (20, 520, larg, 70))
    total = round(mem.total / (1024 * 1024 * 1024), 2)
    texto_barra = "Uso de Memória (Total: " + str(total) + "GB):"
    text = font.render(texto_barra, 1, branco)
    tela.blit(text, (20, 500))



def mostra_uso_disco(s3):
    s3.fill(cinza)
    disco = psutil.disk_usage('.')
    larg = largura_tela - 2 * 20
    pygame.draw.rect(tela, azul, (20, 660, larg, 70))
    larg = larg * disco.percent / 100
    pygame.draw.rect(tela, vermelho, (20, 660, larg, 70))
    total = round(disco.total / (1024 * 1024 * 1024), 2)
    texto_barra = "Uso de Disco: (Total: " + str(total) + "GB):"
    text = font.render(texto_barra, 1, branco)
    tela.blit(text, (20, 630))


def mostra_ip():
    dic_interfaces = psutil.net_if_addrs()
    text_barra = "IP: " + str(dic_interfaces['Ethernet'][0].address)
    text = font.render(text_barra, 1, branco)
    tela.blit(text, (20, 450))


def mostra_info_cpu():
    s1.fill(branco)
    mostra_texto(s1, "Nome:", "brand_raw", 10)
    mostra_texto(s1, "Arquitetura:", "arch", 30)
    mostra_texto(s1, "Palavra (bits):", "bits", 50)
    mostra_texto(s1, "Frequência (MHz):", "freq", 70)
    mostra_texto(s1, "Núcleos (físicos):", "nucleos", 90)
    tela.blit(s1, (0, 0))


def mostra_texto(s1_def, nome, chave, pos_y):
    text = font.render(nome, True, preto)
    s1_def.blit(text, (10, pos_y))
    if chave == "freq":
        s = str(round(psutil.cpu_freq().current, 2))
    elif chave == "nucleos":
        s = str(psutil.cpu_count())
        s = s + " (" + str(psutil.cpu_count(logical=False)) + ")"
    else:
        s = str(info_cpu[chave])
    text = font.render(s, True, cinza)
    s1_def.blit(text, (160, pos_y))


def mostra_uso_cpu(s1_def, l_cpu_percent):
    s1_def.fill(cinza)
    num_cpu = len(l_cpu_percent)
    x = y = 10
    desl = 10
    alt = (s1_def.get_height() - 2 * y)
    larg = (s1_def.get_width() - 2 * y - (num_cpu + 1) * desl) / num_cpu
    d = x + desl
    for i in l_cpu_percent:
        pygame.draw.rect(s1_def, vermelho, (d, y, larg, alt))
        pygame.draw.rect(s1_def, azul, (d, y, larg, (1 - i / 100) * alt))
        d = d + larg + desl
    tela.blit(s1_def, (0, altura_tela / 4))


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


info_cpu = cpuinfo.get_cpu_info()
list_files_direct = os.listdir()
list_process = psutil.pids()

preto = (0, 0, 0)
branco = (255, 255, 255)
cinza = (100, 100, 100)
azul = (40, 40, 255)
vermelho = (255, 0, 0)
amarelo = (255, 255, 0)
verde = (0, 230, 0)

largura_tela = 1000
altura_tela = 800

tela = pygame.display.set_mode((largura_tela, altura_tela))

s1 = pygame.surface.Surface((largura_tela, altura_tela/4))
s2 = pygame.surface.Surface((largura_tela, altura_tela/4))
s3 = pygame.surface.Surface((largura_tela, altura_tela/4))
s4 = pygame.surface.Surface((largura_tela, altura_tela/4))

pygame.display.set_caption("Informações de CPU")
pygame.display.init()


pygame.font.init()
font = pygame.font.Font(None, 24)

clock = pygame.time.Clock()
cont = 60

terminou = False
while not terminou:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
            show_files_directories(list_files_direct)
            show_all_process(list_process)

    if cont == 60:
        mostra_info_cpu()
        mostra_uso_cpu(s1, psutil.cpu_percent(interval=1, percpu=True))
        mostra_uso_memoria(s2)
        mostra_uso_disco(s3)
        mostra_ip()
        cont = 0

    pygame.display.update()

    clock.tick(60)
    cont = cont + 1

pygame.display.quit()
