
from itertools import count
import pygame
import objeto
import menu

pygame.init()
clock = pygame.time.Clock()
fps=60
verde=(0,255,0)
azul=(0,0,255)
rojo=(255,0,0)
negro=(0,0,0)

LargoPantalla= 1353
AnchoPantalla=600
Partemano=100
screen = pygame.display.set_mode((LargoPantalla,AnchoPantalla+Partemano),0,32)
fondo = pygame.image.load('imagenes/tableroPrueba.png').convert_alpha()
botonmov= pygame.image.load('imagenes/Cancelar.png')


pygame.display.set_caption('Battle')


class BotonMov():
    def __init__(self,x,y):
        self.x=x
        self.y=y


    def dibujar(self):
        screen.blit(botonmov,(self.x,self.y))

    def mover(per ,pos)  :
        pass

tamañoTablero=8





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
                        per=j.pers  
        for i in tablero:
            
            for j in i.posiciones:
                if j.pers==per:
                    j.pers.jugo=True
                    j.pers.defiende=True                               
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

def bono(jugada,per):
    if jugada.carta.fuerza=="ligero":
        jugada.carta.daño += per.bonoLig
    elif jugada.carta.fuerza=="pesado":
        jugada.carta.daño += per.bonoPes
    elif jugada.carta.fuerza=="rapido":
        jugada.carta.daño+= per.bonoRap
    elif jugada.carta.fuerza=="presiso":
        jugada.carta.daño += per.bonoPre
    return jugada

def mover(pers,tablero,obj,linea):
    menor=False
    for i in tablero:
        for x in i.posiciones:
            if x.lado!=linea:
                mod=i
                if x.pers==pers and x.pos<obj:
                    menor=True
    if menor==True:
        j=0
        while j<=3:
            if mod.posiciones[j].pers==pers and mod.posiciones[j].pos!=obj:
                mod.posiciones[j].pers=mod.posiciones[j+1].pers
                mod.posiciones[j+1].pers=pers
            j+=1
    else:
        j=3
        while j>=0:
            if mod.posiciones[j].pers==pers and mod.posiciones[j].pos!=obj:
                mod.posiciones[j].pers=mod.posiciones[j-1].pers
                mod.posiciones[j-1]=pers
            j-=1
                            
        




                

#funcion que dibuja el fondo
def dibFondo():
    screen.blit(fondo,(0,0))
    pygame.draw.rect(screen,negro,(0,AnchoPantalla-Partemano/2,LargoPantalla,150))

