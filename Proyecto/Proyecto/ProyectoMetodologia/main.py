
import pygame
import objeto
import menu




obj=objeto


pygame.init()


clock = pygame.time.Clock()
fps=60
verde=(0,255,0)
azul=(0,0,255)
rojo=(255,0,0)
negro=(0,0,0)

tamañoTablero=8
LargoPantalla= 1353
AnchoPantalla=600
Partemano=100

screen = pygame.display.set_mode((LargoPantalla,AnchoPantalla+Partemano),0,32)
#menu.main_menu(screen,LargoPantalla)
menu.main_menu()


fondo = pygame.image.load('imagenes/tableroPrueba.png').convert_alpha()

       

    

