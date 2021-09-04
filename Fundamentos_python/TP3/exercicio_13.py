import pygame

pygame.init()
largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))


def desenho_circulo(VERDE_def, a_def, b_def, rad_def):
    pygame.draw.circle(tela, VERDE_def, (a_def, b_def), rad_def)


PRETO = (0, 0, 0)
VERDE = (0, 128, 0)
BRANCO = (225, 225, 225)
x = 400
y = 300
rad_circ = 100
tela.fill(PRETO)
terminou = False
a, b = x - rad_circ, y - rad_circ
direcao = 1
while not terminou:
    if a < x:
        a -= 1 * direcao
    if a == x:
        a -= 1 * direcao
    if a > x:
        a -= 1 * direcao
    if a == 0:
        direcao = -1
        a += 2
    if a == largura_tela:
        direcao = 1
        a -= 2
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
    tela.fill(PRETO)
    desenho_circulo(VERDE, a, b, rad_circ)
    pygame.display.update()
pygame.quit()
