
from turtle import pos
import pygame
import objeto
pygame.init()

white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)
font = None
clock = pygame.time.Clock()
fps=60


def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
 
    return newText


def armar(screen,largoPantalla,anchoPantalla):
    titulo=text_format("MAZOS",font,75,black)
    text_solo=text_format("Solo",font,75,black) 
    text_multiple=text_format("Multiple",font,75,black)
    text_Salir=text_format("Salir",font,75,black)
    titulo_rect=titulo.get_rect()
    solo_rect=text_solo.get_rect()
    multiple_rect=text_multiple.get_rect()
    salir_rect=text_Salir.get_rect()

    run=True
    posmouse=[]
    while run==True:
        posmouse=pygame.mouse.get_pos()
        pygame.display.update()
        

        if largoPantalla/2 - (solo_rect[2]/2)<=posmouse[0]<=largoPantalla/2+(solo_rect[2]/2) and 300<=posmouse[1]<=300+solo_rect[3]:
            text_solo=text_format("Solo",font,75,white)
        else:
            text_solo=text_format("Solo",font,75,black)
        if largoPantalla/2 - (multiple_rect[2]/2)<=posmouse[0]<=largoPantalla/2+(multiple_rect[2]/2) and 360<=posmouse[1]<=360+multiple_rect[3]:
            text_multiple=text_format("Multiple",font,75,white)
        else:
            text_multiple=text_format("Multiple",font,75,black)  
        if largoPantalla/2 - (salir_rect[2]/2)<=posmouse[0]<=largoPantalla/2 + (salir_rect[2]/2) and 420<=posmouse[1]<=420+salir_rect[3]:
            text_Salir=text_format("Salir",font,75,white)
        else:
            text_Salir=text_format("Salir",font,75,black)


        screen.blit(titulo,(largoPantalla/2-(titulo_rect[2]/2),80))
        screen.blit(text_solo,(largoPantalla/2-(solo_rect[2]/2),300))
        screen.blit(text_multiple,(largoPantalla/2-(multiple_rect[2]/2),360))
        screen.blit(text_Salir,(largoPantalla/2-(salir_rect[2]/2),420))        



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                clik=True
            else:
                clik=False    

        pass
    pygame.quit




