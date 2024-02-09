import pygame

NOTHING = 0
MISS = 1
HIT = 2
HIT_AND_SUNK = 3

FRONT_SHIP_V = 4
BACK_SHIP_V = 5
MIDDLE_SHIP_V = 6

FRONT_SHIP_H = 7
BACK_SHIP_H = 8
MIDDLE_SHIP_H = 9

SETTING_SHIP = 10

FRONT_SHIP_H_HIT = 11
BACK_SHIP_H_HIT = 12
MIDDLE_SHIP_H_HIT = 13

FRONT_SHIP_V_HIT = 14
BACK_SHIP_V_HIT = 15
MIDDLE_SHIP_V_HIT = 16

FRONT_SHIP_H_HNS = 17
BACK_SHIP_H_HNS = 18
MIDDLE_SHIP_H_HNS = 19

FRONT_SHIP_V_HNS = 20
BACK_SHIP_V_HNS = 21
MIDDLE_SHIP_V_HNS = 22

TILE_SIZE = 50
ROWS = 10
COLS = 10

PURPLE = (111, 49, 152)
OUTLINES_WIDTH = 20

WATER1_PNG = "images\\water1.png"
WATER2_PNG = "images\\water2.png"
HIT_PNG = "images\\hit.png"
HIT_AND_SUNK_PNG = "images\\hit_and_sunk.png"
MISS_PNG = "images\\miss.png"
FRONT_SHIP_PNG = "images\\front_ship.png"
MIDDLE_SHIP_PNG = "images\\middle_ship.png"


