import pygame

pygame.init()
largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))


def desenho_circulo(AZUL_def):
    pygame.draw.circle(tela, AZUL_def, (x, y), 100)


PRETO = (0, 0, 0)
AZUL = (0, 0, 225)
BRANCO = (225, 225, 225)
x = 400
y = 300
tela.fill(PRETO)
terminou = False
while not terminou:
    desenho_circulo(AZUL)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
    tela.fill(PRETO)
pygame.display.quit()
pygame.quit()
