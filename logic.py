import random

import board
import data

class Logic:
    def __init__(self, my_board, enemy_board):
        self.my_board = my_board
        self.enemy_board = enemy_board

        self.ships_to_place = {5 : 1, 4 : 1, 3 : 2, 2 : 2}
        self.ships_to_sunk = {5 : 1, 4 : 1, 3 : 2, 2 : 2}

        # tablica pomocnicza, do np. rozstawiania statkow - a dokladniej ich odrozstawiania
        self.temp_board = board.Board()
        # to do sprawdzania podczas wkladania czy sa obok siebie w jednej linii
        self.listx = []
        self.listy = []
        self.listData = []


    # metody pod dodawanie statkow
    def place_ship(self, x, y):
        if(self.my_board.array[y][x] == board.NOTHING):
            good = False
            good_direction_x = 0
            good_direction_y = 0
            if(len(self.listx) > 0):
                for j in self.listx:
                    if(j == x):
                        good_direction_x += 1
                for j in self.listy:
                    if(j == y):
                        good_direction_y += 1
                
                if(good_direction_x == len(self.listx)):
                    for i in self.listy:
                        if(y == i + 1 or y == i - 1):
                            good = True
                elif(good_direction_y == len(self.listy)):
                    for i in self.listx:
                        if(x == i + 1 or x == i - 1):
                            good = True

            elif(len(self.listx) == 0):
                good = True

            if(good):
                self.listx.append(x)
                self.listy.append(y)
                self.temp_board.array[y][x] = board.PLACED
                self.my_board.array[y][x] = board.PLACED
        
    def remove_ship(self, x, y):
        if(self.temp_board.array[y][x] == board.PLACED):
            self.temp_board.array[y][x] = board.NOTHING
            self.my_board.array[y][x] = board.NOTHING

    def accept_ship(self):
        counter = 0
        for row in range(board.ROWS):
            for col in range(board.COLS):
                if(self.temp_board.array[row][col] == board.PLACED):
                    counter += 1

        for key in self.ships_to_place:
            if(counter == key and self.ships_to_place[key] > 0):
                self.ships_to_place[key] -= 1

                for row in range(board.ROWS):
                    for col in range(board.COLS):
                        if(self.temp_board.array[row][col] == board.PLACED):
                            self.temp_board.array[row][col] = board.NOTHING
                            self.my_board.array[row][col] = board.ACCEPTED
                            # czyszczenie listy do okreslania kierunku i kolejnosci pol
                            self.listx.clear()
                            self.listy.clear()

    def check_if_all_ships_placed(self):
        for key in self.ships_to_place:
            if(self.ships_to_place[key] > 0):
                return False
        return True
    

    # metody pod rozkladanie statkow przez komputer
    def place_ship_computer(self):
        ships_map = {5 : 1, 4 : 1, 3 : 2, 2 : 2}
        i = 5
        while i > 1:
            if i in ships_map:
                j = ships_map[i]
                print(f"Placing {j} ships of length {i}")
                while j > 0:
                    direction = random.randint(0, 1)
                    if direction == 0:
                        x = random.randint(0, 9)
                        y = random.randint(0, 9 - i)
                        if self.check_if_placeable(x, y, i, direction):
                            print(f"Placing ship of length {i} at {x}, {y}, direction {direction}")
                            for k in range(i):
                                self.enemy_board.array[y + k][x] = board.SHIP
                            self.listData.append(data.Data(x, y, i, direction))
                            j -= 1
                    else:
                        x = random.randint(0, 9 - i)
                        y = random.randint(0, 9)
                        if self.check_if_placeable(x, y, i, direction):
                            print(f"Placing ship of length {i} at {x}, {y}, direction {direction}")
                            for k in range(i):
                                self.enemy_board.array[y][x + k] = board.SHIP
                            self.listData.append(data.Data(x, y, i, direction))
                            j -= 1
                i -= 1

    def check_if_placeable(self, x, y, length, direction):
        if direction == 0:
            for i in range(length):
                if self.enemy_board.array[y + i][x] == board.SHIP:
                    return False
        else:
            for i in range(length):
                if self.enemy_board.array[y][x + i] == board.SHIP:
                    return False
        return True


    # metody na strzelanie
    def shoot(self, x, y):
        if(self.enemy_board.array[y][x] == board.NOTHING):
            self.enemy_board.array[y][x] = board.MISS
        elif(self.enemy_board.array[y][x] == board.SHIP):
            self.enemy_board.array[y][x] = board.HIT
            if(self.check_if_sunk(x, y)):
                for data in self.listData:
                    if(data.contains(x, y)):
                        for i in range(data.length):
                            if(data.direction == 0):
                                self.enemy_board.array[data.y + i][data.x] = board.SUNK
                            else:
                                self.enemy_board.array[data.y][data.x + i] = board.SUNK
                    break

    # sprawdzamy czy zatonal porownujac z czy nalezy do jakiegos statku
    def check_if_sunk(self, x, y):
        for data in self.listData:
            if(data.contains(x, y)):
                for i in range(data.length):
                    if(data.direction == 0):
                        if(self.enemy_board.array[data.y + i][data.x] != board.HIT):
                            return False
                    else:
                        if(self.enemy_board.array[data.y][data.x + i] != board.HIT):
                            return False
                break
        return True

                
    

    # sprawdza czy nalezy do jakiegos statku





    # metoda sprawdzajaca kto wygral