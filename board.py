import tiles

class Board:
    def __init__(self):
        self.array = [[tiles.NOTHING] * tiles.ROWS for _ in range(tiles.COLS)]

    def get_tile(self, x, y):
        return self.array[x][y]
    
    def set_tile(self, x, y, tile):
        self.array[x][y] = tile