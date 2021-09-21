import pygame
from random import randint

pygame.init()
largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))

PRETO = (0, 0, 0)
tela.fill(PRETO)


class Circle:
    def __init__(self):
        self.rad = 70
        self.x_circ = tela.get_width() / 2
        self.y_circ = tela.get_height() - 525
        self.area = (self.x_circ, self.y_circ)
        self.cor = (225, 225, 225)
        self.fonte = pygame.font.Font(None, 24)
        self.texto = self.fonte.render("Clique Aqui", 1, PRETO)

    def draw_circle(self, tela_def):
        return pygame.draw.circle(tela_def, self.cor, self.area, self.rad)

    def draw_text(self):
        tela.blit(self.texto, (self.x_circ - 45, self.y_circ - 10))


class Rect(pygame.Rect):
    def __init__(self):
        self.altura = 50
        self.largura = 50
        self.x_rct = randint(0, largura_tela)
        self.y_rct = randint(0, altura_tela)
        self.area = pygame.Rect(self.x_rct, self.y_rct, self.largura, self.altura)
        self.cor = (225, 225, 0)

    def draw_rect(self, tela_def):
        pygame.draw.rect(tela_def, self.cor, self.area)


list_rect = []
terminou = False
while not terminou:
    tela.fill(PRETO)
    for r in list_rect:
        r.draw_rect(tela)
    circle = Circle()
    circle.draw_circle(tela)
    circle.draw_text()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            if (circle.x_circ + circle.rad >= x >= circle.x_circ - circle.rad) and \
                    (circle.y_circ - circle.rad <= y <= circle.y_circ + circle.rad):
                rect = Rect()
                rect.draw_rect(tela)
                list_rect.append(rect)
                for rect_2 in list_rect:
                    if rect_2 is not rect and pygame.Rect.colliderect(rect_2.area, rect.area):
                        list_rect.remove(rect_2)
                        if rect in list_rect:
                            list_rect.remove(rect)
        if event.type == pygame.QUIT:
            terminou = True
        pygame.display.update()
pygame.display.quit()
pygame.quit()
