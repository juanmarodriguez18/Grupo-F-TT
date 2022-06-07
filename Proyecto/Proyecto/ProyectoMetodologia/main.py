import pygame


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


fondo = pygame.image.load('imagenes/tableroPrueba.png').convert_alpha()
botonmov= pygame.image.load('imagenes/mover.png')

class cartaOfen():
    def __init__(self,daño,rangoMax,rangoMin):
        self.daño=daño
        self.rangoMax=rangoMax
        self.rangoMin=rangoMin
        


    def rango(self,pos):
        range=[]
        i=pos-self.rangoMax

        while i<= pos-self.rangoMin:
            range.append(i)
            i +=1
        i += self.rangoMin    
        while i<= pos+self.rangoMax:
            range.append(i)
            i +=1
        return range   

class cartaDef():
    def __init__(self,cura,anula,esquiva):
        self.cura=cura
        self.anula=anula
        self.esquiva=esquiva

      

class carta():
    def __init__(self,nombre,tipoCarta,nomTipo,areaTipo):
        self.nombre=nombre
        self.carta=tipoCarta
        self.nomTipo=nomTipo
        self.areaTipo=areaTipo
        self.foto=pygame.image.load(f'imagenes/{self.nombre}.png')

    def dibujar(self,x,y):
        screen.blit(self.foto,(x,y))    

class personaje():
    def __init__(self,x,nombre,vidMax,mov,vel,mazo,vid=50):
        self.x=x
        self.nombre=nombre
        self.vidMax=vidMax
        self.vid=vid
        if self.vid>=self.vidMax:
            self.vid=vidMax
        self.mov=mov
        self.vel=vel
        self.jugo=False
        self.defiende=False
        self.carta= pygame.image.load(f'imagenes/{self.nombre}.png')
        self.mazo=mazo
        self.defe=[]
        

    

    def turno(self,run,tablero,i):
        #es la carta que se hizo clik
        
        jugada:carta=self.mazo[i]
        lineaObj=0
        posself=0
        #revisa si la carta es ofenciva/defensiva y elije en que linea se juega
        for x in tablero:
            for j in x.posiciones:
                if j.pers==self :
                    posself=j.pos
                    if j.lado==1:
                        if jugada.nomTipo=="of":
                            lineaObj=2
                        else:
                            lineaObj=1
                    elif j.lado==2:
                        if jugada.nomTipo=="of":
                            lineaObj=1
                        else:
                            lineaObj=2 

        clik=False
        while run==True :
            #pone en rojo los lugares que llega la carta ofenciva
            if jugada.nomTipo=="of":
                for j in tablero:
                    for x in range(j.posiciones.__len__()):
                        for i in jugada.carta.rango(posself):
                            if j.posiciones[x].pos==i and j.posiciones[x].lado==lineaObj:
                                #colorea las pociones
                                j.posiciones[x].dibujar(rojo)
                                #revisa donde se hizo clik y revisa si el area sigue en la linea objetivo
                                if clik==True and j.posiciones[x].y-85<=posmouse[1]<=j.posiciones[x].y+65 and j.posiciones[x].x-75<=posmouse[0]<=j.posiciones[x].x+75:
                                    return x,lineaObj,jugada
            #pone en azul los lugares de las cartas defensivas                    
            else :
                for j in tablero:
                    for x in range(j.posiciones.__len__()):
                        if j.posiciones[x].lado==lineaObj:
                            #este pinta la carta si es solo propia
                            if jugada.areaTipo=="sing" and j.posiciones[x].pers==self:
                                j.posiciones[x].dibujar(azul)
                                if clik==True and j.posiciones[x].y-85<=posmouse[1]<=j.posiciones[x].y and j.posiciones[x].x-75<=posmouse[0]<=j.posiciones[x].x+75:
                                    return x,lineaObj,jugada
                            #y este pinta todo si la carta no es propia pinta        
                            else:
                                j.posiciones[x].dibujar(azul)
                                if clik==True and j.posiciones[x].y-85<=posmouse[1]<=j.posiciones[x].y and j.posiciones[x].x-75<=posmouse[0]<=j.posiciones[x].x+75:
                                    return x,jugada,lineaObj
                    
            

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
        pygame.quit  


    def defender(self,i):
        defensa:carta=self.defe.pop(i)
        self.defiende=False
        self.vid+=defensa.carta.cura
        

        return defensa
        

               

    def recibir(self,jugada:carta):
        

        if jugada.nomTipo=="of":
            self.vid -= jugada.carta.daño
        elif jugada.nomTipo=="def":
            self.defe.append(jugada)
        else:
            pass

   

    def diferenciador(self):
        x=personaje(self.x+1,self.nombre,self.vidMax,self.mov,self.vel,self.mazo,self.vid)
        return x    

   

    def dibujar(self,posicion):   
        screen.blit(self.carta,(posicion.x-75,posicion.y-85))
        x=0
        if posicion.lado==1:
            for i in self.defe:

                screen.blit(i.foto,((posicion.x-75)-90+x,(posicion.y-85)-140)) 
                x+=75
        if posicion.lado==2:
            for i in self.defe:

                screen.blit(i.foto,((posicion.x-75)-90+x,(posicion.y-85)+70)) 
                x+=75         


    

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


