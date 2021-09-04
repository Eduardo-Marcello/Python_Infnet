import pygame

pygame.init()
largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
LARANJA = (255, 165, 0)
x = 400
y = 300
tela.fill((147, 100, 225))
terminou = False
while not terminou:
    pygame.draw.line(tela, PRETO, (x - 50, y - 10), (x - 140, y - 30), 5)
    pygame.draw.line(tela, PRETO, (x + 50, y - 10), (x + 140, y - 30), 5)
    pygame.draw.circle(tela, BRANCO, (x, y - 75), 35)
    pygame.draw.circle(tela, BRANCO, (x, y + 100), 85)
    pygame.draw.circle(tela, BRANCO, (x, y), 60)
    pygame.draw.circle(tela, PRETO, (x, y), 9)
    pygame.draw.circle(tela, PRETO, (x, y + 35), 9)
    pygame.draw.circle(tela, PRETO, (x, y - 35), 9)
    pygame.draw.circle(tela, PRETO, (x - 13, y - 85), 4)
    pygame.draw.circle(tela, PRETO, (x + 13, y - 85), 4)
    pygame.draw.polygon(tela, LARANJA, [[x, (y - 69)-5], [x-15, (y - 80)+5], [x, y - 80]], 0)
    pygame.draw.circle(tela, PRETO, (x, y - 61), 3)
    pygame.draw.circle(tela, PRETO, (x + 10, y - 63), 3)
    pygame.draw.circle(tela, PRETO, (x - 10, y - 63), 3)
    pygame.draw.circle(tela, PRETO, (x + 20, y - 67), 3)
    pygame.draw.circle(tela, PRETO, (x - 20, y - 67), 3)
    pygame.draw.rect(tela, PRETO, pygame.Rect(x - 25, y - 160, 50, 60))
    pygame.draw.rect(tela, PRETO, pygame.Rect(x - 50, y - 115, 101, 20))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        if event.type == pygame.KEYDOWN:
            if event.key == ord('a'):
                x -= 3
            if event.key == ord('d'):
                x += 3
            if event.key == ord('w'):
                y -= 3
            if event.key == ord('s'):
                y += 3
    tela.fill((147, 100, 225))
pygame.display.quit()
pygame.quit()
