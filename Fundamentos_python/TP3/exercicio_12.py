import pygame

pygame.init()
largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))


def desenho_circulo(AMARELO_def, a_def, b_def, rad_def):
    pygame.draw.circle(tela, AMARELO_def, (a_def, b_def), rad_def)


PRETO = (0, 0, 0)
AMARELO = (225, 225, 0)
BRANCO = (225, 225, 225)
x = 400
y = 300
rad_circ = 100
tela.fill(PRETO)
terminou = False
a, b = x , y 
direcao = 1
while not terminou:
    if a == largura_tela:
        a = 0
    if a == 0:
        a = largura_tela
    if b == altura_tela:
        b = 0
    if b == 0:
        b = altura_tela
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        if event.type == pygame.KEYDOWN:
            if event.key == ord('a'):
                a -= 4
            if event.key == ord('d'):
                a += 4
            if event.key == ord('w'):
                b -= 4
            if event.key == ord('s'):
                b += 4
    tela.fill(PRETO)
    desenho_circulo(AMARELO, a, b, rad_circ)
    pygame.display.update()
pygame.quit()
