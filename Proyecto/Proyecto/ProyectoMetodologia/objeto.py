

import pygame


verde=(0,255,0)
azul=(0,0,255)
rojo=(255,0,0)
negro=(0,0,0)
blanco=(255,255,255)
font = None
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
 
    return newText

def cubrir(texto,rect):
    cubre=pygame.Surface((rect,15))
    cubre.fill((89,2,2))
    cubre.blit(texto,(0,0))
    return cubre


   


class cartaDef():
    def __init__(self,cura,anula,esquiva,daño,defen=0,poten=0,tipo="null"):
        self.cura=cura
        self.anula=anula
        self.esquiva=esquiva
        self.daño=daño
        self.defen=defen
        self.poten=poten
        self.tipo=tipo
        


    

    def dibujar(self,carta:pygame.Surface):
        espacio=52
        if self.cura>0:
            cura=text_format(f"Cura {self.cura}",font,12,negro)    
            carta.blit(cura,(2,espacio))
            espacio+=20
        if self.anula:
            anula=text_format("Anula",font,12,negro)
            carta.blit(anula,(2,espacio))
            espacio+=20
        if self.esquiva>0:
            esquiva=text_format(f"Esquiva {self.esquiva}",font,12,negro)
            carta.blit(esquiva,(2,espacio))
            espacio+=20
        if self.poten!=0:
            poten=text_format(f"Dañ {self.poten} {self.tipo}",font,12,negro)
            carta.blit(poten,(2,espacio))
            espacio+=20
        if self.defen!=0:
            defen=text_format(f"Def {self.defen} {self.tipo}",font,12,negro) 
            carta.blit(defen,(2,espacio))
            espacio+=20   
        daño=text_format(str(self.daño),font,12,negro)
        rectDaño=daño.get_rect()
        rectCarta=carta.get_rect()
        carta.blit(daño,(rectCarta[2]-rectDaño[2]-5,rectCarta[3]/2))                        

class cartaOfen():
    def __init__(self,daño,rangoMax,rangoMin,range,fuerza,sangra=False,marca=False,mover=False):
        self.daño=daño
        self.rangoMax=rangoMax
        self.rangoMin=rangoMin
        self.range=range
        self.fuerza=fuerza
        self.sangra=sangra
        self.marca=marca
        self.mover=mover
        


    def rango(self,pos):
        range=[]
        i=pos-self.rangoMax

        while i<= pos-self.rangoMin:
            range.append(i)
            i +=1
        i =pos+ self.rangoMin    
        while i<= pos+self.rangoMax:
            range.append(i)
            i +=1
        return range 

    def dibujar(self,carta:pygame.Surface):
        espacio=52
        daño=text_format(str(self.daño),font,12,negro)
        rango=text_format(f"Rango:{self.rangoMin}-{self.rangoMax}",font,12,negro)

        rectCarta=carta.get_rect()
        rectDaño=daño.get_rect()
        rectRango=rango.get_rect()

        carta.blit(daño,((rectCarta[2]-rectDaño[2]-5,rectCarta[3]/2)))
        carta.blit(rango,(2,espacio))
        espacio+=20
        if self.marca:
            marca=text_format("Aplica Marca",font,12,negro)
            carta.blit(marca,(2,espacio))
            espacio += 20
        if self.sangra:
            sangra=text_format("Aplica Sangrado",font,12,negro)
            carta.blit(sangra,(2,espacio))
            espacio += 20

        descripcion=text_format(f"{self.range} {self.fuerza}",font,13,negro)
        rectDesc=descripcion.get_rect()
        carta.blit(descripcion,(1,rectCarta[3]-rectDesc[3]-2))    

        


class carta():
    def __init__(self,nombre,tipoCarta,nomTipo,areaTipo):
        self.nombre=nombre
        self.carta=tipoCarta
        self.nomTipo=nomTipo
        self.areaTipo=areaTipo
        if self.nomTipo=="of":
            self.foto=pygame.image.load(f'imagenes/Ataque.png')
        else:
            self.foto=pygame.image.load(f'imagenes/Defensa.png')    

    def dibujar(self,x,y,screen):
        screen.blit(self.foto,(x,y))
        self.carta.dibujar(self.foto)
        nombre=text_format(self.nombre,font,12,negro)
        rectNombre=nombre.get_rect()
        foto=self.foto.get_rect()
        self.foto.blit(nombre,(foto[2]/2-rectNombre[2]/2,5))

           

