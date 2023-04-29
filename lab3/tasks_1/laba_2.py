import pygame
from pygame.draw import *

pygame.init()
x = 600
y = 600
FPS = 30
screen = pygame.display.set_mode((x, y))
Dark_yellow_green = (19, 39, 18) # земля
Dark_greenish_blue = (2, 32, 39) # небо
White = (255, 255, 255)
DimGray = (105, 105, 105)
BlackGray = (56, 56, 56)
Silver = (192, 192, 192)

surf = pygame.Surface((x, y))
screen.fill(Dark_greenish_blue)
surf.fill(Dark_yellow_green)
screen.blit(surf, (0, y // 2))
pygame.display.flip()

def moon(): # луна
    circle(screen, White, (x * .75, y * .25), ((x + y) // 20))

def cloud_gray(): # туча светлая
    width = 60
    ellipse(screen, DimGray,(-100, 0, x, width))
    ellipse(screen, DimGray, (x // 2, 50, x // 2, width))
    ellipse(screen, DimGray, (x * .25, 120, x * .5, width + 15))
    ellipse(screen, DimGray, (0, 80, x // 3, width))

def cloud_black(): # туча темная
    width = 60
    ellipse(screen, BlackGray, (x * .75, 0, x * .2, width - 20))
    ellipse(screen, BlackGray, (x // 2, 150, x // 2, width + 15))
    ellipse(screen, BlackGray, (x // 10, 150, x * .5, width + 30))
    ellipse(screen, BlackGray, (x // 20, 30, x * .5, width + 20))

def alien_machine(x,y,long,width): # инопланетная машина
    '''Рисуем инопланетную машину, размер вводить 1/3(длинный/ширины)
       surface - объект pygame.Surface
       x, y - координаты левого верхнего угла изображения
       long, width - длинна и ширина изобажения
       color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    polygon(screen, White, ((x + long // 2 , y), (x + long, y + long), (x, y + long)))

    ellipse(screen, DimGray, (x, y, long, width))
    plate_x = long * .25
    plate_y = width * .25
    long_1 = long * .75
    width_1 = width * .75

    ellipse(screen, Silver, (x + plate_x // 2, y - plate_y // 2, long_1, width_1))

    long_2 = long * .1
    width_2 = width * .15

    ellipse(screen, White, (x + long_1, y + long * .2, long_2, width_2))
    ellipse(screen, White, (x + long_1 * 1.15, y + long * .13, long_2, width_2))
    ellipse(screen, White, (x + long_1 * .75, y + long * .24, long_2, width_2))
    ellipse(screen, White, (x + long_1 * .50, y + long * .24, long_2, width_2))
    ellipse(screen, White, (x + long_1 * .25, y + long * .21, long_2, width_2))
    ellipse(screen, White, (x + long_1 * .07, y + long * .15, long_2, width_2))

moon()
cloud_gray()
cloud_black()
alien_machine(50,200,120,40)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()