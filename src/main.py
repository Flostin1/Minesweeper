import os
import pygame
from random import randrange

SIZE = WIDTH, HEIGHT = (600, 600)

# A grid of cells with randomly placed mines
class Minefield:
    def __init__(self, game_mode):
        self.cells = []
        self.cell_color = pygame.Color('blue')
        self.mines = game_mode['mines']
        self.horizontal_count = game_mode['width']
        self.vertical_count = game_mode['height']
        self.cell_width = WIDTH / self.horizontal_count
        self.cell_height = HEIGHT / self.vertical_count

        # Fills the minefield with empty cells
        for y in range(self.horizontal_count):
            self.cells.append([])
            for x in range(self.vertical_count):
                self.cells[y].append(0)

        # Places the mines onto the minefield
        mine_count = self.mines
        while mine_count > 0:
            x = randrange(self.horizontal_count)
            y = randrange(self.vertical_count)

            if self.cells[y][x] == 0:
                self.cells[y][x] = 1
                mine_count -= 1
    
    def render(self, surface):
        for y in range(self.horizontal_count):
            for x in range(self.vertical_count):
                pygame.draw.rect(
                    surface, 
                    self.cell_color if self.cells[y][x] == 0 else (200, 0, 0), 
                    (x * self.cell_width + 1, y * self.cell_height + 1, self.cell_width - 2, self.cell_height - 2)
                )

# A cell contains its location, if it has a mine, and if it has been clicked on
class Cell:
    pass

# The first screen the player sees, the menu is a navigation hub to different parts of the game
def menu():
    pass

# A help screen provides the player with information on rules and how to operate the game's features
def help():
    pass

# The settings menu allows the player to change the game mode to easy (9x9 grid and 10 mines), intermediate (16x16 and 40 mines), and advanced (16x30 and 99 mines)
def settings():
    pass

# The game screen is where the game is run, rendered, and manipulated by the player
def game():
    pass

# A pause screen for when the player pauses the game
def pause():
    pass

# The game over screen stops the game and lets the player exit the game or try again
def game_over():
    pass


# Manages in-game variables and hosts the game loop
def main():
    pygame.init()

    minefield = Minefield({'mines': 9, 'width': 9, 'height': 9})

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
        minefield.render(canvas)
        pygame.display.flip()

if __name__ == "__main__":
    main()
    pygame.quit()