"""
Created on 05.11.2024
Solution of the Eight Queens (8Q) problem
with Abstract data type method.
@author: Geolan84
"""
class Board:

    __slots__ = ('size', 'solutions')

    def __init__(self, size):
        self.size = size
        self.solutions = 0

    def solve(self):
        coords = [-1] * self.size
        self.place_queen(coords, 0)
        print(f"Task has {self.solutions} solutions.")

    def place_queen(self, coords, target_row):
        if target_row == self.size:
            self.display_board(coords)
            self.solutions += 1
        else:
            for column in range(self.size):
                if self.try_to_place(coords, target_row, column):
                    coords[target_row] = column
                    self.place_queen(coords, target_row + 1)

    def try_to_place(self, coords, p_size, column):
        for i in range(p_size):
            if coords[i] == column or coords[i] - i == column - p_size or coords[i] + i == column + p_size:
                return False
        return True

    def display_board(self, coords):
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                line += " q " if coords[row] == column else " * "
            print(line)
        print()


board = Board(8)
board.solve()
