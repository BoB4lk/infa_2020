import pygame

pygame.init()

x = 600
y = 600
FPS = 30
screen = pygame.display.set_mode((x, y))
Dark_yellow_green = (19, 39, 18)   # земля
Dark_greenish_blue = (2, 32, 39)   # небо
surf = pygame.Surface((x, y))
screen.fill(Dark_greenish_blue)
surf.fill(Dark_yellow_green)

screen.blit(surf, (0, y // 2))
pygame.display.flip()




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()