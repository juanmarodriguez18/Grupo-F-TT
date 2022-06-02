



from itertools import count
import pygame


pygame.init()


clock = pygame.time.Clock()
fps=60
verde=(0,255,0)
rojo=(255,0,0)
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
    def __init__(self,nombre,tipoCarta,nomTipo):
        self.nombre=nombre
        self.carta=tipoCarta
        self.nomTipo=nomTipo
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

    def turno(self,run,posciones,i):
        #es la carta que se hizo clik
        jugada:carta=self.mazo[i]
        lineaObj=0
        posself=0
        #revisa si la carta es ofenciva/defensiva y elije en que linea se juega
        for x in posiciones:
            if x.pers==self :
                posself=x.pos
                if x.lado==1:
                    if jugada.nomTipo=="of":
                        lineaObj=2
                    else:
                        lineaObj=1
                elif x.lado==2:
                    if jugada.nomTipo=="of":
                        lineaObj=1
                    else:
                        lineaObj=2 

        clik=False
        while run==True :
            #pone en rojo los lugares que llega la carta ofenciva
            if jugada.nomTipo=="of":
                for x in posiciones:
                    if x.lado==lineaObj and ((posself+jugada.carta.rangoMax)>=x.pos>=(posself+jugada.carta.rangoMax)):
                        x.dibujar(rojo)
            

            #sige revisando los eventos
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
               

    pygame.display.update()


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

    def dibujar(self,color=verde):
        pygame.draw.circle(screen,color,(self.x,self.y),5.0)
        if self.pers.nombre != "null":
            self.pers.dibujar(self)

       
#esta roto    
class BotonMov():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def dibujar(self):
        screen.blit(botonmov,(self.x,self.y))

    def mover(per:personaje ,pos)  :
        pass
    
#personajes generales y la posicion en el array de posiciones    
null=personaje(0,0,"null",0,0,0,[])
per1=personaje(0,0,"Espadachin",10,2,4,[carta('Espadachin',cartaOfen(3,1,0),"of"),carta('Espadachin',cartaOfen(3,1,0),"of")])
per2=personaje(0,0,"Espadachin",10,2,3,[carta('Espadachin',cartaOfen(3,1,0),"of")])
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
# crea el orden de turnos
def agregarturnos(turnos,posiciones):
    for i in range(8):
        per=personaje(0,0,"null",0,0,0,[])
        for j in posiciones:
            if j.pers.vel>=per.vel and j.pers.jugo==False:
                if j.pers.vel>per.vel or (j.pers.vel==per.vel and j.pers.vid<=per.vid):
                    per=j.pers
        per.jugo=True                
        turnos.append(per)                
#funcion que dibuja el fondo
def dibFondo():
    screen.blit(fondo,(0,0))
    pygame.draw.rect(screen,negro,(0,AnchoPantalla-Partemano/2,LargoPantalla,150))

#datos generales    
boton=BotonMov(1203,AnchoPantalla-Partemano/2)
run = True
clik=False
espacio=0
posmouse=[]
toca=0
tamañoCartas=150
agregarturnos(turnos,posiciones)


while run:
    clock.tick(fps)
    #dibuja todo
    dibFondo()
    boton.dibujar()
    for i in posiciones:
        i.dibujar()
    
    espacio=0
    for i in turnos[toca].mazo:
        i.dibujar(espacio,AnchoPantalla-Partemano/2)
        espacio += tamañoCartas
    #si hubo un clik revisa si fue en una carta
    if clik==True and AnchoPantalla-Partemano/2<=posmouse[1]<=AnchoPantalla+Partemano:
        espacio=0
        mano=turnos[toca].mazo
        i=0
        while i<mano.__len__():
            if espacio<=posmouse[0]<=espacio+150:
                turnos[toca].turno(run,posiciones,i)
                if toca<=8:
                    toca +=1
                else: 
                    toca=0  
                break               
            else:
                espacio +=tamañoCartas
                i +=1
                   
    
        

    
    #esto revisa los eventos(clik y salir)
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
