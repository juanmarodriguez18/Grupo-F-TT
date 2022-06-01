



from itertools import count
import pygame


pygame.init()


clock = pygame.time.Clock()
fps=60
verde=(0,255,0)
negro=(0,0,0)

LargoPantalla= 1353
AnchoPantalla=600
Partemano=100

screen = pygame.display.set_mode((LargoPantalla,AnchoPantalla+Partemano),0,32)


fondo = pygame.image.load('imagenes/tableroPrueba.png').convert_alpha()
botonmov= pygame.image.load('imagenes/mover.png')

class cartaOfen():
    def __init__(self,daño,rangoMax,rangoMin):
        self.daño=daño
        self.rangoMax=rangoMax
        self.rangoMin=rangoMin

class carta():
    def __init__(self,nombre,tipoCarta):
        self.nombre=nombre
        self.carta=tipoCarta
        self.foto=pygame.image.load(f'imagenes/{self.nombre}.png')

    def dibujar(self,x,y):
        screen.blit(self.foto,(x,y))    

class personaje():
    def __init__(self,x,y,nombre,vidMax,mov,vel,mazo):
        self.nombre=nombre
        self.vidMax=vidMax
        self.vid=vidMax
        self.mov=mov
        self.vel=vel
        self.jugo=False
        self.carta= pygame.image.load(f'imagenes/{self.nombre}.png')
        self.mazo=mazo

    def turno(self):
        self.jugo=False
        pass

    def toca(self):
        pass

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
        screen.blit(botonmov,(self.x,self.y))

    def mover(per:personaje ,pos)  :
        pass
    
    
null=personaje(0,0,"null",0,0,0,[])
per1=personaje(0,0,"Espadachin",10,2,4,[carta('Espadachin',cartaOfen(3,1,0)),carta('Espadachin',cartaOfen(3,1,0))])
per2=personaje(0,0,"Espadachin",10,2,3,[carta('Espadachin',cartaOfen(3,1,0))])
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
pos2A=posicion(500,220.5,2,1,per2)
pos3A=posicion(830,220.75,3,1,null)
pos4A=posicion(1170,220,4,1,null)
pos1B=posicion(169,380,1,2,null)
pos2B=posicion(500,380,2,2,null)
pos3B=posicion(830,380,3,2,null)
pos4B=posicion(1170,380,4,2,null)

posiciones=[pos1A,pos2A,pos3A,pos4A,pos1B,pos2B,pos3B,pos4B]
turnos=[]

def agregarturnos(turnos,posiciones):
    for i in range(8):
        per=personaje(0,0,"null",0,0,0,[])
        for j in posiciones:
            if j.pers.vel>=per.vel and j.pers.jugo==False:
                if j.pers.vel>per.vel or (j.pers.vel==per.vel and j.pers.vid<=per.vid):
                    per=j.pers
        per.jugo=True                
        turnos.append(per)                

def dibFondo():
    screen.blit(fondo,(0,0))
    pygame.draw.rect(screen,negro,(0,AnchoPantalla-Partemano/2,LargoPantalla,150))
    
boton=BotonMov(1203,AnchoPantalla-Partemano/2)
run = True
clik=False
espacio=0
posmouse=[]
toca=0

agregarturnos(turnos,posiciones)


while run:
    clock.tick(fps)

    dibFondo()
    boton.dibujar()
    
    for i in posiciones:
        i.dibujar()
    
    espacio=0
    for i in turnos[toca].mazo:
        i.dibujar(espacio,AnchoPantalla-Partemano/2)
        espacio += 150

    if clik==True and AnchoPantalla-Partemano/2<=posmouse[1]<=AnchoPantalla+Partemano:
        espacio=0
        mano:carta=[]
        mano=turnos[toca].mazo
        i=0
        while i<mano.__len__():
            if espacio<=posmouse[0] and posmouse[0]<=espacio+150:
                turnos[toca].turno()
                if toca<=8:
                    toca +=1
                else: 
                    toca=0  
                break               
            else:
                espacio +=150 
            i +=1       
    
        

    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clik=True
            posmouse=pygame.mouse.get_pos()
        else:
            clik=False    
            posmouse=(0,0)

    pygame.display.update()

pygame.quit
