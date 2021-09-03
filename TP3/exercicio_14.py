import pygame

pygame.init()
largula_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largula_tela, altura_tela))


def desenho_quadrado(VERMELHO_def, x_def, y_def):
    pygame.draw.rect(tela, VERMELHO_def, pygame.Rect(x_def - 50, y_def - 50, 50, 50))


PRETO = (0, 0, 0)
BRANCO = (225, 225, 225)
VERMELHO = (225, 0, 0)
x = 400
y = 300
tela.fill(PRETO)
terminou = False
while not terminou:
    desenho_quadrado(VERMELHO, x, y)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            desenho_quadrado(VERMELHO, x, y)
    tela.fill(PRETO)

pygame.display.quit()
pygame.quit()
