import pygame
import sys

pygame.init()

# Ustawienia okna gry
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pobieranie położenia myszy w Pygame")

# Główna pętla gry
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            # Pobierz aktualne położenie myszy
            mouseX, mouseY = event.pos
            print(f"Aktualne położenie myszy: ({mouseX}, {mouseY})")

    # Tutaj umieść resztę swojej logiki gry

    # Odśwież ekran
    pygame.display.flip()
