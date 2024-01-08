import pygame
import sys

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna gry
WIDTH = 600
HEIGHT = 600
TILE_SIZE = 60
ROWS = 10
COLS = 10

# Ustawienia planszy
board = [[0] * COLS for _ in range(ROWS)]  # Przykładowa tablica 10x10

# Inicjalizacja okna gry
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Klikanie na pola")

# Główna pętla gry
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Sprawdź lewy przycisk myszy
            # Pobierz aktualną pozycję myszy
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Sprawdź, czy kliknięcie było na polu
            clicked_row = mouse_y // TILE_SIZE
            clicked_col = mouse_x // TILE_SIZE

            # Sprawdź, czy kliknięcie było w zakresie planszy
            if 0 <= clicked_row < ROWS and 0 <= clicked_col < COLS:
                print(f"Kliknięcie na polu ({clicked_row}, {clicked_col})")

    # Wypełnij ekran kolorem białym
    screen.fill((255, 255, 255))

    # Narysuj planszę (przykład - zmień na swoją logikę rysowania)
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, (0, 0, 0), (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    # Zaktualizuj ekran
    pygame.display.flip()

    # Ustaw limit klatek na sekundę (60 FPS)
    clock.tick(60)
