import psutil
import pygame

largura_tela = 900
altura_tela = 700
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Uso de memória")
pygame.display.init()

azul = (0, 0, 255)
vermelho = (255, 0, 0)
preto = (0, 0, 0)
branco = (255, 255, 255)

pygame.font.init()
font = pygame.font.Font(None, 32)

# Tentativa de usar surface
# s1 = pygame.surface.Surface((largura_tela, altura_tela/3))
# s2 = pygame.surface.Surface((largura_tela, altura_tela/3))
# s3 = pygame.surface.Surface((largura_tela, altura_tela/3))


def mostra_uso_memoria():
    mem = psutil.virtual_memory()
    larg = largura_tela - 2 * 20
    tela.fill(preto)
    pygame.draw.rect(tela, azul, (20, 50, larg, 70))
    # tela.blit(s1, (0, 0))
    larg = larg * mem.percent / 100
    pygame.draw.rect(tela, vermelho, (20, 50, larg, 70))
    total = round(mem.total / (1024 * 1024 * 1024), 2)
    texto_barra = "Uso de Memória (Total: " + str(total) + "GB):"
    text = font.render(texto_barra, 1, branco)
    tela.blit(text, (20, 10))


def mostra_uso_cpu():
    capacidade = psutil.cpu_percent(interval=0)
    larg = largura_tela - 2 * 20
    pygame.draw.rect(tela, azul, (20, 220, larg, 70))
    # tela.blit(s2, (0, altura_tela/3))
    larg = larg * capacidade / 100
    pygame.draw.rect(tela, vermelho, (20, 220, larg, 70))
    text = font.render("Uso de CPU:", 1, branco)
    tela.blit(text, (20, 180))


def mostra_uso_disco():
    disco = psutil.disk_usage('.')
    larg = largura_tela - 2 * 20
    pygame.draw.rect(tela, azul, (20, 390, larg, 70))
    # tela.blit(s3, (0, 2*altura_tela/3))
    larg = larg * disco.percent / 100
    pygame.draw.rect(tela, vermelho, (20, 390, larg, 70))
    total = round(disco.total / (1024 * 1024 * 1024), 2)
    texto_barra = "Uso de Disco: (Total: " + str(total) + "GB):"
    text = font.render(texto_barra, 1, branco)
    tela.blit(text, (20, 350))


def mostra_ip():
    dic_interfaces = psutil.net_if_addrs()
    text_barra = "IP: " + str(dic_interfaces['Ethernet'][0].address)
    text = font.render(text_barra, 1, branco)
    tela.blit(text, (20, 500))


clock = pygame.time.Clock()

cont = 60
terminou = False
while not terminou:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
    if cont == 60:
        mostra_uso_memoria()
        mostra_uso_disco()
        mostra_uso_cpu()
        mostra_ip()
        cont = 0
    pygame.display.update()
    clock.tick(60)
    cont = cont + 1
pygame.display.quit()
