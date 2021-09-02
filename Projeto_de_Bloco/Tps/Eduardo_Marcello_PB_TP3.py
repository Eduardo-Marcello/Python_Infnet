import pygame
import psutil
import cpuinfo


def mostra_uso_memoria():
    mem = psutil.virtual_memory()
    larg = largura_tela - 2 * 20
    pygame.draw.rect(tela, azul, (20, 520, larg, 70))
    larg = larg * mem.percent / 100
    pygame.draw.rect(tela, vermelho, (20, 520, larg, 70))
    total = round(mem.total / (1024 * 1024 * 1024), 2)
    texto_barra = "Uso de Memória (Total: " + str(total) + "GB):"
    text = font.render(texto_barra, 1, branco)
    tela.blit(text, (20, 500))


def mostra_uso_disco():
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
    tela.blit(text, (20, 460))


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


def mostra_uso_cpu(s, l_cpu_percent):
    s.fill(cinza)
    num_cpu = len(l_cpu_percent)
    x = y = 10
    desl = 10
    alt = (s.get_height() - 2 * y) / 3
    larg = (s.get_width() - 2 * y - (num_cpu + 1) * desl) / num_cpu
    d = x + desl
    for i in l_cpu_percent:
        pygame.draw.rect(s, vermelho, (d, y, larg, alt))
        pygame.draw.rect(s, azul, (d, y, larg, (1 - i / 100) * alt))
        d = d + larg + desl
    tela.blit(s, (0, altura_tela / 5))


info_cpu = cpuinfo.get_cpu_info()

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
        mostra_uso_cpu(s1, psutil.cpu_percent(interval=1, percpu=True))
        mostra_ip()
        mostra_uso_memoria()
        mostra_uso_disco()
        cont = 0

    pygame.display.update()

    clock.tick(60)
    cont = cont + 1

pygame.display.quit()
