import pygame

pygame.init()
largula_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largula_tela, altura_tela))

def desenho_estrela(BRANCO):
    pygame.draw.polygon(tela, BRANCO, [[360, 300], [400, 169], [440, 300], [606, 293], [442, 368],
                                       [491, 495], [385, 401], [279, 487], [328, 360], [214, 295]], 0)


PRETO = (0, 0, 0)
BRANCO = (225, 225, 225)
tela.fill(PRETO)
terminou = False
while not terminou:
    desenho_estrela(BRANCO)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
    tela.fill(PRETO)

pygame.display.quit()
pygame.quit()