class personaje():
    def __init__(self,x,nombre,vidMax,mov,vel,cartas,vid=50,diferenciar=False,mazo=[]):
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
        self.cartas=[]
        self.cartas=cartas
        self.mazo=[]
        self.mazo=mazo
        self.defe=[]
        self.esquiva=0
        self.sangrado=0
        self.marcado=False
        if nombre!="null" and diferenciar==False:
            self.mazo=self.armarMano()

        self.bonoLig=0
        self.bonoPes=0
        self.bonoRap=0
        self.bonoPre=0
        self.defLig=0
        self.defPes=0
        self.defRap=0
        self.defPre=0    



    def armarMano(self):
        i=0
        mazo=[]
        while i<3:
            mano=self.cartas.pop(0)
            mazo.append(mano)
            i += 1
        return mazo    
            
    def rellenar(self):
        mano=self.cartas.pop(0)
        return mano
        
        

    

    def turno(self,run,tablero,i,screen):
        #es la carta que se hizo clik
        
        jugada:carta=self.mazo.pop(i)
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
            if clik==True and 1203<posmouse[0] and 600<posmouse[1]:
                self.mazo.append(jugada)
                return x.pos,lineaObj,carta("null",cartaOfen(0,0,0,"melee","ligero"),"of","sing")
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
                                    self.cartas.append(jugada)
                                    self.mazo.append(self.rellenar())
                                    self.vid -= self.sangrado
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
                                    self.cartas.append(jugada)
                                    self.mazo.append(self.rellenar())
                                    self.vid-=self.sangrado
                                    return x.pos,lineaObj,jugada
                            #y este pinta todo si la carta no es propia pinta        
                            elif jugada.areaTipo!="sing":
                                x.dibujar(screen,azul)
                                if clik==True and x.y-85<=posmouse[1]<=x.y and x.x-75<=posmouse[0]<=x.x+75:
                                    self.cartas.append(jugada)
                                    self.mazo.append(self.rellenar())
                                    self.vid-=self.sangrado
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
                    
            pygame.display.update()   
        pygame.quit  


    def defender(self,i):
        defensa:carta=self.defe.pop(i)
        self.defiende=False
        self.vid+=defensa.carta.cura
        if self.vid>self.vidMax:
            self.vid=self.vidMax
        self.cartas.append(defensa)

        return defensa
        

               

    def recibir(self,jugada:carta):
        vel=text_format(str(self.vel),font,20,(102,100,0))
        mov=text_format(str(self.mov),font,20,(53,65,177))
        vid=text_format(str(self.vid),font,20,(89,2,2))
        san=text_format(str(self.sangrado),font,20,(50,50,50))
        esq=text_format(str(self.esquiva),font,20,(50,50,50)) 
        bonl=text_format(str(self.bonoLig),font,20,(50,50,50))
        bonp=text_format(str(self.bonoPes),font,20,(50,50,50))
        bonr=text_format(str(self.bonoRap),font,20,(50,50,50))
        bonP=text_format(str(self.bonoPre),font,20,(50,50,50))
        defl=text_format(str(self.defLig),font,20,(50,50,50))
        defp=text_format(str(self.defPes),font,20,(50,50,50))
        defr=text_format(str(self.defRap),font,20,(50,50,50))
        defP=text_format(str(self.defPre),font,20,(50,50,50))   
            
        rectVel=vel.get_rect()
        rectMov=mov.get_rect()
        rectVid=vid.get_rect()
        recCarta=self.carta.get_rect()
        rectSan=san.get_rect()
        rectEsq=esq.get_rect()
            
        self.carta.blit(vel,(recCarta[2]-rectVel[2]-5,2))
        self.carta.blit(mov,(5,75))
        self.carta.blit(vid,(recCarta[2]-rectVid[2]-5,75))
        self.carta.blit(san,(31-rectSan[2],102))
        self.carta.blit(esq,(112-rectEsq[2],102))
        self.carta.blit(bonp,(34,73))
        self.carta.blit(bonl,(44,73))
        self.carta.blit(bonr,(52,73))
        self.carta.blit(bonP,(63,73))
        self.carta.blit(defp,(75,73))
        self.carta.blit(defl,(90,73))
        self.carta.blit(defr,(105,73))
        self.carta.blit(defP,(119,73))

        if jugada.nomTipo=="of":
            
            
            if self.esquiva==0:
                if jugada.carta.fuerza=="ligero":
                    self.vid -= jugada.carta.daño-self.defLig
                elif jugada.carta.fuerza=="pesado":
                    self.vid -= jugada.carta.daño-self.defPes
                elif jugada.carta.fuerza=="rapido":
                    self.vid -= jugada.carta.daño-self.defRap
                elif jugada.carta.fuerza=="presiso":
                    self.vid -= jugada.carta.daño-self.defPre      
                if jugada.carta.sangra:
                    self.sangrado += 1
            if jugada.carta.marca==True:
                self.marcado=True        
        elif jugada.nomTipo=="def":
            self.defe.append(jugada)
        else:
            pass

    def aplicar(self,defe):
        bonl=text_format(str(self.bonoLig),font,20,(50,50,50))
        bonp=text_format(str(self.bonoPes),font,20,(50,50,50))
        bonr=text_format(str(self.bonoRap),font,20,(50,50,50))
        bonP=text_format(str(self.bonoPre),font,20,(50,50,50))
        defl=text_format(str(self.defLig),font,20,(50,50,50))
        defp=text_format(str(self.defPes),font,20,(50,50,50))
        defr=text_format(str(self.defRap),font,20,(50,50,50))
        defP=text_format(str(self.defPre),font,20,(50,50,50)) 

        self.carta.blit(bonp,(34,73))
        self.carta.blit(bonl,(44,73))
        self.carta.blit(bonr,(52,73))
        self.carta.blit(bonP,(63,73))
        self.carta.blit(defp,(75,73))
        self.carta.blit(defl,(90,73))
        self.carta.blit(defr,(105,73))
        self.carta.blit(defP,(119,73))
        self.vid+= defe.carta.cura
        self.esquiva+=defe.carta.esquiva 
        
        if defe.carta.tipo=="lig" or defe.carta.tipo=="melee" or defe.carta.tipo=="todo":
            self.bonoLig += defe.carta.poten
            self.defLig += defe.carta.defen
        if defe.carta.tipo=="pes" or defe.carta.tipo=="melee" or defe.carta.tipo=="todo":
            self.bonoPes += defe.carta.poten
            self.defPes += defe.carta.defen
        if defe.carta.tipo=="rap" or defe.carta.tipo=="distancia" or defe.carta.tipo=="todo":
            self.bonoRap += defe.carta.poten
            self.defRap += defe.carta.defen
        if defe.carta.tipo=="pre" or defe.carta.tipo=="distancia" or defe.carta.tipo=="todo":
            self.bonoPre += defe.carta.poten
            self.defPre += defe.carta.defen

   

    def diferenciador(self,posicion):
        if posicion.lado==1:
            x=personaje(self.x+1,self.nombre,self.vidMax,self.mov,self.vel,self.cartas,self.vid,True,self.mazo)
        else:
            x=personaje(self.x-1,self.nombre,self.vidMax,self.mov,self.vel,self.cartas,self.vid,True,self.mazo)
        return x    

   

    def dibujar(self,posicion,screen):
        
        
        x=0
        nombre=text_format(self.nombre,font,20,negro)
        vel=text_format(str(self.vel),font,20,negro)
        mov=text_format(str(self.mov),font,20,negro)
        vid=text_format(str(self.vid),font,20,negro)
        san=text_format(str(self.sangrado),font,20,negro)
        esq=text_format(str(self.esquiva),font,20,negro)
        bonl=text_format(str(self.bonoLig),font,20,negro)
        bonp=text_format(str(self.bonoPes),font,20,negro)
        bonr=text_format(str(self.bonoRap),font,20,negro)
        bonP=text_format(str(self.bonoPre),font,20,negro)
        defl=text_format(str(self.defLig),font,20,negro)
        defp=text_format(str(self.defPes),font,20,negro)
        defr=text_format(str(self.defRap),font,20,negro)
        defP=text_format(str(self.defPre),font,20,negro)
        
        rectNonbre=nombre.get_rect()
        rectVel=vel.get_rect()
        rectMov=mov.get_rect()
        rectVid=vid.get_rect()
        recCarta=self.carta.get_rect()
        rectSan=san.get_rect()
        rectEsq=esq.get_rect()
        
        screen.blit(self.carta,(posicion.x-75,posicion.y-85))
        
        
        self.carta.blit(nombre,(recCarta[2]/2 - (rectNonbre[2]/2),5))
        self.carta.blit(vel,(recCarta[2]-rectVel[2]-5,2))
        self.carta.blit(mov,(5,75))
        
        self.carta.blit(vid,(recCarta[2]-rectVid[2]-5,75))
        self.carta.blit(san,(31-rectSan[2],102))
        self.carta.blit(esq,(112-rectEsq[2],102))
        self.carta.blit(bonp,(34,73))
        self.carta.blit(bonl,(44,73))
        self.carta.blit(bonr,(52,73))
        self.carta.blit(bonP,(63,73))
        self.carta.blit(defp,(75,73))
        self.carta.blit(defl,(90,73))
        self.carta.blit(defr,(105,73))
        self.carta.blit(defP,(119,73))
        
        
        if posicion.lado==1:
            for i in self.defe:

                screen.blit(i.foto,((posicion.x-75)-90+x,(posicion.y-85)-140)) 
                x+=75
        if posicion.lado==2:
            for i in self.defe:

                screen.blit(i.foto,((posicion.x-75)-100+x,(posicion.y-85)+130)) 
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
        if color!=verde:
            pygame.draw.circle(screen,color,(self.x,self.y),5.0)  


