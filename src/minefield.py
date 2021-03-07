"""
TODO:
 * Generate minefield
 * Make function that returns all surrounding cells

"""

from random import randrange

# Fills the minefield with empty cells
minefield = []
for y in range(9):
    minefield.append([])
    for x in range(9):
        minefield[y].append(0)

# Places the mines onto the minefield
mine_count = 9
while mine_count > 0:
    x = randrange(9)
    y = randrange(9)

    if minefield[y][x] == 0:
        minefield[y][x] = 1
        mine_count -= 1

for row in minefield:
    print(row)