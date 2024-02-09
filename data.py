class Data:
    def __init__(self, x, y, length, direction):
        self.x = x
        self.y = y
        self.length = length
        self.direction = direction
    
    def contains(self, x, y):
        if self.direction == 0:
            return self.x == x and self.y <= y and y < self.y + self.length
        else:
            return self.y == y and self.x <= x and x < self.x + self.length