#datos generales 
def jugar(tablero):  
    boton=BotonMov(1203,AnchoPantalla-Partemano/2)
    termina=False
    run = True
    clik=False
    seguir=True
    espacio=0
    posmouse=[]
    toca=0
    tamañoCartas=150
    turnos=[]
    turnos =agregarturnos(turnos,tablero,tamañoTablero)
    juega:objeto.jugador
    jugadas=[]
    jugada=objeto.carta("null",objeto.cartaOfen(0,0,0,"null","null"),"of","sing")
    null=objeto.carta("null",objeto.cartaOfen(0,0,0,"null","null"),"of","sing")

    while run:
        #permite continuar si todos los jugadores ceden a seguir

        seguir=True
        for i in tablero:
            if i.cede!=True:
                seguir=False


        if seguir==True and jugadas.__len__()>=1:
            t=jugadas.__len__()-1
            while t>=0:
                aplica=jugadas.pop(t)
                if t>=1:
                    bloquea=jugadas[t-1]

                if aplica[0].nomTipo=="of":
                    if aplica[0].carta.mover==True:
                        mover(aplica[1],tablero,posObj,lineaObj)
                    for j in tablero:
                        for p in j.posiciones:
                            if  p.lado==lineaObj:
                                if aplica[0].areaTipo=="sing" and p.pos==posObj:
                                    p.pers.recibir(aplica[0])
                                elif aplica[0].areaTipo=="alr" and (p.pos==posObj-1 or p.pos==posObj+1):
                                    p.pers.recibir(aplica[0])                    
                                elif aplica[0].areaTipo=="area" and (posObj-1<=p.pos<=posObj+1 ):
                                    p.pers.recibir(aplica[0])
                                elif aplica[0].areaTipo=="todo":
                                    p.pers.recibir(aplica[0])
                elif aplica[0].nomTipo=="def" and aplica[0]!=jugada:
                    for j in tablero:
                        for p in j.posiciones:
                            if bloquea[1]==p.pers:
                                p.pers.vid-=aplica[0].carta.daño
                                if aplica[0].carta.anula:
                                    bloquea[0]=null
                            if aplica[1]==p.pers:
                                p.pers.aplicar(aplica[0])
                elif aplica[0].nomTipo=="def" and aplica[0]==jugada:
                    for j in tablero:
                        for p in j.posiciones:
                            if  p.lado==lineaObj:
                                if (jugada.areaTipo=="sing" or jugada.areaTipo=="alr" )and p.pos==posObj:
                                    p.pers.recibir(jugada)
                                elif jugada.areaTipo=="todo":
                                    p.pers.recibir(jugada)


                t-=1                                





            
        
        clock.tick(fps)
        #dibuja todo

        dibFondo()
        boton.dibujar()
        for i in tablero:
            for j in i.posiciones:
                j.dibujar(screen)

        #esto elije quien es el primero en reacionar y el que le siga        
        if seguir==True:
            juega=tablero[juegaya(tablero,turnos,toca)]
        else:
            if toca!=turnos.__len__():
                mantenerTurnos(turnos)
            else:
                agregarturnos(turnos,tablero,tamañoTablero) 
                toca=0
            for i in range(tablero.__len__()):
                if juega==tablero[i] and juega.cede==True:
                    juega=tablero[i-1]
            

        espacio=0
        if seguir==True:
            screen.blit(objeto.text_format(juega.nombre,objeto.font,20,objeto.blanco),(LargoPantalla/2,AnchoPantalla-Partemano/2))
            i=0
            if turnos[toca].vid>0:
                while i<turnos[toca].mazo.__len__():
                    turnos[toca].mazo[i].dibujar(espacio,AnchoPantalla-Partemano/2,screen)
                    espacio += tamañoCartas
                    i+=1
            #si hubo un clik revisa si fue en una carta
                if clik==True and AnchoPantalla-Partemano/2<=posmouse[1]<=AnchoPantalla+Partemano:
                    espacio=0
                    mano=turnos[toca].mazo
                    i=0
                    while i<mano.__len__():
                        if espacio<=posmouse[0]<=espacio+tamañoCartas:
                            
                            posObj,lineaObj,jugada=turnos[toca].turno(run,tablero,i,screen)
                            if jugada.nombre!="null":
                                if jugada.nomTipo=="of":
                                    jugada=bono(jugada,turnos[toca])
                                turnos[toca].jugo==False
                                jugadas.append([jugada,turnos[toca]])
                                #prepara todo para ejecutar las defensas
                                for i in tablero:
                                    i.cede=False
                                if toca<=8:
                                    toca +=1
                                else: 
                                    toca=0  
                            clik=False
                            break
                                           
                        else:
                            espacio +=tamañoCartas
                            i +=1
            else:
                if toca<=8:
                    toca +=1
                else: 
                    toca=0               
        #si faltan jugadores para ceder ejecuta
        if seguir==False:
            for i in jugadas:
                i[0].dibujar(espacio,AnchoPantalla-Partemano/2,screen)
            screen.blit(objeto.text_format(juega.nombre,objeto.font,20,objeto.blanco),(LargoPantalla/2,AnchoPantalla-Partemano/2))    
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
                                    jugadas.append([defensa,x.pers])
                                    #if defensa.carta.anula==True:
                                    #   jugada=objeto.carta("null",objeto.cartaOfen(0,0,0),"of","sing")
                                    for x in tablero:
                                        x.cede=False 
                                    clik=False     
                                    break       
                                else:
                                    espacio+=75
                                    i+=1
                    
                        

        for i in tablero:
            termina=True
            for x in i.posiciones:
                if x.pers.vid>0:
                    termina=False
            if termina==True:
                for j in tablero:
                    if j.nombre!=i.nombre:
                        menu.victoria(screen,screen.get_width(),j.nombre)
                
                    
        
            

        
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

jugar(objeto.tablero)    