class jugador():
    def __init__(self,posiciones):
        self.posiciones=[]
        self.posiciones=posiciones
        self.juega=False
        self.cede=True


       
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
null=personaje(0,"null",0,0,0,[])
per1=personaje(0,"Espadachin",10,2,4,[carta('defensa',cartaDef(3,False,0),"def","sing"),carta('Espadachin',cartaOfen(3,1,0),"of","alr")])
per2=personaje(0,"Espadachin",10,2,3,[carta('Espadachin',cartaOfen(3,1,0),"of","area")])
#per2=personaje(0, "Desesperada",6,1,3)
#per3=personaje(0,"Enfermo",10,1,3)
#per4=personaje(0"Bandida",12,2,2)
#per5=personaje(0,"Tirador",10,1,4)
#per6=personaje(0"Bardo",8,3,5)
per7=personaje(0,"null",16,1,1,[])
#per8=personaje(0,"Maniatica",8,3,4)
#per9=personaje(0,"Bestia",14,2,2)
#per10=personaje(0,"Barbaro",12,1,2)
#per11=personaje(0,"Cazadora",6,3,4)
#per12=personaje(0,"Desertor",8,2,3)
pos1A=posicion(169,220,1,1,per1)
pos2A=posicion(500,220.5,2,1,per2)
pos3A=posicion(830,220.75,3,1,null)
pos4A=posicion(1170,220,4,1,null)
pos1B=posicion(169,380,1,2,per7)
pos2B=posicion(500,380,2,2,null)
pos3B=posicion(830,380,3,2,null)
pos4B=posicion(1170,380,4,2,null)

jug1=jugador([pos1A,pos2A,pos3A,pos4A])
jug2=jugador([pos1B,pos2B,pos3B,pos4B])
tablero=[jug1,jug2]
for x in tablero:
    for i in x.posiciones:
        i.pers=i.pers.diferenciador()


turnos=[]
# crea el orden de turnos
def agregarturnos(turnos,tablero,tamaño):
    turnos=[]
    for i in tablero:
        per=personaje(0,"null",0,0,0,[])
        for j in i.posiciones:
            if j.pers.vel>=per.vel and j.pers.jugo==False:
                if j.pers.vel>per.vel or (j.pers.vel==per.vel and j.pers.vid<=per.vid):
                    j.pers.jugo=True
                    j.pers.defiende=True
                    per=j.pers

                
                        
            turnos.append(per)
    return turnos                        
            
        

def mantenerTurnos(turnos) :
    i=0
    while i<turnos.__len__():
        for x in range(turnos.__len__()-1):
            if turnos[x].jugo==False:
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
pos1A.pers.defe.append(carta('defensa',cartaDef(3,False,0),"def","sing"))
juega:jugador
jugada=carta("null",cartaOfen(0,0,0),"of","sing")
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
            j.dibujar()

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
            i.dibujar(espacio,AnchoPantalla-Partemano/2)
            espacio += tamañoCartas
    #si hubo un clik revisa si fue en una carta
        if clik==True and AnchoPantalla-Partemano/2<=posmouse[1]<=AnchoPantalla+Partemano:
            espacio=0
            mano=turnos[toca].mazo
            i=0
            while i<mano.__len__():
                if espacio<=posmouse[0]<=espacio+tamañoCartas:
                    
                    posObj,lineaObj,jugada=turnos[toca].turno(run,tablero,i)
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
            for x in juega.posiciones:
                if ((x.lado==1 and posmouse[1]<x.y-85) or (x.lado==2 and x.y+65<=posmouse[1]<=AnchoPantalla-Partemano)) and x.pers.defiende==True:
                    espacio=(x.x-75)-90
                    i=0
                    while i<=x.pers.defe.__len__()-1:
                        if espacio<=posmouse[0]<=espacio+75:
                            defensa=x.pers.defender(i)
                            if defensa.carta.anula==True:
                                jugada=carta("null",cartaOfen(0,0,0),"of","sing")
                            for x in tablero:
                                x.cede=False 
                            break       
                        else:
                            espacio+=75
                            i+=1
                elif boton.x<=posmouse[0]<=boton.x+150 and boton.y<=posmouse[1]:
                    juega.cede=True
                    


               
                   
    
        

    
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
