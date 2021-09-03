import pygame

pygame.init()
largula_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largula_tela, altura_tela))


def desenho_estrela(BRANCO_def, x_def, y_def):
    pygame.draw.polygon(tela, BRANCO_def, [[x_def - 50, y_def], [x_def, y_def - 131], [x_def + 40, y_def],
                                           [x_def + 206, y_def - 7], [x_def + 42, y_def + 68],
                                           [x_def + 91, y_def + 195], [x_def - 15, y_def + 101],
                                           [x_def - 121, y_def + 187], [x_def - 72, y_def + 60],
                                           [x_def - 186, y_def - 5]], 0)


x = 400
y = 300
PRETO = (0, 0, 0)
BRANCO = (225, 225, 225)
tela.fill(PRETO)
terminou = False
while not terminou:
    desenho_estrela(BRANCO, x, y)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            desenho_estrela(BRANCO, x, y)
        if event.type == pygame.QUIT:
            terminou = True
    tela.fill(PRETO)

pygame.display.quit()
pygame.quit()
