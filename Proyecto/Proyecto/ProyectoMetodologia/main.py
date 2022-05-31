from typing_extensions import Self
import pygame


pygame.init()


clock = pygame.time.Clock()
fps=60


LargoPantalla= 1353
AnchoPantalla=600

screen = pygame.display.set_mode((LargoPantalla,AnchoPantalla))


fondo = pygame.image.load('imagenes/tableroPrueba.png').convert_alpha()

class personaje():
    def __init__(self):
        pass

def dibFondo():
    screen.blit(fondo,(0,0))

run = True

while run:
    clock.tick(fps)

    dibFondo()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    pygame.display.update()

pygame.quit

# probando tocar el codigo