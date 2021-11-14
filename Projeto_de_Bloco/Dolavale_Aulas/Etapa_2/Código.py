import psutil
import pygame

# Iniciando a janela principal
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Uso de memória")
pygame.display.init()

azul = (0, 0, 255)
vermelho = (255, 0, 0)
preto = (0, 0, 0)
branco = (255, 255, 255)

pygame.font.init()
font = pygame.font.Font(None, 32)


# Mostar uso de memória
def mostra_uso_memoria():
    mem = psutil.virtual_memory()
    larg = largura_tela - 2 * 20
    tela.fill(preto)
    pygame.draw.rect(tela, azul, (20, 50, larg, 70))
    larg = larg * mem.percent / 100
    pygame.draw.rect(tela, vermelho, (20, 50, larg, 70))
    total = round(mem.total / (1024 * 1024 * 1024), 2)
    texto_barra = "Uso de Memória (Total: " + str(total) + "GB):"
    text = font.render(texto_barra, 1, branco)
    tela.blit(text, (20, 10))


def mostra_uso_cpu():
    capacidade = psutil.cpu_percent(interval=0)
    larg = largura_tela - 2 * 20
    # tela.fill(preto)
    pygame.draw.rect(tela, azul, (20, 250, larg, 70))
    larg = larg * capacidade / 100
    pygame.draw.rect(tela, vermelho, (20, 250, larg, 70))
    text = font.render("Uso de CPU:", 1, branco)
    tela.blit(text, (20, 210))


# Cria relógio
clock = pygame.time.Clock()

cont = 60

terminou = False
while not terminou:
    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
    if cont == 60:
        mostra_uso_memoria()
        mostra_uso_cpu()
        cont = 0

    # Atualiza o desenho na tela
    pygame.display.update()
    # 60 frames por segundo
    clock.tick(60)
    cont = cont + 1

# Finaliza a janela
pygame.display.quit()