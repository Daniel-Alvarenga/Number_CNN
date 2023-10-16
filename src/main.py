import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from PIL import Image
import pygame
import sys
import time
import datetime
import pytz

fusoHorario = pytz.timezone('America/Sao_Paulo')
dia_atual = (datetime.datetime.now(fusoHorario)).strftime('%Y-%m-%d %H-%M-%S')

x = []
y = []
digitos = 10
registros = 200

print("Carregando dados...")

for digito in range(digitos):
    for registro in range(registros):
        valores = []
        y.append(digito)
        arquivo = f'../data/n{digito}/n{digito}_{registro + 1}.png'
        imagem = Image.open(arquivo)
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
        x.append(valores)

x = np.array(x)
y = np.array(y)

y = to_categorical(y, num_classes=10)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.01, random_state=42)

x_train = x_train.reshape(-1, 64, 64, 1)
x_test = x_test.reshape(-1, 64, 64, 1)

x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

model = Sequential()

model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 1)))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(64, (3, 3), activation='relu'))

model.add(Flatten())

model.add(Dense(256, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=100, batch_size=256)

model.save(f"../models/modelo{dia_atual}.keras")

loss, accuracy = model.evaluate(x_test, y_test)
print(f'Acurácia no conjunto de teste: {accuracy * 100:.2f}%')

testar = input("Testar modelo recém-treinado? (0-Não)/(1-Sim)")

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
        pygame.image.save(drawing_surface, 'image.png')
        drawing_surface.fill((0, 0, 0))
        numero = []
        valores = []
        imagem = Image.open('image.png')
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