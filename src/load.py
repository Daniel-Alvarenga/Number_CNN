import numpy as np
from keras.models import load_model
from PIL import Image
import matplotlib.pyplot as plt
import pygame
import time
import sys


modelo = "../models/modelo2023-09-21 19-14-55.keras"
model = load_model(modelo)

SCREEN_WIDTH = 64
SCREEN_HEIGHT = 64
PIXEL_SIZE = 4

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH * PIXEL_SIZE, SCREEN_HEIGHT * PIXEL_SIZE))
pygame.display.set_caption("Dígitos")
drawing_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
drawing_surface.fill((0, 0, 0))
BLACK = (255, 255, 255)
drawing = False

PEN_SIZE = 3
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
        teste = []
        last_save_time = current_time
        pygame.image.save(drawing_surface, '../test/image.png')
        drawing_surface.fill((0, 0, 0))
        numero = []
        valores = []
        imagem = Image.open('../test/image.png')
        largura, altura = imagem.size
        for h in range(altura):
            for w in range(largura):
                pixel = imagem.getpixel((w, h))
                valor = '#{0:02x}{1:02x}{2:02x}'.format(pixel[0], pixel[1], pixel[2])
                if valor == '#000000':
                    valor = 0
                else:
                    valor = 1
                valores.append(valor)
        numero.append(valores)
        teste.append(numero)

        teste = np.array(teste)
        teste = teste.reshape(-1, 64, 64, 1)

        teste = teste.astype('float32') / 255.0

        predictions = model.predict(np.array([teste[0]]))
        predicted_digit = np.argmax(predictions)
        print(f'Dígito previsto: {predicted_digit}')

    pygame.time.delay(10)