import os
import pygame
from random import randrange

SIZE = WIDTH, HEIGHT = (600, 600)

def main():
    pygame.init()

    canvas = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()

    background = pygame.Surface(SIZE)
    background.fill((255, 255, 255))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        canvas.blit(background, (0, 0))
        pygame.display.flip()

if __name__ == "__main__":
    main()
    pygame.quit()