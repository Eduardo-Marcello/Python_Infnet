import pygame
from random import randint


def draw_random_squares(screen, rect_color, area):
    return pygame.draw.rect(screen, rect_color, area)


class Question_08:

    def _init_(self):
        pygame.init()
        self.width, self.height = 600, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.bgcolor = (255, 255, 255)
        self.text_color = (255, 255, 0)
        self.rect_color = (255, 255, 0)
        self.button_color = (0, 0, 0)
        self.finish = False
        self.rect_width, self.rect_height = 50, 50
        self.collided_rects = []
        self.circle_pos, self.circle_width = 300, 50
        self.circle_height = 50
        self.font = pygame.font.Font(None, 24)
        self.circle_caption = self.font.render("Clique", True, self.text_color)
        self.display_name = pygame.display.set_caption('Question 07')

    def draw_button(self):
        return pygame.draw.circle(self.screen, self.button_color, (self.circle_pos, self.circle_width),
                                  self.circle_height)

    def event(self):
        self.screen.fill(self.bgcolor)

        while not self.finish:
            self.screen.fill(self.bgcolor)
            for rect in self.collided_rects:
                rect = draw_random_squares(self.screen, self.rect_color, area)
            button = self.draw_button()
            self.screen.blit(self.circle_caption, (272, 40))
            x, y = randint(0, self.width), randint(0, self.height)
            area = pygame.Rect(x, y, self.rect_width, self.rect_height)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finish = True
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if button.collidepoint(pos):
                        square = draw_random_squares(self.screen, self.rect_color, area)
                        self.collided_rects.append(square)
                        print(self.collided_rects)

                        for r in self.collided_rects:
                            if r is not square and r.colliderect(square):
                                self.collided_rects.remove(r)
                                print("colidiu")
                                if square in self.collided_rects:
                                    self.collided_rects.remove(square)
                                    print("colidiu")
                            if r.colliderect(button):
                                self.collided_rects.remove(r)
                                print("colidiu")
                            if square.colliderect(button) and square in self.collided_rects:
                                self.collided_rects.remove(square)
                                print("colidiu")
                pygame.display.update()

        pygame.display.quit()
        pygame.quit()


Question_08().event()
