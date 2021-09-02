import pygame

pygame.init()
largula_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largula_tela, altura_tela))


def desenho_quadrado(VERMELHO_def):
    pygame.draw.rect(tela, VERMELHO_def, pygame.Rect(x - 50, y - 50, 100, 100))


PRETO = (0, 0, 0)
BRANCO = (225, 225, 225)
VERMELHO = (225, 0, 0)
x = 400
y = 300
tela.fill(PRETO)
terminou = False
while not terminou:
    desenho_quadrado(VERMELHO)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        if event.type == pygame.KEYDOWN:
            if event.key == ord('a'):
                x -= 4
            if event.key == ord('d'):
                x += 4
            if event.key == ord('w'):
                y -= 4
            if event.key == ord('s'):
                y += 4
    tela.fill(PRETO)

pygame.display.quit()
pygame.quit()
