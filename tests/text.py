import pygame
import sys

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna gry
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Napis na środku ekranu")

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ustawienia czcionki
font = pygame.font.SysFont(None, 36)
text = font.render("Napis na środku ekranu", True, BLACK)
text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Pętla główna
running = True
while running:
    WINDOW.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    # Rysowanie napisu na środku ekranu
    WINDOW.blit(text, text_rect)

    pygame.display.update()
