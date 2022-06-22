import pygame
import objeto


clock = pygame.time.Clock()
fps=60
verde=(0,255,0)
azul=(0,0,255)
rojo=(255,0,0)
negro=(0,0,0)

LargoPantalla= 1353
AnchoPantalla=600
Partemano=100

fondo = pygame.image.load('imagenes/tableroPrueba.png').convert_alpha()
botonmov= pygame.image.load('imagenes/mover.png')

screen = pygame.display.set_mode((LargoPantalla,AnchoPantalla+Partemano),0,32)
pygame.display.set_caption('Battle')


class BotonMov():
    def __init__(self,x,y):
        self.x=x
        self.y=y


    def dibujar(self):
        screen.blit(botonmov,(self.x,self.y))

    def mover(per ,pos)  :
        pass
tablero=[jug1,jug2]


for x in tablero:
    for i in x.posiciones:
        i.pers=i.pers.diferenciador()


turnos=[]
# crea el orden de turnos
def agregarturnos(turnos,tablero,tamaño):
    turnos=[]
    z=0
    while z<tamaño:
        per=objeto.personaje(0,"null",0,0,0,[])
        for i in tablero:
            
            for j in i.posiciones:
                if j.pers.vel>=per.vel and j.pers.jugo==False:
                    if j.pers.vel>per.vel or (j.pers.vel==per.vel and j.pers.vid<=per.vid):
                        j.pers.jugo=True
                        j.pers.defiende=True
                        per=j.pers                
        turnos.append(per)
        z+=1    
    return turnos                        
            
        

def mantenerTurnos(turnos) :
    i=0
    while i<turnos.__len__():
        for x in range(turnos.__len__()-1):
            if turnos[x].jugo==True:
                if turnos[x].vel<turnos[x+1].vel or (turnos[x].vel<=turnos[x+1].vel and turnos[x].vid<=turnos[x+1].vid):
                    per=turnos[x]
                    turnos[x]=turnos[x+1]
                    turnos[x+1]=per
        i +=1        
                      
def juegaya(tablero,turnos,toca):
    for i in range(tablero.__len__()):
        for x in tablero[i].posiciones:
            if x.pers==turnos[toca]:
                return i



#funcion que dibuja el fondo
def dibFondo():
    screen.blit(fondo,(0,0))
    pygame.draw.rect(screen,negro,(0,AnchoPantalla-Partemano/2,LargoPantalla,150))

#datos generales 
   
boton=BotonMov(1203,AnchoPantalla-Partemano/2)
run = True
clik=False
seguir=True
espacio=0
posmouse=[]
toca=0
tamañoCartas=150
turnos =agregarturnos(turnos,tablero,tamañoTablero)
pos1A.pers.defe.append(objeto.carta('defensa',objeto.cartaDef(3,False,0),"def","sing"))
juega:objeto.jugador
jugada=objeto.carta("null",objeto.cartaOfen(0,0,0),"of","sing")
while run:
    #permite continuar si todos los jugadores ceden a seguir

    seguir=True
    for i in tablero:
        if i.cede!=True:
            seguir=False


    if seguir==True and jugada.nombre!="null":
        if jugada.nomTipo=="of":
            for j in tablero:
                for p in j.posiciones:
                    if  p.lado==lineaObj:
                        if jugada.areaTipo=="sing" and p.pos==posObj:
                            p.pers.recibir(jugada)
                    elif jugada.areaTipo=="alr" and (p.pos==posObj-1 or p.pos==posObj+1):
                        p.pers.recibir(jugada)                    
                    elif jugada.areaTipo=="area" and (posObj-1<=p.pos<=posObj+1 ):
                        p.pers.recibir(jugada)
                    elif jugada.areaTipo=="todo":
                        p.pers.recibir(jugada)
        elif jugada.nomTipo=="def":
            for j in tablero:
                for p in j.posiciones:
                    if p.lado==lineaObj:
                        if (jugada.areaTipo=="sing" or jugada.areaTipo=="alr") and p.pos==posObj:
                            p.pers.recibir(jugada)
                        elif jugada.areaTipo=="area":
                            p.pers.recibir(jugada)
        jugada.nombre="null"                                





        
    
    clock.tick(fps)
    #dibuja todo
    if turnos[turnos.__len__()-1].jugo==True:
        mantenerTurnos(turnos)
    else:
        agregarturnos(turnos,tablero,tamañoTablero) 
    dibFondo()
    boton.dibujar()
    for i in tablero:
        for j in i.posiciones:
            j.dibujar(screen)

    #esto elije quien es el primero en reacionar y el que le siga        
    if seguir==True:
        juega=tablero[juegaya(tablero,turnos,toca)]
    else:
        for i in range(tablero.__len__()):
            if juega==tablero[i] and juega.cede==True:
                juega=tablero[i-1]
        

    espacio=0
    if seguir==True:
        for i in turnos[toca].mazo:
            i.dibujar(espacio,AnchoPantalla-Partemano/2,screen)
            espacio += tamañoCartas
    #si hubo un clik revisa si fue en una carta
        if clik==True and AnchoPantalla-Partemano/2<=posmouse[1]<=AnchoPantalla+Partemano:
            espacio=0
            mano=turnos[toca].mazo
            i=0
            while i<mano.__len__():
                if espacio<=posmouse[0]<=espacio+tamañoCartas:
                    
                    posObj,lineaObj,jugada=turnos[toca].turno(run,tablero,i,screen)
                    turnos[toca].jugo==False
                    #prepara todo para ejecutar las defensas
                    for i in tablero:
                        i.cede=False
                    if toca<=8:
                        toca +=1
                    else: 
                        toca=0  
                    break               
                else:
                    espacio +=tamañoCartas
                    i +=1
    #si faltan jugadores para ceder ejecuta
    if seguir==False:
        #en caso de que el judador no halla cedido revisa donde clikeo
        if juega.cede==False and clik==True:
            if boton.x<=posmouse[0]<=boton.x+150 and boton.y<=posmouse[1]:
                juega.cede=True
                clik=False 
            else:    
                for x in juega.posiciones:
                    if ((x.lado==1 and posmouse[1]<x.y-85) or (x.lado==2 and x.y+65<=posmouse[1]<=AnchoPantalla-Partemano)) and x.pers.defiende==True:
                        espacio=(x.x-75)-90
                        i=0
                        while i<=x.pers.defe.__len__()-1:
                            if espacio<=posmouse[0]<=espacio+75:
                                defensa=x.pers.defender(i)
                                if defensa.carta.anula==True:
                                    jugada=objeto.carta("null",objeto.cartaOfen(0,0,0),"of","sing")
                                for x in tablero:
                                    x.cede=False 
                                clik=False     
                                break       
                            else:
                                espacio+=75
                                i+=1
                
                    


               
                   
    
        

    
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