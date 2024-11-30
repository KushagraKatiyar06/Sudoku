import pygame, sys
from sudoku_generator import SudokuGenerator, Cell



if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Sudoku')
    screen.fill(("light blue"))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            pygame.display.update()