class Tile:
    def __init__(self, display, my_board, enemy_board):
        self.surface = display
        self.y_offset = 20
        self.water_stage = True

        self.water_image1 = pygame.image.load(WATER1_PNG).convert_alpha()
        self.water_image1 = pygame.transform.scale(self.water_image1, (TILE_SIZE, TILE_SIZE))
        self.water_image2 = pygame.image.load(WATER2_PNG).convert_alpha()
        self.water_image2 = pygame.transform.scale(self.water_image2, (TILE_SIZE, TILE_SIZE))
        self.miss_image = pygame.image.load(MISS_PNG).convert_alpha()
        self.miss_image = pygame.transform.scale(self.miss_image, (TILE_SIZE, TILE_SIZE))
        self.hit_and_sunk_image = pygame.image.load(HIT_AND_SUNK_PNG).convert_alpha()
        self.hit_and_sunk_image = pygame.transform.scale(self.hit_and_sunk_image, (TILE_SIZE, TILE_SIZE))
        self.hit_image = pygame.image.load(HIT_PNG).convert_alpha()
        self.hit_image = pygame.transform.scale(self.hit_image, (TILE_SIZE, TILE_SIZE))
    
        # tylko plansza gracza
        self.my_board = my_board
        self.mb_x_offset = 20

        self.front_ship_image = pygame.image.load(FRONT_SHIP_PNG).convert_alpha()
        self.front_ship_image = pygame.transform.scale(self.front_ship_image, (TILE_SIZE, TILE_SIZE))
        self.middle_ship_image = pygame.image.load(MIDDLE_SHIP_PNG).convert_alpha()
        self.middle_ship_image = pygame.transform.scale(self.middle_ship_image, (TILE_SIZE, TILE_SIZE))
        
        # tylko plansza przeciwnika
        self.enemy_board = enemy_board
        self.eb_x_offset = 560

        # polozenie accept button
        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0


    def draw_board(self):
        for row in range(ROWS):
            for col in range(COLS):
                my_x = col * TILE_SIZE + self.mb_x_offset
                y = row * TILE_SIZE + self.y_offset
                enemy_x = col * TILE_SIZE + self.eb_x_offset

                if(self.water_stage):
                    self.surface.blit(self.water_image1, (my_x, y))
                    self.surface.blit(self.water_image1, (enemy_x, y))
                else:
                    self.surface.blit(self.water_image2, (my_x, y))
                    self.surface.blit(self.water_image2, (enemy_x, y))


    def draw_tiles_choosing_time(self):
        for row in range(ROWS):
            for col in range(COLS):
                x = col * TILE_SIZE + self.mb_x_offset
                y = row * TILE_SIZE + self.y_offset

                # jedno zmienia sie w drugie jak zatwierdzimy ze tu jest statek
                if(self.my_board.get_tile(row, col) == SETTING_SHIP):
                    self.surface.blit(self.front_ship_image, (x, y))
                elif(self.my_board.get_tile(row, col) == FRONT_SHIP_H or self.my_board.get_tile(row, col) == MIDDLE_SHIP_H or self.my_board.get_tile(row, col) == BACK_SHIP_H or self.my_board.get_tile(row, col) == FRONT_SHIP_V or self.my_board.get_tile(row, col) == MIDDLE_SHIP_V or self.my_board.get_tile(row, col) == BACK_SHIP_V):
                    self.surface.blit(self.middle_ship_image, (x, y))


    def draw_tiles(self):
        for row in range(ROWS):
            for col in range(COLS):
                my_x = col * TILE_SIZE + self.mb_x_offset
                y = row * TILE_SIZE + self.y_offset
                enemy_x = col * TILE_SIZE + self.eb_x_offset

                if(self.my_board.get_tile(row, col) == MISS):
                    self.surface.blit(self.miss_image, (my_x, y))

                elif(self.my_board.get_tile(row, col) == FRONT_SHIP_H or self.my_board.get_tile(row, col) == FRONT_SHIP_H_HIT or self.my_board.get_tile(row, col) == FRONT_SHIP_H_HNS):
                    rotated_image = pygame.transform.rotate(self.front_ship_image, 90)
                    self.surface.blit(rotated_image, (my_x, y))
                    if(self.my_board.get_tile(row, col) == FRONT_SHIP_H_HIT):
                        self.surface.blit(self.hit_image, (my_x, y))
                    elif(self.my_board.get_tile(row, col) == FRONT_SHIP_H_HNS):
                        self.surface.blit(self.hit_and_sunk_image, (my_x, y))
                elif(self.my_board.get_tile(row, col) == MIDDLE_SHIP_H or self.my_board.get_tile(row, col) == MIDDLE_SHIP_H_HIT or self.my_board.get_tile(row, col) == MIDDLE_SHIP_H_HNS):
                    rotated_image = pygame.transform.rotate(self.middle_ship_image, 90)
                    self.surface.blit(rotated_image, (my_x, y))
                    if(self.my_board.get_tile(row, col) == MIDDLE_SHIP_H_HIT):
                        self.surface.blit(self.hit_image, (my_x, y))
                    elif(self.my_board.get_tile(row, col) == MIDDLE_SHIP_H_HNS):
                        self.surface.blit(self.hit_and_sunk_image, (my_x, y))
                elif(self.my_board.get_tile(row, col) == BACK_SHIP_H or self.my_board.get_tile(row, col) == BACK_SHIP_H_HIT or self.my_board.get_tile(row, col) == BACK_SHIP_H_HNS):
                    rotated_image = pygame.transform.rotate(self.front_ship_image, -90)
                    self.surface.blit(rotated_image, (my_x, y))
                    if(self.my_board.get_tile(row, col) == BACK_SHIP_H_HIT):
                        self.surface.blit(self.hit_image, (my_x, y))
                    elif(self.my_board.get_tile(row, col) == BACK_SHIP_H_HNS):
                        self.surface.blit(self.hit_and_sunk_image, (my_x, y))

                elif(self.my_board.get_tile(row, col) == FRONT_SHIP_V or self.my_board.get_tile(row, col) == FRONT_SHIP_V_HIT or self.my_board.get_tile(row, col) == FRONT_SHIP_V_HNS):
                    self.surface.blit(self.front_ship_image, (my_x, y))
                    if(self.my_board.get_tile(row, col) == FRONT_SHIP_V_HIT):
                        self.surface.blit(self.hit_image, (my_x, y))
                    elif(self.my_board.get_tile(row, col) == FRONT_SHIP_V_HNS):
                        self.surface.blit(self.hit_and_sunk_image, (my_x, y))
                elif(self.my_board.get_tile(row, col) == MIDDLE_SHIP_V or self.my_board.get_tile(row, col) == MIDDLE_SHIP_V_HIT or self.my_board.get_tile(row, col) == MIDDLE_SHIP_V_HNS):
                    self.surface.blit(self.middle_ship_image, (my_x, y))
                    if(self.my_board.get_tile(row, col) == MIDDLE_SHIP_V_HIT):
                        self.surface.blit(self.hit_image, (my_x, y))
                    elif(self.my_board.get_tile(row, col) == MIDDLE_SHIP_V_HNS):
                        self.surface.blit(self.hit_and_sunk_image, (my_x, y))
                elif(self.my_board.get_tile(row, col) == BACK_SHIP_V or self.my_board.get_tile(row, col) == BACK_SHIP_V_HIT or self.my_board.get_tile(row, col) == BACK_SHIP_V_HNS):
                    rotated_image = pygame.transform.rotate(self.front_ship_image, 180)
                    self.surface.blit(rotated_image, (my_x, y))
                    if(self.my_board.get_tile(row, col) == BACK_SHIP_V_HIT):
                        self.surface.blit(self.hit_image, (my_x, y))
                    elif(self.my_board.get_tile(row, col) == BACK_SHIP_V_HNS):
                        self.surface.blit(self.hit_and_sunk_image, (my_x, y))
                

                # teraz dla planszy przeciwnika
                if(self.enemy_board.get_tile(row, col) == MISS):
                    self.surface.blit(self.miss_image, (enemy_x, y))
                elif(self.enemy_board.get_tile(row, col) == HIT):
                    self.surface.blit(self.hit_image, (enemy_x, y))
                elif(self.enemy_board.get_tile(row, col) == HIT_AND_SUNK):
                    self.surface.blit(self.hit_and_sunk_image, (enemy_x, y))
                    
                elif(self.enemy_board.get_tile(row, col) == FRONT_SHIP_H_HNS):
                    rotated_image = pygame.transform.rotate(self.front_ship_image, 90)
                    self.surface.blit(rotated_image, (enemy_x, y))
                    self.surface.blit(self.hit_and_sunk_image, (enemy_x, y))
                elif(self.enemy_board.get_tile(row, col) == MIDDLE_SHIP_H_HNS):
                    rotated_image = pygame.transform.rotate(self.middle_ship_image, 90)
                    self.surface.blit(rotated_image, (enemy_x, y))
                    self.surface.blit(self.hit_and_sunk_image, (enemy_x, y))
                elif(self.enemy_board.get_tile(row, col) == BACK_SHIP_H_HNS):
                    rotated_image = pygame.transform.rotate(self.front_ship_image, -90)
                    self.surface.blit(rotated_image, (enemy_x, y))
                    self.surface.blit(self.hit_and_sunk_image, (enemy_x, y))

                elif(self.enemy_board.get_tile(row, col) == FRONT_SHIP_V_HNS):
                    self.surface.blit(self.front_ship_image, (enemy_x, y))
                    self.surface.blit(self.hit_and_sunk_image, (enemy_x, y))
                elif(self.enemy_board.get_tile(row, col) == MIDDLE_SHIP_V_HNS):
                    self.surface.blit(self.middle_ship_image, (enemy_x, y))
                    self.surface.blit(self.hit_and_sunk_image, (enemy_x, y))
                elif(self.enemy_board.get_tile(row, col) == BACK_SHIP_V_HNS):
                    rotated_image = pygame.transform.rotate(self.front_ship_image, 180)
                    self.surface.blit(rotated_image, (enemy_x, y))
                    self.surface.blit(self.hit_and_sunk_image, (enemy_x, y))
                     

    def draw_outlines(self):
        pygame.draw.rect(self.surface, PURPLE, (self.mb_x_offset - OUTLINES_WIDTH, 0, COLS * TILE_SIZE + 2 * OUTLINES_WIDTH, ROWS * TILE_SIZE + 2 * OUTLINES_WIDTH), 20)
        # TODO: tu moze byc zle
        pygame.draw.rect(self.surface, PURPLE, (self.eb_x_offset - OUTLINES_WIDTH, 0, COLS * TILE_SIZE + 2 * OUTLINES_WIDTH, ROWS * TILE_SIZE + 2 * OUTLINES_WIDTH), 20)

    
    def draw_confirm_button(self):
        confirm_text = "ACCEPT"
        self.text_with_outlines(confirm_text, 18, self.surface.get_width() - 120, ((self.surface.get_height() - 540) / 2) + 540)

        font_w = pygame.font.Font(None, 20)
        text_white = font_w.render(confirm_text, True, (255, 255, 255))
        # przesuwamy biały tekst
        text_white_rect = text_white.get_rect(center=(self.screen_width - 150 + 2, self.screen_height - 25 + 2))
        # nie jest to najlepsze wyjscie ale dopisalem do klasy board pola ktore przechowaja polozenie
        self.set_x1(text_white_rect.left)
        self.set_x2(text_white_rect.right)
        self.set_y1(text_white_rect.top)
        self.set_y2(text_white_rect.bottom)

        pygame.draw.rect(self.surface, (255, 255, 255), text_white_rect, 4)

    def draw_bottom_bar(self, ship_list):
        text = ""
        count = 5
        for val in ship_list:
            text += f"{count}x - {val}"
            count -= 1

        self.text_with_outlines(text, 16, 180, ((self.surface.get_height - 540) / 2) + 540)

    def fill_bottom_black(self):
        pygame.draw.rect(self.surface, (0, 0, 0), (0, 540, self.surface.get_width(), self.surface.get_height() - 540))

    def draw_during_game(self, ship_list):
        self.draw_outlines()
        self.fill_bottom_black()

        self.draw_board()
        self.draw_tiles()

        self.draw_bottom_bar(ship_list)
        self.draw_confirm_button()

    def draw_choosing_time(self, ship_list):
        self.draw_outlines()
        self.fill_bottom_black()

        self.draw_board()
        self.draw_tiles_choosing_time()

        self.draw_bottom_bar(ship_list)
        self.draw_confirm_button()

    def draw_before_game(self):
        pygame.draw.rect(self.surface, (0, 0, 0), (0, 540, self.surface.get_width(), self.surface.get_height()))
        text1 = "Welcome to Battleships"
        text2 = "Press enter to continue"
        self.text_with_outlines(text1, 48, self.surface.get_width() / 2, self.surface.get_height() / 2 - 50)
        self.text_with_outlines(text2, 24, self.surface.get_width() / 2, self.surface.get_height() / 2 + 50)

    def draw_after_game(self, was_won):
        pygame.draw.rect(self.surface, (0, 0, 0), (0, 540, self.surface.get_width(), self.surface.get_height()))
        if(was_won):
            text = "YOU WON!"
        else:
            text = "YOU LOST!"

        text2 = "Press enter to play again"
        
        self.text_with_outlines(text, 48, self.surface.get_width() / 2, self.surface.get_height() / 2 - 50)
        self.text_with_outlines(text2, 24, self.surface.get_width() / 2, self.surface.get_height() / 2 + 50)

    def text_with_outlines(self, text, text_size, place_x, place_y):
        font_b = pygame.font.Font(None, text_size)
        font_w = pygame.font.Font(None, text_size + 2)

        text_black = font_b.render(text, True, (0, 0, 0))
        text_white = font_w.render(text, True, (255, 255, 255))

        text_black_rect = text_black.get_rect(center=(place_x, place_y))
        text_white_rect = text_white.get_rect(center=(place_x + 2, place_y + 2))

        self.surface.blit(text_white, text_white_rect)
        self.surface.blit(text_black, text_black_rect)


    def set_x1(self, val):
        self.x1 = val
    def set_x2(self, val):
        self.x2 = val
    def set_y1(self, val):
        self.y1 = val
    def set_y2(self, val):
        self.y2 = val

    def get_x1(self):
        return self.x1
    def get_x2(self):
        return self.x2
    def get_y1(self):
        return self.y1
    def get_y2(self):
        return self.y2