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

surf = pygame.Surface((x, y))
screen.fill(Dark_greenish_blue)
surf.fill(Dark_yellow_green)
screen.blit(surf, (0, y // 2))
pygame.display.flip()

def moon(): # луна
    circle(screen, White, (x * .75, y * .25), ((x + y) // 20))
moon()

def cloud_gray(): # туча
    ellipse(screen, DimGray,(0, 0, (x // 2), 50))
    # ellipse(screen, DimGray, (x, y, long, thickness))
    # ellipse(screen, DimGray, (x, y, long, thickness))
    # ellipse(screen, DimGray, (x, y, long, thickness))
cloud_gray()
# cloud_gray(350,150,300,50)
# cloud_gray(0,10,500,100)
# cloud_gray(-50,120,250,50)

def cloud_black(x, y, long, thickness): # туча
    ellipse(screen, BlackGray,(x, y, long, thickness))
# cloud_black(250,100,300,70)
# cloud_black(400,10,350,100)
# cloud_black(10,70,250,90)
# cloud_black(300,0,150,50)

def alien_machine(): # инопланетная машина
    ellipse(screen, DimGray, (20, 200, 200, 50))
    ellipse(screen, White, (45, 190, 150, 40))

    ellipse(screen, White, (40, 223, 10, 10))
    ellipse(screen, White, (80, 233, 10, 10))
    ellipse(screen, White, (120, 235, 10, 10))
    ellipse(screen, White, (160, 233, 10, 10))
    ellipse(screen, White, (200, 220, 10, 10))

# alien_machine()

def alien(): # инопланетянин
    aalines(screen, White)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()