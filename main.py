import pygame, sys
from pygame.locals import *

def main():
    pygame.init()

    DISPLAY = pygame.display.set_mode((500,400),0,32)

    WHITE = (255,255,255)
    BLUE = (0,0,255)

    DISPLAY.fill(WHITE)

    pygame.draw.rect(DISPLAY, BLUE, (200,150,100,50))

    x = 100
    y = 100
    velocity = pygame.Vector2()
    velocity.xy = 0, 0
    acceleration = 0.1
    while True:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        DISPLAY.fill(WHITE)
        pygame.draw.rect(DISPLAY, BLUE, (x,y, 50,50))
        y += velocity.y
        velocity.y += acceleration
        if keys[pygame.K_a]:
            velocity.y = -3
        if y > DISPLAY.get_height() - 50:
            velocity.y = -velocity.y
        pygame.display.update()
        pygame.time.delay(10)

main()
