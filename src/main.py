import os
import pygame
from random import randrange

SIZE = WIDTH, HEIGHT = (600, 600)

# A grid of cells with randomly placed mines
class Minefield:
    pass

# A cell contains its location, if it has a mine, and if it has been clicked on
class Cell:
    pass

# The first screen the player sees, the menu is a navigation hub to different parts of the game
def menu():
    pass

# A help screen provides the player with information on rules and how to operate the game's features
def help():
    pass

# A pause screen for when the player pauses the game
def pause():
    pass

# The game over screen stops the game and lets the player exit the game or try again
def game_over():
    pass

# The settings menu allows the player to change the game mode to easy (9x9 grid and 10 mines), intermediate (16x16 and 40 mines), and advanced (16x30 and 99 mines)
def settings():
    pass

# Manages in-game variables and hosts the game loop
def main():
    pygame.init()

    canvas = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()

    background = pygame.Surface(SIZE)
    background.fill((255, 255, 255))

    # Game loop
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