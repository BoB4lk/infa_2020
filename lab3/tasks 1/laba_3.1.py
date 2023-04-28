import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((600, 600))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

class balls:

    def ball(self):
        ''' Рисуем шар в разных местах с частотой обновления  FPS.
            Рисует в разных цветах из списка '''

        self.x = randint(100, 700)
        self.y = randint(100, 500)
        self.r = randint(30, 50)
        self.color = COLORS[randint(0, 5)]
        circle(screen, self.color, (self.x, self.y), self.r)

    def click(self):
        ''' Определяем находится ли курсор мыши в радиусе кругаю во время клика мышью.
            Если находиться, то печатает в терминале текскст указанный в (print) '''

        self.x_mouse = pygame.mouse.get_pos()
        self.x_ball = (self.x - self.r, self.y - self.r)
        self.y_ball = (self.x + self.r, self.y + self.r)
        if self.x_ball <= self.x_mouse <= self.y_ball:
            print("Попал =)")

num = 0

balls = balls()
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if balls.click() == True:
                num += 1

    balls.ball()
    pygame.display.update()
    screen.fill(BLACK)

print("Всего за игру попали - ", num, "раз")
pygame.quit()