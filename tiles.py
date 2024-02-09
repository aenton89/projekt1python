import pygame

import board

TILE_SIZE = 50

WATER1_PNG = "images\\water1.png"
WATER2_PNG = "images\\water2.png"
HIT_PNG = "images\\hit.png"
HIT_AND_SUNK_PNG = "images\\hit_and_sunk.png"
MISS_PNG = "images\\miss.png"

class Tile:
    def __init__(self, my_board, enemy_board, display):
        self.surface = display
        self.my_board = my_board
        self.enemy_board = enemy_board
        # wypelnianie ekranu na bialo
        self.surface.fill((255, 255, 255))
        # offsety plansz
        self.my_board_x_offset = 50
        self.enemy_board_x_offset = 600
        self.y_offset = 50
        # stan wody
        self.water_stage = True
        # wczytanie obrazkow wody
        self.water1_image = pygame.image.load(WATER1_PNG).convert_alpha()
        self.water1_image = pygame.transform.scale(self.water1_image, (TILE_SIZE, TILE_SIZE))
        self.water2_image = pygame.image.load(WATER2_PNG).convert_alpha()
        self.water2_image = pygame.transform.scale(self.water2_image, (TILE_SIZE, TILE_SIZE))
        # wczytanie obrazkow trafienia/rozstawiania statkow
        self.hit_image = pygame.image.load(HIT_PNG).convert_alpha()
        self.hit_image = pygame.transform.scale(self.hit_image, (TILE_SIZE, TILE_SIZE))
        self.hit_and_sunk_image = pygame.image.load(HIT_AND_SUNK_PNG).convert_alpha()
        self.hit_and_sunk_image = pygame.transform.scale(self.hit_and_sunk_image, (TILE_SIZE, TILE_SIZE))
        # wczytanie obrazkow nietrafiony/strzal wroga
        self.miss_image = pygame.image.load(MISS_PNG).convert_alpha()
        self.miss_image = pygame.transform.scale(self.miss_image, (TILE_SIZE, TILE_SIZE))


    # update wody
    def update_water(self):
        if self.water_stage:
            self.water_stage = False
        else:
            self.water_stage = True


    # rysowanie ekranu poczatkowego
    def draw_1(self):
        font_title = pygame.font.Font(None, 72)
        font_subtitle = pygame.font.Font(None, 48)

        text_title = font_title.render("gra w statki", True, (0, 0, 0))
        text_subtitle = font_subtitle.render("naciśnij ENTER aby kontynuować", True, (0, 0, 0))

        title_rect = text_title.get_rect(center=(self.surface.get_rect().centerx, self.surface.get_rect().centery - 50))
        subtitle_rect = text_subtitle.get_rect(center=(self.surface.get_rect().centerx, self.surface.get_rect().centery))

        self.surface.blit(text_title, title_rect)
        self.surface.blit(text_subtitle, subtitle_rect)


    # rysowanie ekranu rozstawiania statkow
    def draw_2(self, map):
        self.draw_water()
        self.ships_left(map)

        # napis - Enter zeby zaakceptowac statek
        font = pygame.font.Font(None, 36)
        text = font.render("naciśnij ENTER, żeby zaakceptować statek, PPM, żeby cofnąć", True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.surface.get_rect().centerx, 25))
        self.surface.blit(text, text_rect)

        # rysowanie stawianych statkow
        for row in range(board.ROWS):
            for col in range(board.COLS):
                my_x = col * TILE_SIZE + self.my_board_x_offset
                y = row * TILE_SIZE + self.y_offset

                if(self.my_board.array[row][col] == board.PLACED):
                    self.surface.blit(self.hit_image, (my_x, y))
                elif(self.my_board.array[row][col] == board.ACCEPTED):
                    self.surface.blit(self.hit_and_sunk_image, (my_x, y))
    

    # rysowanie ekranu podczas rozgrywki - zatapiania
    def draw_3(self, map):
        self.draw_water()
        self.ships_left(map)
        self.draw_ships()


    # rysowanie ekranu koncowego
    def draw_4(self, did_i_win):
        font = pygame.font.Font(None, 72)
        font_subtitle = pygame.font.Font(None, 48)
        if(did_i_win):
            string_text = "WYGRAŁEŚ"
        else:
            string_text = "PRZEGRAŁEŚ"

        text = font.render(string_text, True, (0, 0, 0))
        text_subtitle = font_subtitle.render("naciśnij ENTER aby zakończyć", True, (0, 0, 0))
        
        text_rect = text.get_rect(center=(self.surface.get_rect().centerx, self.surface.get_rect().centery - 50))
        subtitle_rect = text_subtitle.get_rect(center=(self.surface.get_rect().centerx, self.surface.get_rect().centery))

        self.surface.blit(text, text_rect)
        self.surface.blit(text_subtitle, subtitle_rect)


    def draw_water(self):
        for row in range(board.ROWS):
            for col in range(board.COLS):
                my_x = col * TILE_SIZE + self.my_board_x_offset
                enemy_x = col * TILE_SIZE + self.enemy_board_x_offset
                y = row * TILE_SIZE + self.y_offset

                if(self.water_stage):
                    self.surface.blit(self.water1_image, (my_x, y))
                    self.surface.blit(self.water1_image, (enemy_x, y))
                else:
                    self.surface.blit(self.water2_image, (my_x, y))
                    self.surface.blit(self.water2_image, (enemy_x, y))


    def ships_left(self, map):
        text = ""
        for key, value in map.items():
            text += f"{key}: x{value}   "

        font = pygame.font.Font(None, 36)
        text = font.render(text, True, (0, 0, 0))
        text_rect = text.get_rect(left = 50, top = 625)
        self.surface.blit(text, text_rect)


    def draw_ships(self):
        for row in range(board.ROWS):
            for col in range(board.COLS):
                my_x = col * TILE_SIZE + self.my_board_x_offset
                enemy_x = col * TILE_SIZE + self.enemy_board_x_offset
                y = row * TILE_SIZE + self.y_offset

                # tablica gracza
                if(self.my_board.array[row][col] == board.SHIP):
                    pygame.draw.rect(self.surface, (0, 0, 0), (my_x, y, TILE_SIZE, TILE_SIZE))
                elif(self.my_board.array[row][col] == board.ENEMY_SHOT):
                    self.surface.blit(self.miss_image, (my_x, y))
                
                # tablica przeciwnika
                if(self.enemy_board.array[row][col] == board.HIT):
                    self.surface.blit(self.hit_image, (enemy_x, y))
                elif(self.enemy_board.array[row][col] == board.SUNK):
                    self.surface.blit(self.hit_and_sunk_image, (enemy_x, y))
                elif(self.enemy_board.array[row][col] == board.MISS):
                    self.surface.blit(self.miss_image, (enemy_x, y))