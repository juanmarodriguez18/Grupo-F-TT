



import pygame


pygame.init()


clock = pygame.time.Clock()
fps=60
verde=(0,255,0)

LargoPantalla= 1353
AnchoPantalla=600
Partemano=100

screen = pygame.display.set_mode((LargoPantalla,AnchoPantalla+Partemano),0,32)


fondo = pygame.image.load('imagenes/tableroPrueba.png').convert_alpha()
botonMov= pygame.image.load('imagenes/mover.png')

class personaje():
    def __init__(self,x,y,nombre,vidMax,mov,vel):
        self.nombre=nombre
        self.vidMax=vidMax
        self.vid=vidMax
        self.mov=mov
        self.vel=vel
        self.carta= pygame.image.load(f'imagenes/{self.nombre}.png')


    def dibujar(self,posicion):   
        screen.blit(self.carta,(posicion.x-75,posicion.y-85)) 


    

class posicion():
    def __init__(self,x,y,pos,lado,pers:personaje):
        self.x=x
        self.y=y
        self.pos=pos
        self.lado=lado
        self.pers=pers

    def dibujar(self):
        pygame.draw.circle(screen,verde,(self.x,self.y),5.0)
        if self.pers.nombre != "null":
            self.pers.dibujar(self)
    
class BotonMov():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def dibujar(self):
        screen.blit(botonMov,(self.x,self.y))

    def mover(per:personaje ,pos)  :
        pass
    
    
null=personaje(0,0,"null",0,0,0)
per1=personaje(0,0,"Espadachin",10,2,4)
#per2=personaje(0,0, "Desesperada",6,1,3)
#per3=personaje(0,0,"Enfermo",10,1,3)
#per4=personaje(0,0"Bandida",12,2,2)
#per5=personaje(0,0,"Tirador",10,1,4)
#per6=personaje(0,0"Bardo",8,3,5)
#per7=personaje(0,0"Reforsado",16,1,1)
#per8=personaje(0,0,"Maniatica",8,3,4)
#per9=personaje(0,0,"Bestia",14,2,2)
#per10=personaje(0,0,"Barbaro",12,1,2)
#per11=personaje(0,0,"Cazadora",6,3,4)
#per12=personaje(0,0,"Desertor",8,2,3)
pos1A=posicion(169,220,1,1,per1)
pos2A=posicion(500,220.5,2,1,null)
pos3A=posicion(830,220.75,3,1,null)
pos4A=posicion(1170,220,4,1,null)
pos1B=posicion(169,380,1,2,null)
pos2B=posicion(500,380,5,2,2,null)
pos3B=posicion(830,380,75,3,2,null)
pos4B=posicion(1170,380,4,2,null)

posiciones=[pos1A,pos2A,pos3A,pos4A,pos1B,pos2B,pos3B,pos4B]

def dibFondo():
    screen.blit(fondo,(0,0))
boton=BotonMov(1000,AnchoPantalla-Partemano/2)
run = True

while run:
    clock.tick(fps)

    dibFondo()
    boton.dibujar()
    for i in posiciones:
        i.dibujar()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    pygame.display.update()

pygame.quit
