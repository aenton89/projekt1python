import pygame
import sys

import tiles

BEFORE_GAME = 0
CHOOSING_TIME = 1
DURING_GAME = 2
AFTER_GAME = 3

PLAYER_TURN = True
ENEMY_TURN = False

class Logic:
    def __init__(self, my_board, enemy_board):
        self.my_board = my_board
        self.enemy_board = enemy_board
        self.state = BEFORE_GAME
        self.turn = PLAYER_TURN

    def start_game(self, input):
        if(self.state == BEFORE_GAME):
            self.my_board.draw_before_game()
            # sprawdzenie czy wcisnieto enter
            if(input == pygame.K_RETURN): # TODO: to cale ponizej
                self.state = CHOOSING_TIME
                self.my_board.draw_during_game()
                self.enemy_board.draw_during_game()
    
    def choose_time(self, input):
        pass

    def inform_GUI_water_stage(self, first_stage):
        if(first_stage):
            self.my_board.draw_water_stage()
        else:
            self.enemy_board.draw_water_stage()


    
            

    def close(self):
        pygame.quit()
        sys.exit()
