import pygame
from sudoku_generator import SudokuGenerator
import random

# Constants
WIDTH, HEIGHT = 900, 900
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game Variables
game_state = None
difficulty = 40  # Number of cells to remove for the puzzle

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Game")

# Initialize Pygame and Fonts
pygame.init()  # This will initialize all Pygame modules, including fonts

# Fonts
font = pygame.font.Font(None, 50)

# Function to display text on the screen
def display_text(text, x, y, font, color=BLACK):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

# Game Start Screen
def game_start_screen():
    screen.fill(WHITE)
    display_text("Welcome to Sudoku!", WIDTH // 3, HEIGHT // 3, font)
    display_text("Press any key to start", WIDTH // 3, HEIGHT // 2, font)
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                waiting = False

# Game Over Screen
def game_over_screen():
    screen.fill(WHITE)
    display_text("Game Over! You Win!", WIDTH // 3, HEIGHT // 3, font)
    display_text("Press R to restart or Q to quit", WIDTH // 3, HEIGHT // 2, font)
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()  # Restart the game
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

# Game in Progress Screen (Main Game Loop)
def game_in_progress_screen():
    global game_state

    # Initialize a Sudoku board and remove some cells
    game_state = SudokuGenerator(9, difficulty)  # Pass size and number of cells to remove
    game_state.fill_values()  # Fill the Sudoku grid with valid values

    # Game loop
    running = True
    while running:
        screen.fill(WHITE)  # Clear screen before drawing
        draw_board(game_state)  # Draw the Sudoku grid and numbers
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Handle other events like clicking, number entry, etc.
            if event.type == pygame.KEYDOWN:
                # Handle number input or game state checks here
                pass

# Function to draw the board
def draw_board(game_state):
    cell_size = WIDTH // 9
    for row in range(9):
        for col in range(9):
            x, y = col * cell_size, row * cell_size
            rect = (x, y, cell_size, cell_size)
            pygame.draw.rect(screen, BLACK, rect, 1)  # Draw grid cell borders
            if game_state.board[row][col] != 0:  # Access the board inside game_state
                display_text(str(game_state.board[row][col]), x + cell_size // 3, y + cell_size // 3, font)

# Main Game Loop
def main():
    game_start_screen()
    game_in_progress_screen()
    game_over_screen()

# Run the game
if __name__ == "__main__":
    main()
