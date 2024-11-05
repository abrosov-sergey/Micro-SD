class QueenObserver:
    def __init__(self, board):
        self.board = board

    def is_safe(self, row, col):
        for r, c in self.board.queen_positions:
            if row == r or col == c or abs(row - r) == abs(col - c):
                return False
        return True

class Board:
    def __init__(self):
        self.queen_positions = []
        self.observers = [QueenObserver(self)]

    def add_queen(self, row, col):
        if all(observer.is_safe(row, col) for observer in self.observers):
            self.queen_positions.append((row, col))
            self.notify_observers()
            return True
        return False

    def remove_queen(self, row, col):
        self.queen_positions.remove((row, col))
        self.notify_observers()

    def notify_observers(self):
        pass  # Logic for notifying observers can be added here

    def solve(self, row=0):
        if row == 8:
            print(self.queen_positions)
            return True

        for col in range(8):
            if self.add_queen(row, col):
                if self.solve(row + 1):
                    return True
                self.remove_queen(row, col)
        return False

board = Board()
board.solve()
