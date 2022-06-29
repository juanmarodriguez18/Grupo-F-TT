import pygame
import objeto
import partida

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
posmouse=[]
clik=False


def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
 
    return newText

def main_menu(screen,largoPantalla):
    screen_width=largoPantalla
    menu=True
    posmouse=[]
    while menu:
        posmouse=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

 
        # Main Menu UI
        screen.fill(blue)
        title=text_format("Menu Principal", font, 90, yellow)
        text_start = text_format("Inicio", font, 75, black)
        text_quit = text_format("Salir", font, 75, black)
        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()

        if screen_width/2 - (start_rect[2]/2)<=posmouse[0]<=screen_width/2+(start_rect[2]/2) and 300<=posmouse[1]<=start_rect[3]+300:
            text_start=text_format("Inicio", font, 75, white)
            if clik==True:
                partida.jugar(objeto.tablero)
        else:
            text_start = text_format("Inicio", font, 75, black)
        if screen_width/2 - (quit_rect[2]/2)<=posmouse[0]<=screen_width/2+(quit_rect[2]/2) and 420<=posmouse[1]<=quit_rect[3]+420:
            text_quit=text_format("Salir", font, 75, white)
            if clik==True:
                pygame.quit()
        else:
            text_quit = text_format("Salir", font, 75, black)
 
        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()
 
        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 420))

        


        pygame.display.update()



def victoria(screen,largoPantalla,ganador):

    screen_width=largoPantalla
    menu=True
    posmouse=[]
    while menu:
        posmouse=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                clik=True
                
                

 
        # Main Menu UI
        screen.fill(blue)
        title=text_format("El Ganador es:", font, 90, yellow)
        gana=text_format(ganador,font,75,white)
        text_start = text_format("Inicio", font, 75, black)
        text_mazos = text_format("Mazos",font,75,black)
        text_quit = text_format("Salir", font, 75, black)
        title_rect=title.get_rect()
        gana_rect=gana.get_rect()
        start_rect=text_start.get_rect()
        mazos_rect=text_mazos.get_rect()
        quit_rect=text_quit.get_rect()

        if screen_width/2 - (start_rect[2]/2)<=posmouse[0]<=screen_width/2+(start_rect[2]/2) and 300<=posmouse[1]<=start_rect[3]+300:
            text_start=text_format("Revancha", font, 75, white)
            if clik==True:
                partida.jugar(objeto.tablero)
        else:
            text_start = text_format("Revancha", font, 75, black)
        if screen_width/2 - (quit_rect[2]/2)<=posmouse[0]<=screen_width/2+(quit_rect[2]/2) and 420<=posmouse[1]<=quit_rect[3]+420:
            text_quit=text_format("Salir", font, 75, white)
            if clik==True:
                pygame.quit()
        else:
            text_quit = text_format("Salir", font, 75, black)
 
        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()
 
        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 420))

        pygame.display.update()


