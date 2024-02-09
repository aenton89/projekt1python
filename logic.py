import random

import board
import data

PLAYER = True
COMPUTER = False

NOT_END = 0
WON = 1
LOST = 2

class Logic:
    def __init__(self, my_board, enemy_board):
        self.my_board = my_board
        self.enemy_board = enemy_board

        self.turn = PLAYER

        self.ships_to_place = {5 : 1, 4 : 1, 3 : 2, 2 : 2}
        self.ships_to_sunk = {5 : 1, 4 : 1, 3 : 2, 2 : 2}

        # tablica pomocnicza, do np. rozstawiania statkow - a dokladniej ich odrozstawiania
        self.temp_board = board.Board()
        # to do sprawdzania podczas wkladania czy sa obok siebie w jednej linii
        self.listx = []
        self.listy = []
        self.listData = []

        # pod ostrzal komputera
        self.ship_shot = False
        self.ship_shot_twice = False
        self.ship_sunk = False
        self.pos_shot = []
        self.arrow = None
        self.direction = [0, 1, 2, 3]

        



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
            
        for row in range(board.ROWS):
            for col in range(board.COLS):
                if(self.my_board.array[row][col] == board.ACCEPTED):
                    self.my_board.array[row][col] = board.SHIP
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
            self.turn = COMPUTER
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
                        self.ships_to_sunk[data.length] -= 1
        

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


    # strzal komputera
    def shoot_computer(self):
         if(not self.ship_shot):
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            while(self.my_board.array[y][x] == board.MISS or self.my_board.array[y][x] == board.ENEMY_SHOT):
                x = random.randint(0, 9)
                y = random.randint(0, 9)
            print(f"Computer shooting at {x}, {y}")
            if(self.my_board.array[y][x] == board.NOTHING):
                self.my_board.array[y][x] = board.MISS
                self.turn = PLAYER
            elif(self.my_board.array[y][x] == board.SHIP):
                self.my_board.array[y][x] = board.ENEMY_SHOT


    # # strzal komputera   
    # def shoot_computer(self):
    #     if(not self.ship_shot):
    #         x = random.randint(0, 9)
    #         y = random.randint(0, 9)
    #         print(f"Computer shooting at {x}, {y}")
    #         if(self.my_board.array[y][x] == board.NOTHING):
    #             self.my_board.array[y][x] = board.MISS
    #             self.turn = PLAYER
    #         elif(self.my_board.array[y][x] == board.SHIP):
    #             self.my_board.array[y][x] = board.ENEMY_SHOT
    #             self.ship_shot = True
    #             self.pos_shot.append((x,y))
    #     elif(self.ship_shot and not self.ship_shot_twice):
    #         actual_direction = random.choice(self.direction)

    #         if(actual_direction == 0):
    #             x = self.pos_shot[-1][0]
    #             y = self.pos_shot[-1][1] - 1
    #         elif(actual_direction == 1):
    #             x = self.pos_shot[-1][0] + 1
    #             y = self.pos_shot[-1][1]
    #         elif(actual_direction == 2):
    #             x = self.pos_shot[-1][0]
    #             y = self.pos_shot[-1][1] + 1
    #         elif(actual_direction == 3):
    #             x = self.pos_shot[-1][0] - 1
    #             y = self.pos_shot[-1][1]

    #         print(f"Computer shooting at {x}, {y}")

    #         if(self.my_board.array[y][x] == board.MISS or self.my_board.array[y][x] == board.ENEMY_SHOT or self.my_board.array[y][x] == board.NOTHING):
    #             self.direction.remove(actual_direction)
    #             self.turn = PLAYER
    #             if(self.my_board.array[y][x] == board.NOTHING):
    #                 self.my_board.array[y][x] = board.MISS
    #         else:
    #             self.ship_shot_twice = True
    #             self.arrow = actual_direction
    #             self.pos_shot.append((x,y))
    #             self.ship_sunk = self.check_if_computer_sunk_this()
    #             self.my_board.array[y][x] = board.ENEMY_SHOT
    #     elif(self.ship_shot_twice):
    #         remek = random.randint(0, 1)
    #         if(self.arrow == 0 or self.arrow == 2):
    #             minimum = min(self.pos_shot, key=lambda x: x[0])
    #             maximum = max(self.pos_shot, key=lambda x: x[0])
    #             if(remek == 0):
    #                 x = minimum[0] - 1
    #                 y = minimum[1]
    #             else:
    #                 x = maximum[0] + 1
    #                 y = maximum[1]

    #             if(self.my_board.array[y][x] == board.MISS or self.my_board.array[y][x] == board.ENEMY_SHOT or self.my_board.array[y][x] == board.NOTHING):
    #                 self.turn = PLAYER
    #                 if(self.my_board.array[y][x] == board.NOTHING):
    #                     self.my_board.array[y][x] = board.MISS
    #             else:
    #                 self.ship_sunk = self.check_if_computer_sunk_this()
    #                 self.my_board.array[y][x] = board.ENEMY_SHOT
    #         elif(self.arrow == 1 or self.arrow == 3):
    #             minimum = min(self.pos_shot, key=lambda x: x[1])
    #             maximum = max(self.pos_shot, key=lambda x: x[1])
    #             if(remek == 0):
    #                 x = minimum[0]
    #                 y = minimum[1] - 1
    #             else:
    #                 x = maximum[0]
    #                 y = maximum[1] + 1

    #             if(self.my_board.array[y][x] == board.MISS or self.my_board.array[y][x] == board.ENEMY_SHOT or self.my_board.array[y][x] == board.NOTHING):
    #                 self.turn = PLAYER
    #                 if(self.my_board.array[y][x] == board.NOTHING):
    #                     self.my_board.array[y][x] = board.MISS
    #             else:
    #                 self.ship_sunk = self.check_if_computer_sunk_this()
    #                 self.my_board.array[y][x] = board.ENEMY_SHOT


    #         self.ship_sunk = self.check_if_computer_sunk_this()

    #     if(self.ship_sunk):
    #         self.restore_params()

                
    # # sprawdza czy juz zatopiono ten statek
    # def check_if_computer_sunk_this(self):
    #     if(self.arrow == 0 or self.arrow == 2):
    #         minimum = min(self.pos_shot, key=lambda x: x[0])
    #         maximum = max(self.pos_shot, key=lambda x: x[0])
    #         min1 = minimum[1] - 1
    #         max1 = maximum[1] + 1
    #         if((self.my_board.array[min1][minimum[0]] == board.NOTHING or self.my_board.array[min1][minimum[0]] == board.MISS) and (self.my_board.array[max1][maximum[0]] == board.NOTHING or self.my_board.array[max1][maximum[0]] == board.MISS)):
    #             return True
    #         else:
    #             return False
    #     elif(self.arrow == 1 or self.arrow == 3):
    #         minimum = min(self.pos_shot, key=lambda x: x[1])
    #         maximum = max(self.pos_shot, key=lambda x: x[1])
    #         min1 = minimum[0] - 1
    #         max1 = maximum[0] + 1
    #         if((self.my_board.array[minimum[1]][min1] == board.NOTHING or self.my_board.array[minimum[1]][min1] == board.MISS) and (self.my_board.array[maximum[1]][max1] == board.NOTHING or self.my_board.array[maximum[1]][max1] == board.MISS)):
    #             return True
    #         else:
    #             return False
            

    # powrot do normalnosci po zdjeciu jednego obiektu
    def restore_params(self):
        self.ship_shot = False
        self.ship_sunk = False
        self.ship_shot_twice = False
        self.pos_shot = []
        self.direction = [0, 1, 2, 3]
        self.arrow = None


    # metoda sprawdzajaca kto wygral
    def check_if_end(self):
        player = 0
        computer = 0
        sum = 5+4+3+3+2+2
        for row in range(board.ROWS):
            for col in range(board.COLS):
                if(self.my_board.array[row][col] == board.ENEMY_SHOT):
                    computer += 1
                if(self.enemy_board.array[row][col] == board.SUNK):
                    player += 1
        if(player == sum):
            return WON
        elif(computer == sum):
            return LOST
        else:
            return NOT_END