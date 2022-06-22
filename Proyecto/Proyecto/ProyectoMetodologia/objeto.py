import pygame


verde=(0,255,0)
azul=(0,0,255)
rojo=(255,0,0)
negro=(0,0,0)

class cartaDef():
    def __init__(self,cura,anula,esquiva,daño,condicion="null",condRango="null"):
        self.cura=cura
        self.anula=anula
        self.esquiva=esquiva
        self.condicion=condicion
        self.condRango=condRango


    def cumpleCon(self,carta):
        if self.condicion!="null":
            if self.condicion=="recibir" and (self.condRango=="null" or carta.range==self.condRango or carta.fuerza==self.condRango):
                self.daño=carta.daño
            

class cartaOfen():
    def __init__(self,daño,rangoMax,rangoMin,range,fuerza):
        self.daño=daño
        self.rangoMax=rangoMax
        self.rangoMin=rangoMin
        self.range=range
        self.fuerza=fuerza
        


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


class carta():
    def __init__(self,nombre,tipoCarta,nomTipo,areaTipo):
        self.nombre=nombre
        self.carta=tipoCarta
        self.nomTipo=nomTipo
        self.areaTipo=areaTipo
        self.foto=pygame.image.load(f'imagenes/{self.nombre}.png')

    def dibujar(self,x,y,screen):
        screen.blit(self.foto,(x,y))   

class personaje():
    def __init__(self,x,nombre,vidMax,mov,vel,mazoPD,cartas,mazo,vid=50,mano=[]):
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
        self.cartas=cartas
        self.mazoPD=mazoPD
        self.mazo=mazo
        self.mano=mano
        self.defe=[]
        

    

    def turno(self,run,tablero,i,screen):
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
                    for x in j.posiciones:
                        for i in jugada.carta.rango(posself):
                            if x.pos==i and x.lado==lineaObj:
                                #colorea las pociones
                                x.dibujar(screen,rojo)
                                #revisa donde se hizo clik y revisa si el area sigue en la linea objetivo
                                if clik==True and x.y-85<=posmouse[1]<=x.y+65 and x.x-75<=posmouse[0]<=x.x+75:
                                    return x.pos,lineaObj,jugada
            #pone en azul los lugares de las cartas defensivas                    
            else :
                for j in tablero:
                    for x in j.posiciones:
                        if x.lado==lineaObj:
                            #este pinta la carta si es solo propia
                            if jugada.areaTipo=="sing" and x.pers==self:
                                x.dibujar(screen,azul)
                                if clik==True and x.y-85<=posmouse[1]<=x.y and x.x-75<=posmouse[0]<=x.x+75:
                                    return x.pos,lineaObj,jugada
                            #y este pinta todo si la carta no es propia pinta        
                            else:
                                x.dibujar(screen,azul)
                                if clik==True and x.y-85<=posmouse[1]<=x.y and x.x-75<=posmouse[0]<=x.x+75:
                                    return x.pos,lineaObj,jugada
                    
            

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
        if self.vid>self.vidMax:
            self.vid=self.vidMax
        

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

   

    def dibujar(self,posicion,screen):   
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

    def dibujar(self,screen,color=verde):
        pygame.draw.circle(screen,color,(self.x,self.y),5.0)
        if self.pers.nombre != "null":
            self.pers.dibujar(self,screen)


class jugador():
    def __init__(self,posiciones):
        self.posiciones=[]
        self.posiciones=posiciones
        self.juega=False
        self.cede=True



#def clasesBasicas():
    #null=personaje(0,0,0,0,0,[],[],[],0)
    #per1=personaje(0,"Espadachin",10,2,4,[carta("Corte Limpio",cartaOfen(3,1,0),"of","sing"),carta("Corte en Ola",cartaOfen(4,1,0),"of")])
    #null=obj.personaje(0,"null",0,0,0,[])
    #per1=obj.personaje(0,"Espadachin",10,2,4,[obj.carta('defensa',obj.cartaDef(3,False,0),"def","sing"),obj.carta('Espadachin',obj.cartaOfen(3,1,0),"of","alr")])
    #per2=obj.personaje(0,"Espadachin",10,2,3,[obj.carta('Espadachin',obj.cartaOfen(3,1,0),"of","area")])
    #per2=personaje(0, "Desesperada",6,1,3)
    #per3=personaje(0,"Enfermo",10,1,3)
    #per4=personaje(0"Bandida",12,2,2)
    #per5=personaje(0,"Tirador",10,1,4)
    #per6=personaje(0"Bardo",8,3,5)
    #per7=obj.personaje(0,"null",16,1,1,[])
    #per8=personaje(0,"Maniatica",8,3,4)
    #per9=personaje(0,"Bestia",14,2,2)
    #per10=personaje(0,"Barbaro",12,1,2)
    #per11=personaje(0,"Cazadora",6,3,4)
    #per12=personaje(0,"Desertor",8,2,3)
       


espadachin=personaje(0,"Espadachin",10,2,4,)




espadachinMazo=[
    carta("Corte Limpio",cartaOfen(3,0,0,"melee","ligero"),"of","sing"),
    carta("Corte en Ola",cartaOfen(4,0,0,"melee","pesado"),"of","sing"),
    carta("Aire Afilado",cartaOfen(4,3,2,"melee","pesado"),"of","sing"),
    carta("Corte Largo",cartaOfen(2,1,0,"melee","ligero"),"of","sing"),
    carta("Evasivo",cartaDef(0,False,2,0),"def","sing"),
    carta("Avanze Cortante",cartaOfen(2,1,1,"melee","ligero"),"of","sing"),
    carta("Reflejo",cartaDef(0,False,0,0,"recibir","melee"))




]