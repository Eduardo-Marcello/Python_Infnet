import pygame
from random import randint


class Question_09():

    def __init__(self):
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

    def draw_button(self, x, y):
        return pygame.draw.circle(self.screen, self.button_color, (x, y), self.circle_height)

    def draw_random_squares(self, screen, rect_color, area):
        return pygame.draw.rect(screen, rect_color, area)

    def draw_text(self):
        return self.screen.blit(self.circle_caption, (self.circle_pos - 25, self.circle_width - 10))

    def move_button(self, event):
        if event.type == pygame.KEYDOWN:
            self.screen.fill(self.bgcolor)
            self.draw_button(self.circle_pos, self.circle_width)
            self.draw_text()
            # self.screen.blit(self.circle_caption, (self.circle_pos - 25, self.circle_width - 10))
            for r in self.collided_rects:
                if r.collidepoint(self.circle_pos, self.circle_width):
                    self.collided_rects.remove(r)
                else:
                    self.draw_random_squares(self.screen, self.rect_color, r)
            if event.key == ord('a'):
                self.circle_pos -= 10
                # print('a pressed')
            if event.key == ord('d'):
                self.circle_pos += 10
                # print('d pressed')
            if event.key == ord('w'):
                self.circle_width -= 10
                # print('w pressed')
            if event.key == ord('s'):
                self.circle_width += 10
                # print('s pressed')
            print(self.circle_pos, self.circle_width)
        return self

    def event(self):
        self.screen.fill(self.bgcolor)
        button = self.draw_button(self.circle_pos, self.circle_width)
        self.screen.blit(self.circle_caption, (272, 40))
        while not self.finish:
            x, y = randint(0, self.width), randint(0, self.height)
            area = pygame.Rect(x, y, self.rect_width, self.rect_height)
            for event in pygame.event.get():

                self.move_button(event)

                if event.type == pygame.QUIT:
                    self.finish = True
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # pos = pygame.mouse.get_pos()
                    cx, cy = pygame.mouse.get_pos()
                    if (self.circle_pos + self.circle_height >= cx >= self.circle_pos - self.circle_height) and\
                            (self.circle_width + self.circle_height >= cy >= self.circle_width - self.circle_height):
                    # if button.collidepoint(pos):
                        square = self.draw_random_squares(self.screen, self.rect_color, area)
                        self.collided_rects.append(square)
                        # self.collided_rects.append(area)

                        # for r in self.collided_rects:
                        #     if r is not area and r.colliderect(area):
                        #         self.collided_rects.remove(r)
                        #
                        #         if area in self.collided_rects:
                        #             self.collided_rects.remove(area)

                pygame.display.update()

        pygame.display.quit()
        pygame.quit()


Question_09().event()
