import pygame
import sys

# Inicjalizacja Pygame
pygame.init()


# Utwórz okno gry
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Nakładanie obrazków")

# Utwórz powierzchnie z przezroczystością (RGBA)
image1 = pygame.image.load("images/water1.png").convert_alpha()
image2 = pygame.image.load("images/hit.png").convert_alpha()

# Główna pętla gry
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Wypełnij ekran kolorem białym
    screen.fill((255, 255, 255))

    # Nakładaj obrazki na siebie
    screen.blit(image1, (50, 50))
    screen.blit(image2, (50, 50))

    # Zaktualizuj ekran
    pygame.display.flip()

    # Ustaw limit klatek na sekundę (60 FPS)
    clock.tick(60)
