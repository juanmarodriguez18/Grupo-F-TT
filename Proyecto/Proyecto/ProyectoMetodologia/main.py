



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
            
null=personaje(0,0,"null",0,0,0)
per1=personaje(0,0,"Espadachin",10,2,4)
pos1A=posicion(169,220,1,1,per1)
pos2A=posicion(500,220.5,2,1,null)
pos3A=posicion(830,220.75,3,1,null)
pos4A=posicion(1170,220,4,1,null)

posiciones=[pos1A,pos2A,pos3A,pos4A]

def dibFondo():
    screen.blit(fondo,(0,0))

run = True

while run:
    clock.tick(fps)

    dibFondo()
    for i in posiciones:
        i.dibujar()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    pygame.display.update()

pygame.quit
