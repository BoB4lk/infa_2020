import pygame
from pygame.draw import *

pygame.init()

screen = pygame.display.set_mode((600,800))
clock = pygame.time.Clock()



clock.tick(30)


pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()