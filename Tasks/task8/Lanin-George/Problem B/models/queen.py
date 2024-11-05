class Queen:

    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def try_place(self, queens) -> bool:
        for coords in queens:
            if (self.x == coords[0] or self.y == coords[1] or abs(coords[0] - self.x) == abs(coords[1] - self.y)):
                return False
        return True
