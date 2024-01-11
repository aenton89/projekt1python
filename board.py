import tiles

BOARD_SIZE = 10


class Board:
    def __init__(self):
        self.array = [[tiles.NOTHING] * BOARD_SIZE for _ in range(BOARD_SIZE)]

    def get_tile(self, x, y):
        return self.array[x][y]
    
    def set_tile(self, x, y, tile):
        self.array[x][y] = tile    