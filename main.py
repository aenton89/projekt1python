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