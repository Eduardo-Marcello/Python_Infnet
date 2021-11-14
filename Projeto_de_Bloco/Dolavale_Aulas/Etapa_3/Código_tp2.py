import pygame
import psutil
import cpuinfo


# Mostra as informações de CPU escolhidas:
def mostra_info_cpu():
    s1.fill(branco)
    mostra_texto(s1, "Nome:", "brand_raw", 10)
    mostra_texto(s1, "Arquitetura:", "arch", 30)
    mostra_texto(s1, "Palavra (bits):", "bits", 50)
    mostra_texto(s1, "Frequência (MHz):", "freq", 70)
    mostra_texto(s1, "Núcleos (físicos):", "nucleos", 90)
    tela.blit(s1, (0, 0))


# Mostra texto de acordo com uma chave:
def mostra_texto(s1, nome, chave, pos_y):
    text = font.render(nome, True, preto)
    s1.blit(text, (10, pos_y))
    if chave == "freq":
        s = str(round(psutil.cpu_freq().current, 2))
    elif chave == "nucleos":
        s = str(psutil.cpu_count())
        s = s + " (" + str(psutil.cpu_count(logical=False)) + ")"
    else:
        s = str(info_cpu[chave])
    text = font.render(s, True, cinza)
    s1.blit(text, (160, pos_y))


def mostra_uso_cpu(s, l_cpu_percent):
    s.fill(cinza)
    num_cpu = len(l_cpu_percent)
    x = y = 10
    desl = 10
    alt = s.get_height() - 2 * y
    larg = (s.get_width() - 2 * y - (num_cpu + 1) * desl) / num_cpu
    d = x + desl
    for i in l_cpu_percent:
        pygame.draw.rect(s, vermelho, (d, y, larg, alt))
        pygame.draw.rect(s, azul, (d, y, larg, (1 - i / 100) * alt))
        d = d + larg + desl
    # parte mais abaixo da tela e à esquerda
    tela.blit(s, (0, altura_tela / 5))


# Obtém informações da CPU
info_cpu = cpuinfo.get_cpu_info()

# Cores:
preto = (0, 0, 0)
branco = (255, 255, 255)
cinza = (100, 100, 100)
azul = (40, 40, 255)
vermelho = (255, 0, 0)
amarelo = (255, 255, 0)
verde = (0, 230, 0)

# Iniciando a janela principal
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Informações de CPU")
pygame.display.init()
# Superfície para mostrar as informações:
s1 = pygame.surface.Surface((largura_tela, altura_tela))

# Para usar na fonte
pygame.font.init()
font = pygame.font.Font(None, 24)

# Cria relógio
clock = pygame.time.Clock()
# Contador de tempo
cont = 60

terminou = False
# Repetição para capturar eventos e atualizar tela
while not terminou:
    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

    # Fazer a atualização a cada segundo:
    if cont == 60:
        mostra_info_cpu()
        mostra_uso_cpu(s1, psutil.cpu_percent(interval=1, percpu=True))
        cont = 0

    # Atualiza o desenho na tela
    pygame.display.update()

    # 60 frames por segundo
    clock.tick(60)
    cont = cont + 1

# Finaliza a janela
pygame.display.quit()
