ROWS = 10
COLS = 10

NOTHING = 0
SHIP = 1
ENEMY_SHOT = 2

MISS = 3
HIT = 4
SUNK = 5

PLACED = 6
ACCEPTED = 7

class Board:
    def __init__(self):
        self.array = [[NOTHING] * ROWS for _ in range(COLS)]
    
    def clear(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.array[row][col] = NOTHING