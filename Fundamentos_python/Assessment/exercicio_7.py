import pygame
from random import randint

pygame.init()
largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))

PRETO = (0, 0, 0)
AMARELO = (225, 225, 0)
BRANCO = (225, 225, 225)
tela.fill(PRETO)


def draw_rect(x_def, y_def, AMARELO_def, medida_def):
    pygame.draw.rect(tela, AMARELO_def, pygame.Rect(x_def, y_def, medida_def, medida_def))


terminou = False
while not terminou:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x = randint(0, largura_tela)
            y = randint(0, altura_tela)
            medida = 50
            draw_rect(x, y, AMARELO, medida)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                x = randint(0, largura_tela)
                y = randint(0, altura_tela)
                medida = 50
                draw_rect(x, y, AMARELO, medida)
        pygame.display.update()
        if event.type == pygame.QUIT:
            terminou = True
        pygame.display.update()

pygame.display.quit()
pygame.quit()
