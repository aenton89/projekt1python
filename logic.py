import pygame
import random

import tiles

BEFORE_GAME = 0
CHOOSING_TIME = 1
DURING_GAME = 2
AFTER_GAME = 3

PLAYER_TURN = True
ENEMY_TURN = False

# dodanie zmiany stanu wody - te fale zeby sie robily
class Logic:
    def __init__(self, gui_instance):
        # dwie plansze - jedna dla gracza, druga dla przeciwnika
        self.gui = gui_instance

        self.state = BEFORE_GAME
        self.turn = PLAYER_TURN

        # lista w ktorej sa wspolrzedne fragmentow obecnie ukladanego statku
        self.fragments_list = []
        # liczba fragmentow statku juz polozonych

        self.amount_of_ships = {2: 2, 3: 2, 4: 2, 5: 1}
        self.amount_of_ships_to_place = {2: 2, 3: 2, 4: 2, 5: 1}
        
        

    # przeliczenie wspolrzednych klikniecia mysza na wspolrzedne pola na planszy gracza
    def mouse_to_tiles_players(self, x_mouse, y_mouse):
        if(y_mouse > 20 and y_mouse < 520 and x_mouse > 20 and x_mouse < 520):
            x = (x_mouse - 20) // tiles.TILE_SIZE
            y = (y_mouse - 20) // tiles.TILE_SIZE
        return x, y

    # przeliczenie wspolrzednych klikniecia mysza na wspolrzedne pola na planszy przeciwnika
    def mouse_to_tiles_enemy(self, x_mouse, y_mouse):
        if(y_mouse > 20 and y_mouse < 520 and x_mouse > 540 and x_mouse < 1040):
            x = (x_mouse - 540) // tiles.TILE_SIZE
            y = (y_mouse - 20) // tiles.TILE_SIZE
        return x, y

    # sprawdzenie czy kliknieto w przycisk accept
    def accept_button(self, x_mouse, y_mouse):
        if(x_mouse > self.gui.get_x1 and x_mouse < self.gui.get_x2 and y_mouse > self.gui.get_y1 and y_mouse < self.gui.get_y2):
            return True
        else:
            return False
        
    # zwraca prawde gdy nachodzi juz na jakis statek    
    def check_placement_interference(self, x, y, direction, length):
        if(direction == 0):
            if(y + length > 10):
                return True
            for i in range(length):
                if(self.gui.enemy_board.get_tile(x, y+i) != tiles.NOTHING):
                    return True
        elif(direction == 1):
            if(x + length > 10):
                return True
            for i in range(length):
                if(self.gui.enemy_board.get_tile(x+i, y) != tiles.NOTHING):
                    return True
        elif(direction == 2):
            if(y - length < 0):
                return True
            for i in range(length):
                if(self.gui.enemy_board.get_tile(x, y-i) != tiles.NOTHING):
                    return True
        elif(direction == 3):
            if(x - length < 0):
                return True
            for i in range(length):
                if(self.gui.enemy_board.get_tile(x-i, y) != tiles.NOTHING):
                    return True
        return False
    
    def place_enemy_ships(self):
        for i in range(5, 1, -1):
            for j in range(self.amount_of_ships[i]):
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                direction = random.randint(0,3)

                while self.check_placement_interference(x, y, direction, i):
                    x = random.randint(0, 9)
                    y = random.randint(0, 9)
                    direction = random.randint(0,3)

                # polnoc
                if(direction == 0):
                    for k in range(i):
                        if(k == 0):
                            self.gui.enemy_board.set_tile(x, y+k, tiles.FRONT_SHIP_H)
                        elif(k == i-1):
                            self.gui.enemy_board.set_tile(x, y+k, tiles.BACK_SHIP_H)
                        else:
                            self.gui.enemy_board.set_tile(x, y+k, tiles.MIDDLE_SHIP_H)
                # wschod
                elif(direction == 1):
                    for k in range(i):
                        if(k == 0):
                            self.gui.enemy_board.set_tile(x+k, y, tiles.FRONT_SHIP_V)
                        elif(k == i-1):
                            self.gui.enemy_board.set_tile(x+k, y, tiles.BACK_SHIP_V)
                        else:
                            self.gui.enemy_board.set_tile(x+k, y, tiles.MIDDLE_SHIP_V)
                # poludnie
                elif(direction == 2):
                    for k in range(i):
                        if(k == 0):
                            self.gui.enemy_board.set_tile(x, y-k, tiles.BACK_SHIP_H)
                        elif(k == i-1):
                            self.gui.enemy_board.set_tile(x, y-k, tiles.FRONT_SHIP_H)
                        else:
                            self.gui.enemy_board.set_tile(x, y-k, tiles.MIDDLE_SHIP_H)
                # zachod
                elif(direction == 3):
                    for k in range(i):
                        if(k == 0):
                            self.gui.enemy_board.set_tile(x-k, y, tiles.BACK_SHIP_V)
                        elif(k == i-1):
                            self.gui.enemy_board.set_tile(x-k, y, tiles.FRONT_SHIP_V)
                        else:
                            self.gui.enemy_board.set_tile(x-k, y, tiles.MIDDLE_SHIP_V)

    # rozlozenie statkow gracza - sprawdzanie czy rozklada poprawnie
    def place_player_ships(self, x, y, direction, length):
        pass

    # poczatek gry, wyswietlenie napisow oraz oczekiwanie na enter
    def start_game(self, input):
        if(self.state == BEFORE_GAME):
            self.gui.draw_before_game()
            # sprawdzenie czy wcisnieto enter
            if(input.type == pygame.K_RETURN):
                self.state = CHOOSING_TIME
                self.gui.draw_choosing_time()
                self.place_enemy_ships()

    def calc_direction(self):
        return self.fragments_list[0][0] - self.fragments_list[1][0], self.fragments_list[0][1] - self.fragments_list[1][1]
    
    def change_setting_ship_to_ships(self):
        x_off, y_off = self.calc_direction()

        for i in range(len(self.fragments_list)):
            if(x_off == 0):
                if(i == 0):
                    self.gui.player_board.set_tile(self.fragments_list[i][0], self.fragments_list[i][1], tiles.FRONT_SHIP_H)
                elif(i == len(self.fragments_list) - 1):
                    self.gui.player_board.set_tile(self.fragments_list[i][0], self.fragments_list[i][1], tiles.BACK_SHIP_H)
                else:
                    self.gui.player_board.set_tile(self.fragments_list[i][0], self.fragments_list[i][1], tiles.MIDDLE_SHIP_H)
            elif(y_off == 0):
                if(i == 0):
                    self.gui.player_board.set_tile(self.fragments_list[i][0], self.fragments_list[i][1], tiles.FRONT_SHIP_V)
                elif(i == len(self.fragments_list) - 1):
                    self.gui.player_board.set_tile(self.fragments_list[i][0], self.fragments_list[i][1], tiles.BACK_SHIP_V)
                else:
                    self.gui.player_board.set_tile(self.fragments_list[i][0], self.fragments_list[i][1], tiles.MIDDLE_SHIP_V)


    # rozkladanie statkow przez gracza - input, prawe czy lewe klikniecie myszy - prawe usuwa zaznaczone pole
    def choosing_time_game(self, mouse_x, mouse_y, input):
        if(self.state == CHOOSING_TIME):
            # rysowanie
            self.gui.draw_choosing_time(self.amount_of_ships_to_place.values())

            # lewy przycisk myszy
            if(input.type == pygame.MOUSEBUTTONDOWN and input.button == 1):
                if(self.accept_button(mouse_x, mouse_y) == False):
                    x,y = self.mouse_to_tiles_players(mouse_x, mouse_y)

                    # sprawdzenie czy moze byc to pole dodane
                    if(self.gui.player_board.get_tile(x, y) == tiles.NOTHING):
                        # lista wolnych dlugosci statkow
                        list_of_free_ships = []
                        for i in self.amount_of_ships_to_place:
                            if(self.amount_of_ships_to_place[i] > 0):
                                list_of_free_ships.append(i)

                        if(len(self.fragments_list) == 0):
                            self.fragments_list.append((x,y))
                            self.gui.player_board.set_tile(x, y, tiles.SETTING_SHIP)
                        # sprawdzic czy mamy jeszcze wolne statki o takiej dlugosci
                        elif(len(self.fragments_list) + 1 <= max(list_of_free_ships)):
                            last_x, last_y = self.fragments_list[-1]
                            # sprawdzenie czy to pole jest pionowo/poziomo od poprzednio kliknietego/obliczenie kierunku
                            if(self.fragments_list == 1):
                                if((last_x == x and (last_y == y - 1 or last_y == y + 1)) or (last_y == y and(last_x == x - 1 or last_x == x + 1))):
                                    self.fragments_list.append((x,y))
                                    self.gui.player_board.set_tile(x, y, tiles.SETTING_SHIP)
                                    # tu obliczam kierunek
                                    x_off, y_off = self.calc_direction()
                            else:
                                # tu obliczam kierunek
                                x_off, y_off = self.calc_direction()

                                for last_x, last_y in self.fragments_list:
                                    if((last_x + x_off == x and last_y + y_off == y) or (last_x - x_off == x and last_y - y_off == y)):
                                        self.fragments_list.append((x,y))
                                        self.gui.player_board.set_tile(x, y, tiles.SETTING_SHIP)
                                        break

                else:
                    for amount in self.amount_of_ships_to_place:
                        if(self.amount_of_ships_to_place[amount] > 0):
                            if len(self.fragments_list) == self.amount_of_ships[amount]:
                                # zamiana SETTING_SHIP na front/middle/back_ship
                                self.change_setting_ship_to_ships()
                                # odjecie liczby statkow o danej dlugosci od statkow, ktore jeszcze mozemy postawic
                                self.amount_of_ships_to_place[len(self.fragments_list)] -= 1
                                # czyszczenie listy fragmentow
                                self.fragments_list.clear()

                    # koniec ukladania statkow, gdy wszystkie statki zostaly ustawione
                    if(max(self.amount_of_ships_to_place.values()) == 0):
                        # zamiana SETTING_SHIP na front/middle/back_ship
                        self.state = DURING_GAME
                        self.gui.draw_during_game()
                
            # prawy przycisk myszy - usuwanie zaznaczonego pola
            elif(input.type == pygame.MOUSEBUTTONDOWN and input.button == 3):
                x,y = self.mouse_to_tiles_players(mouse_x, mouse_y)
                
                if((x,y) in self.fragments_list):
                    if(len(self.fragments_list) == 1):
                        self.gui.player_board.set_tile(x, y, tiles.NOTHING)
                        self.fragments_list.pop()
                    elif(len(self.fragments_list) > 1):
                        # tu obliczam kierunek
                        x_off, y_off = self.calc_direction()

                        # sprawdzenie czy i poprzedni i nastepny nie sa juz zajete
                        if x_off == 0:
                            if x == 0 or x == 9 or self.gui.player.board.get_tile(x + 1, y) == tiles.NOTHING or self.gui.player.board.get_tile(x - 1, y) == tiles.NOTHING:
                                self.gui.player_board.set_tile(x, y, tiles.NOTHING)
                                self.fragments_list.remove((x,y))
                        elif y_off == 0:
                            if y == 0 or y == 9 or self.gui.player.board.get_tile(x, y + 1) == tiles.NOTHING or self.gui.player.board.get_tile(x, y - 1) == tiles.NOTHING:
                                self.gui.player_board.set_tile(x, y, tiles.NOTHING)
                                self.fragments_list.remove((x,y))
                    
    def update(self, x_mouse, y_mouse):
        # sprawdzenie czy kliknieto w przycisk accpet
        # update trafionych pol - czy cos trafilismy czy nie
        pass
    
    def placements(self, input):
        pass

    def during_game(self, input):
        pass

    def after_game(self, input):
        pass

    def shoot_player_ships(self):
        pass