class jugador():
    def __init__(self,nombre,posiciones):
        self.posiciones=[]
        self.posiciones=posiciones
        self.juega=False
        self.cede=True
        self.nombre=nombre



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
       







espadachinMazo=[
    carta("Corte Limpio",cartaOfen(3,0,0,"melee","ligero"),"of","sing"),
    carta("Corte en Ola",cartaOfen(4,0,0,"melee","pesado"),"of","sing"),
    carta("Aire Afilado",cartaOfen(4,3,2,"melee","pesado",False,False,True),"of","sing"),
    carta("Corte Largo",cartaOfen(2,1,0,"melee","ligero"),"of","sing"),
    carta("Evasivo",cartaDef(0,False,2,0),"def","sing"),
    carta("Avanze Cortante",cartaOfen(2,1,1,"melee","ligero",False,False,True),"of","sing"),
    carta("Reflejo",cartaDef(0,False,0,4,1,0,"distancia"),"def","singular")
]

tiradorMazo=[
    carta("Disparo Rapido",cartaOfen(3,1,0,"distancia","rapido"),"of","sing"),
    carta("Disparo de Advertencia",cartaDef(0,True,0,0),"def","sing"),
    carta("Disparo Presiso",cartaOfen(3,4,2,"distancia","presiso"),"of","sing"),
    carta("La Presa",cartaOfen(0,4,0,"distancia","rapido",False,True),"of","sing"),
    carta("Vendas de Guerra",cartaDef(2,False,0,0),"def","alr"),
    carta("Cazando",cartaOfen(1,3,1,"distancia","presiso",True,True),"of","sing")
]

