import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
white = (255, 255, 255)
blue = (0, 0, 255)
screen.fill(white)
pygame.display.flip()

x = 200
y = 200
eye = 75
circle(screen, (255, 255, 0), (x, y), 150)
circle(screen, (0, 0, 0), (x, y), 150, width=1)

circle(screen, (255, 0, 0), (x - eye, y - 50), 25)
circle(screen, (0, 0, 0), (x - eye, y - 50), 25, width=1)
circle(screen, (255, 0, 0), (x + eye, y - 50), 20)
circle(screen, (0, 0, 0), (x + eye, y - 50), 20, width=1)

circle(screen, (0, 0, 0), (x - eye, y - 50), 12)
circle(screen, (0, 0, 0), (x + eye, y - 50), 10)

polygon(screen, blue,((60,60),(55,65),(170,155),(175,150)))
polygon(screen, blue,((355,90),(360,95),(235,145),(230,140)))

rect(screen, (0, 0, 0),(125,280,150,30))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()