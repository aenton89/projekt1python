import pygame
import sys

import board
import tiles
import logic

# rozmiar okna
WIDTH = 1150
HEIGHT = 700
#  liczba klatek
FPS = 60
# stany gry
MENU = 1
PLACEMENT = 2
GAME = 3
END = 4




# inicjalizacja pygame
pygame.init()

# ustawienia okna gry oraz zegar
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gra w statki")
clock = pygame.time.Clock()

# tworzenie obiektow klas
my_board = board.Board()
enemy_board = board.Board()
tile = tiles.Tile(my_board, enemy_board, screen)
logics = logic.Logic(my_board, enemy_board)

# licznik klatek
frame_counter = 0
frames_per_image_change = 60 * 1.5


# stan gry
state = MENU




# glowna petla gry
while True:
    for event in pygame.event.get():
        # wyjscie z gry
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # wypelnij ekran kolorem bialym
    screen.fill((255, 255, 255))


    # update wody
    if(frame_counter % frames_per_image_change == 0):
        tile.update_water()


    # w zaleznosci od stanu gry
    if(state == MENU):
        tile.draw_1()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                state = PLACEMENT


    elif(state == PLACEMENT):
        tile.draw_2(logics.ships_to_place)

        # prawy/lewy przycisk - rozstawianie statkow
        if(event.type == pygame.MOUSEBUTTONDOWN):
            mouse_button = event.button
            if(mouse_button == 1 or mouse_button == 3):
                x, y = pygame.mouse.get_pos()
                if(x >= 50 and x <= 550 and y >= 50 and y <= 550):
                    x, y = get_my_tile_coords(x, y)
                    if(mouse_button == 1):
                        logics.place_ship(x, y)
                    elif(mouse_button == 3):
                        logics.remove_ship(x, y)

        # enter - zakonczenie rozstawiania tego jednego statku
        elif(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_RETURN):
                logics.accept_ship()
                # sprawdzenie czy wszystkie statki zostaly juz rozstawione
                if(logics.check_if_all_ships_placed()):
                    state = GAME
                    logics.place_ship_computer()

        
    elif(state == GAME):
        tile.draw_3(logics.ships_to_sunk)

        # strzal - lewy przycisk
        if(logics.turn == logic.PLAYER):
            if(event.type == pygame.MOUSEBUTTONDOWN):
                mouse_button = event.button
                if(mouse_button == 1):
                    x, y = pygame.mouse.get_pos()
                    if(x >= 600 and x <= 1100 and y >= 50 and y <= 550):
                        # TODO: POPRAWIC GET_ENEMY_TILE_COORDS - chyba juz dobrze
                        x, y = get_enemy_tile_coords(x, y)
                        logics.shoot(x, y)
        # tura komputera
        else:
            logics.shoot_computer()
        
        if(logics.check_if_end() == logic.WON or logics.check_if_end() == logic.LOST):
            state = END
            


    elif(state == END):
        tile.draw_4(logics.check_if_end() == logic.WON)

        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_RETURN):
                pygame.quit()
                sys.exit()
            


    # zlicz klatki
    frame_counter += 1
    if frame_counter >= frames_per_image_change:
        frame_counter = 0
    # aktualizacja ekranu i framerate
    pygame.display.update()
    clock.tick(FPS)




    # funkcja przeliczajaca wspolrzedne kliknietego pola na wspolrzedne w tablicy
    def get_my_tile_coords(x, y):
        print (x,y)
        x = ((x) // 50) - 1
        y = ((y) // 50) - 1
        print (x,y)
        return x, y
    
    def get_enemy_tile_coords(x, y):
        x = ((x) // 50) - 12
        y = ((y) // 50) - 1
        return x, y