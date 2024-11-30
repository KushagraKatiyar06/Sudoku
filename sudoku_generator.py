import math
import random

class SudokuGenerator:
    def __init__(self, row_length=9, removed_cells=40):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = []
        self.box_length = int(math.sqrt(self.row_length))

        # Initialize the board
        self.get_board()

    def get_board(self):
        """ Initializes the board with zeros. """
        for row in range(self.row_length):
            new_row = [0] * self.row_length
            self.board.append(new_row)

    def fill_box(self, row_start, col_start):
        """ Fill a 3x3 box with unique numbers. """
        num_set = []
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                num = random.randint(1, 9)
                while num in num_set:
                    num = random.randint(1, 9)
                num_set.append(num)
                self.board[i][j] = num

    def fill_diagonal(self):
        """ Fill the diagonal boxes (3x3 boxes). """
        for i in range(0, self.row_length, 3):
            self.fill_box(i, i)

    def valid_in_row(self, row, num):
        """ Check if the number is valid in the row. """
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        """ Check if the number is valid in the column. """
        for row in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        """ Check if the number is valid in the 3x3 box. """
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                if self.board[row][col] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        """ Check if a number is valid in the given position. """
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        return self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row_start, col_start, num)

    def fill_remaining(self, row, col):
        """ Fill the remaining cells using backtracking. """
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        """ Fill the board with a valid solution. """
        self.fill_diagonal()
        self.fill_remaining(0, 0)

    def remove_cells(self):
        """ Remove cells to create the puzzle. """
        count = self.removed_cells
        while count > 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                count -= 1

    def generate_sudoku(self):
        """ Generate the Sudoku puzzle. """
        self.fill_values()
        self.remove_cells()
        return self.board
