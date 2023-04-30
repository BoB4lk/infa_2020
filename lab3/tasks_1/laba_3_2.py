import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

class Balls:
    def __init__(self):
        self.num = 0
        self.r = randint(20, 50)
        self.x = randint(self.r, screen_width - self.r)
        self.y = randint(self.r, screen_height - self.r)
        self.dx, self.dy = (2, 3)
        self.color = COLORS[randint(0, 5)]
        # self.ball_new()
        circle(screen, YELLOW, (self.x, self.y), self.r)

    def movement_ball(self):
        ''' Перемещение нарисованного обьекта в одну из сторон экрана  '''

        self.x += self.dx
        self.y += self.dy

        if self.x - self.r < 0 or self.x + self.r > screen_width:
            self.dx = -self.dx
        if self.y - self.r < 0 or self.y + self.r > screen_height:
            self.dy = -self.dy

    def ball_new(self):
        ''' Рисуем шар в рандомном месте экрана и с рандомным радиусом (от 20 до 50) '''

        circle(screen, YELLOW, (self.x, self.y), self.r)

    def click(self):
        ''' Определяем находится ли курсор мыши в радиусе кругаю во время клика мышью. '''

        self.x_mouse = pygame.mouse.get_pos()
        self.x_ball = (self.x - self.r, self.y - self.r)
        self.y_ball = (self.x + self.r, self.y + self.r)
        if self.x_ball <= self.x_mouse <= self.y_ball:
            self.num += 1

    def click_1(self):
        ''' Вывод общего колличества попаданий курсором мыши во время клика по шару '''

        print("Всего за игру попали - ", self.num, "раз")

ball = Balls()
bal2 = Balls()
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            ball.click()
            bal2.click()

    ball.ball_new()
    ball.movement_ball()
    bal2.ball_new()
    bal2.movement_ball()
    pygame.display.update()
    screen.fill(BLACK)


ball.click_1()
bal2.click_1()
pygame.quit()

