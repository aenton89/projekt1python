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
SET_SHIP = 11

FRONT_SHIP_H_HIT = 12
BACK_SHIP_H_HIT = 13
MIDDLE_SHIP_H_HIT = 14

FRONT_SHIP_V_HIT = 15
BACK_SHIP_V_HIT = 16
MIDDLE_SHIP_V_HIT = 17

FRONT_SHIP_H_HNS = 18
BACK_SHIP_H_HNS = 19
MIDDLE_SHIP_H_HNS = 20

FRONT_SHIP_V_HNS = 21
BACK_SHIP_V_HNS = 22
MIDDLE_SHIP_V_HNS = 23

BOARD_SIZE = 10
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
    def __init__(self, display, player_board = True):
        self.board = [[NOTHING] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.surface = display
        self.player_board = player_board
        self.y_offset = 20
        self.pregame = True
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
        if(player_board):
            self.x_offset = 20
            self.front_ship_image = pygame.image.load(FRONT_SHIP_PNG).convert_alpha()
            self.front_ship_image = pygame.transform.scale(self.front_ship_image, (TILE_SIZE, TILE_SIZE))
            self.middle_ship_image = pygame.image.load(MIDDLE_SHIP_PNG).convert_alpha()
            self.middle_ship_image = pygame.transform.scale(self.middle_ship_image, (TILE_SIZE, TILE_SIZE))
        else:
            self.x_offset = 560


    def set_tile(self, row, col, value):
        self.board[row][col] = value


    def set_if_pregame(self, is_pregame):
        self.pregame = is_pregame


    def draw_board(self, first_stage):
        for row in range(ROWS):
            for col in range(COLS):
                x = col * TILE_SIZE + self.x_offset
                y = row * TILE_SIZE + self.y_offset

                if(first_stage):
                    self.surface.blit(self.water_image1, (x, y))
                else:
                    self.surface.blit(self.water_image2, (x, y))
    

    def draw_tiles(self):
        if(self.pregame):
            if(self.player_board):
                for row in range(ROWS):
                    for col in range(COLS):
                        x = col * TILE_SIZE + self.x_offset
                        y = row * TILE_SIZE + self.y_offset

                        if(self.board[row][col] == SETTING_SHIP):
                            self.surface.blit(self.hit_image, (x, y))
                        elif(self.board[row][col] == SET_SHIP):
                            self.surface.blit(self.hit_and_sunk_image, (x, y))
            else:
                pass
        else:
            if(self.player_board):  # TODO: - rysowanie dla tego co przeciwnik trafil tez - korzystac z front_ship_image = pygame.transform.rotate
                for row in range(ROWS):
                    for col in range(COLS):
                        x = col * TILE_SIZE + self.x_offset
                        y = row * TILE_SIZE + self.y_offset

                        if(self.board[row][col] == MISS):
                            self.surface.blit(self.miss_image, (x, y))

                        elif(self.board[row][col] == FRONT_SHIP_H or self.board[row][col] == FRONT_SHIP_H_HIT or self.board[row][col] == FRONT_SHIP_H_HNS):
                            rotated_image = pygame.transform.rotate(self.front_ship_image, 90)
                            self.surface.blit(rotated_image, (x, y))
                            if(self.board[row][col] == FRONT_SHIP_H_HIT):
                                self.surface.blit(self.hit_image, (x, y))
                            elif(self.board[row][col] == FRONT_SHIP_H_HNS):
                                self.surface.blit(self.hit_and_sunk_image, (x, y))
                        elif(self.board[row][col] == MIDDLE_SHIP_H or self.board[row][col] == MIDDLE_SHIP_H_HIT or self.board[row][col] == MIDDLE_SHIP_H_HNS):
                            rotated_image = pygame.transform.rotate(self.middle_ship_image, 90)
                            self.surface.blit(rotated_image, (x, y))
                            if(self.board[row][col] == MIDDLE_SHIP_H_HIT):
                                self.surface.blit(self.hit_image, (x, y))
                            elif(self.board[row][col] == MIDDLE_SHIP_H_HNS):
                                self.surface.blit(self.hit_and_sunk_image, (x, y))
                        elif(self.board[row][col] == BACK_SHIP_H or self.board[row][col] == BACK_SHIP_H_HIT or self.board[row][col] == BACK_SHIP_H_HNS):
                            rotated_image = pygame.transform.rotate(self.front_ship_image, -90)
                            self.surface.blit(rotated_image, (x, y))
                            if(self.board[row][col] == BACK_SHIP_H_HIT):
                                self.surface.blit(self.hit_image, (x, y))
                            elif(self.board[row][col] == BACK_SHIP_H_HNS):
                                self.surface.blit(self.hit_and_sunk_image, (x, y))
                        
                        elif(self.board[row][col] == FRONT_SHIP_V or self.board[row][col] == FRONT_SHIP_V_HIT or self.board[row][col] == FRONT_SHIP_V_HNS):
                            self.surface.blit(self.front_ship_image, (x, y))
                            if(self.board[row][col] == FRONT_SHIP_V_HIT):
                                self.surface.blit(self.hit_image, (x, y))
                            elif(self.board[row][col] == FRONT_SHIP_V_HNS):
                                self.surface.blit(self.hit_and_sunk_image, (x, y))
                        elif(self.board[row][col] == MIDDLE_SHIP_V or self.board[row][col] == MIDDLE_SHIP_V_HIT or self.board[row][col] == MIDDLE_SHIP_V_HNS):
                            self.surface.blit(self.middle_ship_image, (x, y))
                            if(self.board[row][col] == MIDDLE_SHIP_V_HIT):
                                self.surface.blit(self.hit_image, (x, y))
                            elif(self.board[row][col] == MIDDLE_SHIP_V_HNS):
                                self.surface.blit(self.hit_and_sunk_image, (x, y))
                        elif(self.board[row][col] == BACK_SHIP_V or self.board[row][col] == BACK_SHIP_V_HIT or self.board[row][col] == BACK_SHIP_V_HNS):
                            rotated_image = pygame.transform.rotate(self.front_ship_image, 180)
                            self.surface.blit(rotated_image, (x, y))
                            if(self.board[row][col] == BACK_SHIP_V_HIT):
                                self.surface.blit(self.hit_image, (x, y))
                            elif(self.board[row][col] == BACK_SHIP_V_HNS):
                                self.surface.blit(self.hit_and_sunk_image, (x, y))

            else:
                for row in range(ROWS):
                    for col in range(COLS):
                        x = col * TILE_SIZE + self.x_offset
                        y = row * TILE_SIZE + self.y_offset

                        if(self.board[row][col] == MISS):
                            self.surface.blit(self.miss_image, (x, y))
                        elif(self.board[row][col] == HIT):
                            self.surface.blit(self.hit_image, (x, y))
                        elif(self.board[row][col] == HIT_AND_SUNK):
                            self.surface.blit(self.hit_and_sunk_image, (x, y))

                        elif(self.board[row][col] == FRONT_SHIP_H_HNS):
                            rotated_image = pygame.transform.rotate(self.front_ship_image, 90)
                            self.surface.blit(rotated_image, (x, y))
                            self.surface.blit(self.hit_and_sunk_image, (x, y))
                        elif(self.board[row][col] == MIDDLE_SHIP_H_HNS):
                            rotated_image = pygame.transform.rotate(self.middle_ship_image, 90)
                            self.surface.blit(rotated_image, (x, y))
                            self.surface.blit(self.hit_and_sunk_image, (x, y))
                        elif(self.board[row][col] == BACK_SHIP_H_HNS):
                            rotated_image = pygame.transform.rotate(self.front_ship_image, -90)
                            self.surface.blit(rotated_image, (x, y))
                            self.surface.blit(self.hit_and_sunk_image, (x, y))

                        elif(self.board[row][col] == FRONT_SHIP_V_HNS):
                            self.surface.blit(self.front_ship_image, (x, y))
                            self.surface.blit(self.hit_and_sunk_image, (x, y))
                        elif(self.board[row][col] == MIDDLE_SHIP_V_HNS):
                            self.surface.blit(self.middle_ship_image, (x, y))
                            self.surface.blit(self.hit_and_sunk_image, (x, y))
                        elif(self.board[row][col] == BACK_SHIP_V_HNS):
                            rotated_image = pygame.transform.rotate(self.front_ship_image, 180)
                            self.surface.blit(rotated_image, (x, y))
                            self.surface.blit(self.hit_and_sunk_image, (x, y))
                    

    def draw_outlines(self):
        pygame.draw.rect(self.surface, PURPLE, (self.x_offset - OUTLINES_WIDTH, 0, COLS * TILE_SIZE + 2 * OUTLINES_WIDTH, ROWS * TILE_SIZE + 2 * OUTLINES_WIDTH), 20)
    
    def draw_confirm_button(self):
        confirm_text = "ACCEPT"
        self.text_with_outlines(self, confirm_text, 18, self.surface.get_width() - 120, ((self.surface.get_height() - 540) / 2) + 540)

        font_w = pygame.font.Font(None, 20)
        text_white = font_w.render(confirm_text, True, (255, 255, 255))
        text_white_rect = text_white.get_rect(center=(self.screen_width - 150 + 2, self.screen_height - 25 + 2))  # Przesuwamy biały tekst

        pygame.draw.rect(self.surface, (255, 255, 255), text_white_rect, 4)

    def draw_bottom_bar(self, ship_list):
        text = ""
        count = 5
        for val in ship_list:
            text += f"{count}x - {val}"
            count -= 1

        self.text_with_outlines(self, text, 16, 180, ((self.surface.get_height - 540) / 2) + 540)

    def fill_bottom_black(self):
        pygame.draw.rect(self.surface, (0, 0, 0), (0, 540, self.surface.get_width(), self.surface.get_height() - 540))

    def draw_during_game(self, first_stage):
        self.draw_outlines(self)
        self.fill_bottom_black(self)

        self.draw_board(self, first_stage)
        self.draw_tiles(self)

        self.draw_bottom_bar(self)
        self.draw_confirm_button(self)

    def draw_before_game(self):
        pygame.draw.rect(self.surface, (0, 0, 0), (0, 540, self.surface.get_width(), self.surface.get_height()))
        text1 = "Welcome to Battleships"
        text2 = "Press enter to continue"
        self.text_with_outlines(self, text1, 48, self.surface.get_width() / 2, self.surface.get_height() / 2 - 50)
        self.text_with_outlines(self, text2, 24, self.surface.get_width() / 2, self.surface.get_height() / 2 + 50)

    def draw_after_game(self, was_won):
        pygame.draw.rect(self.surface, (0, 0, 0), (0, 540, self.surface.get_width(), self.surface.get_height()))
        if(was_won):
            text = "YOU WON!"
        else:
            text = "YOU LOST!"
        
        self.text_with_outlines(self, text, 48, self.surface.get_width() / 2, self.surface.get_height() / 2)

    def text_with_outlines(self, text, text_size, place_x, place_y):
        font_b = pygame.font.Font(None, text_size)
        font_w = pygame.font.Font(None, text_size + 2)

        text_black = font_b.render(text, True, (0, 0, 0))
        text_white = font_w.render(text, True, (255, 255, 255))

        text_black_rect = text_black.get_rect(center=(place_x, place_y))
        text_white_rect = text_white.get_rect(center=(place_x + 2, place_y + 2))

        self.surface.blit(text_white, text_white_rect)
        self.surface.blit(text_black, text_black_rect)