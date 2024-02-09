import pygame
import sys

import tiles
import logic

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna gry
WIDTH = 1200  # Szerokość okna
HEIGHT = 750  # Wysokość okna
TILE_SIZE = 50  # Rozmiar komórki
FPS = 60  # Liczba klatek na sekundę

# Ustawienia planszy
rows = 10  # Liczba wierszy
cols = 10  # Liczba kolumn

# Ścieżki do plików z obrazkami wody
water1_image_path = "images\\water1.png"
water2_image_path = "images\\water2.png"

# Inicjalizacja okna gry
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plansza z obrazkami")

# Licznik klatek
frame_counter = 0
frames_per_image_change = 60 * 0.95  # Zmiana obrazka co 0.5 sekundy przy 60 FPS

def draw_board(surface, x_offset):
    for row in range(rows):
        for col in range(cols):
            # Wybierz obrazek wody
            water_image_path = water1_image_path if frame_counter % frames_per_image_change < frames_per_image_change / 2 else water2_image_path
            water_image = pygame.image.load(water_image_path)
            
            # Przeskaluj obrazek do wymiarów komórki
            water_image = pygame.transform.scale(water_image, (TILE_SIZE, TILE_SIZE))
            
            # Ustal pozycję obrazka na planszy
            x = col * TILE_SIZE + x_offset
            y = row * TILE_SIZE + 50
            
            # Wyrysuj obrazek na ekranie
            surface.blit(water_image, (x, y))

# Główna pętla gry
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Wypełnij ekran kolorem białym
    screen.fill((255, 255, 255))

    # Narysuj pierwszą planszę
    draw_board(screen, 50)

    # Dodaj ramkę dla pierwszej planszy
    pygame.draw.rect(screen, (255, 0, 0), (50 - 20, 0, cols * TILE_SIZE + 40, rows * TILE_SIZE + 20), 20)

    # Narysuj drugą planszę
    draw_board(screen, 650)

    # Dodaj ramkę dla drugiej planszy
    pygame.draw.rect(screen, (255, 0, 0), (300 - 20, 0, cols * TILE_SIZE + 40, rows * TILE_SIZE + 20), 20)

    # Zaktualizuj ekran
    pygame.display.flip()

    # Zlicz klatki
    frame_counter += 1
    if frame_counter >= FPS:
        frame_counter = 0

    # Ustaw limit klatek na sekundę (60 FPS)
    clock.tick(60)
