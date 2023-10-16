import pygame
import sys
import time

SCREEN_WIDTH = 64
SCREEN_HEIGHT = 64
PIXEL_SIZE = 4

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH * PIXEL_SIZE, SCREEN_HEIGHT * PIXEL_SIZE))
pygame.display.set_caption("Desenho")
drawing_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
drawing_surface.fill((0, 0, 0))
BLACK = (255, 255, 255)
drawing = False

PEN_SIZE = 3

n = 200
p = 0

last_save_time = 0 
while True:
    current_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                x, y = event.pos
                x //= PIXEL_SIZE
                y //= PIXEL_SIZE
                pygame.draw.rect(drawing_surface, BLACK, (x, y, PEN_SIZE, PEN_SIZE))

    pygame.transform.scale(drawing_surface, (SCREEN_WIDTH * PIXEL_SIZE, SCREEN_HEIGHT * PIXEL_SIZE), screen)
    pygame.display.flip()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_s] and current_time - last_save_time >= 2:
        last_save_time = current_time
        n += 1
        name = f"../data/n{p}/n{p}_{n}.png"
        pygame.image.save(drawing_surface, name)
        print(f"Desenho salvo como '{name}'")
        drawing_surface.fill((0, 0, 0))

        if n == 250:
            n = 150
            p += 1

    pygame.time.delay(10)