bandidaMazo=[
    carta("Filo de Hacha",cartaOfen(3,1,0,"melee","ligero"),"of","sing"),
    carta("Encrusijada",cartaOfen(2,0,0,"melee","ligero"),"of","alr"),
    carta("Apunta y Fuego",cartaOfen(3,3,1,"distancia","presiso"),"of","sing"),
    carta("Apaño para Seguir",cartaDef(2,False,0,0),"def","alr"),
    carta("Duelo",cartaDef(0,True,0,2,1,0,"melee"),"def","sing"),
    carta("Disparo a Quemaropa",cartaOfen(6,0,0,"distancia","rapido"),"of","sing")
]
barbaroMazo=[
    carta("Filo Oxidado",cartaOfen(2,1,0,"melee","lijero",True),"of","sing"),
    carta("Sangria",cartaOfen(3,0,0,"melee","pesado",True),"of","sing"),
    carta("Ataque en Pinza",cartaOfen(1,0,0,"melee","ligero",True),"of","alr"),
    carta("Aguantar",cartaDef(0,False,0,0,1,-1,"todos"),"def","sing"),
    carta("Adrenalina",cartaDef(1,0,0,0,0,1,"melee"),"def","sing"),
    carta("Alcanze Pesado",cartaOfen(1,2,1,"melee","pesado",False,False,True),"of","sing")
]


p1=personaje(0,"Espadachin",10,3,4,espadachinMazo)
p2=personaje(0,"Tirador",10,2,4,tiradorMazo)
p3=personaje(0,"Bandida",12,1,3,bandidaMazo)
p4=personaje(0,"Barbaro",12,1,2,barbaroMazo)
p5=personaje(0,"Espadachin",10,3,4,espadachinMazo)
p6=personaje(0,"Tirador",10,2,4,tiradorMazo)
p7=personaje(0,"Bandida",12,1,3,bandidaMazo)
p8=personaje(0,"Barbaro",12,1,2,barbaroMazo)
pos1A=posicion(169,220,1,1,p1)
pos2A=posicion(500,220.5,2,1,p2)
pos3A=posicion(830,220.75,3,1,p3)
pos4A=posicion(1170,220,4,1,p4)
pos1B=posicion(169,360,1,2,p5)
pos2B=posicion(500,360,2,2,p6)
pos3B=posicion(830,360,3,2,p7)
pos4B=posicion(1170,360,4,2,p8)

jug1=jugador("jugador1",[pos1A,pos2A,pos3A,pos4A])
jug2=jugador("jugador2",[pos1B,pos2B,pos3B,pos4B])
tablero=[jug1,jug2]

