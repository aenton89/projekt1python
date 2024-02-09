import pygame
import sys

import tiles
import logic
import board

# Inicjalizacja Pygame
pygame.init()

# Inicjalizacja okna gry
screen = pygame.display.set_mode((tiles.WIDTH, tiles.HEIGHT))
pygame.display.set_caption("Battleships")

# Inicjalizacja plansz
my_board = board.Board()
enemy_board = board.Board()

# TODO: moze przerobic tiles.py tak, zeby od razu rysowalo i my_board i enemy_board jesli robimy tylko gre pve
GUI_obj = tiles.Tiles(screen, my_board, enemy_board)    # do zmiany Tiles, zeby bylo i enemy_board i moje od razu w nim, a nie dwa oddzielne gui
LOGIC_obj = logic.Logic(my_board, enemy_board)

# w petli tez zmieniac to zeby woda sie falowala (set_water_stage())
# w petli sprawdzamy jaki mamy state gry obecnie i te metody wywolamy (mimo ze w nich tez sprawdzamy state)
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        

# podawac w logic.py do draw_during_game() liczbe statkow przeciwnika do rozbicia