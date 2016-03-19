#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, time, math
#szachownica - lista dwuwymiarowa, pierwsza wartosc x, druga y, zakres 0-7, wartosci: 0 gdy pusta, bierka
szachownica=[[0 for x in range(8)] for x in range(8)]
figury=[0 for x in range(16)]
#sciezka do pliku wymiany ruchow
plikWymiany='ruchy.txt'
#lista alfabet sluzy do wyswietlania planszy oraz ustalenia wartosci x ruchu
alfabet=[" ","A","B","C","D","E","F","G","H"]
#nasz kolor, domyslnie bialy
kolor=0
#flaga SzachMat
szachMat=0
#Klasy bierek(figur):
class Pion:
    #wartosc danej bierki
    wartosc=1
    def __init__(self, numer, kolor, pozycjaX, pozycjaY):
        #id bierki np: piony od 1 do 8
        self.numer = numer
        #kolor bierki 0 -> biały, 1 -> czarny
        self.kolor = kolor
        self.pozycjaX=pozycjaX
        self.pozycjaY=pozycjaY
        #inicjal czyli to co sie wyswietla na szachownicy
        self.inicjal='p'
        if kolor:
            self.inicjal='P'
    #sprawdzanie poprawnosci ruchu odczytanego z pliku i nadanie nowych współrzędnych
    def sprawdz(self,endX,endY):
        #sprawdzenie ruchu na prawo i lewo
        if self.pozycjaX!=endX:
            if math.fabs(self.pozycjaX-endX)>1:
                return 0
            else:
                if szachownica[endX][endY]==0:
                    return 0
        else:
            if szachownica[self.pozycjaX][endY]!=0:
                return 0
        #sprawdzenie ruchu w przód
        if self.kolor:
            if self.pozycjaY<endY:
                return 0
            if self.pozycjaY==6:
                if self.pozycjaY-endY>2:
                    return 0
            else:
                if self.pozycjaY-endY>1:
                    return 0 
        else:
            if self.pozycjaY>endY:
                return 0
            if self.pozycjaY==1:
                if endY-self.pozycjaY>2:
                    return 0
            else:
                if endY-self.pozycjaY>1:
                    return 0
        #nadanie nowych wartosci pozycji bierki
        self.pozycjaX=endX
        self.pozycjaY=endY
        return 1
    #sprawdzanie poprawnosci ruchu dla SI
    def sprawdzSI(self,endX,endY):
        if sprawdzSzachownice(endX,endY)==0:
           return 0
        #sprawdzenie ruchu w zależności od ukladu bierek
        if self.pozycjaX!=endX:
            if szachownica[endX][endY]==0 or szachownica[endX][endY].kolor==self.kolor:
                return 0
        else:
            if szachownica[self.pozycjaX][endY]!=0:
                return 0  
        #sprawdzenie ruchu w przód
        if self.kolor:
            if self.pozycjaY==6:
                if self.pozycjaY-endY>2:
                    return 0
            else:
                if self.pozycjaY-endY>1:
                    return 0
        else:
            if self.pozycjaY==1:
                if endY-self.pozycjaY>2:
                    return 0
            else:
                if endY-self.pozycjaY>1:
                    return 0
        return 1
    #typy ruchow
    ruchy=['przod2','przod','bicielewo','bicieprawo']
    def przod(self):
        if self.kolor:
            return [self.pozycjaX,self.pozycjaY-1]
        return [self.pozycjaX,self.pozycjaY+1]
    def przod2(self):
        if self.kolor:
            return [self.pozycjaX,self.pozycjaY-2]
        return [self.pozycjaX,self.pozycjaY+2]
    def bicielewo(self):
        if self.kolor:
            return [self.pozycjaX+1,self.pozycjaY-1]
        return [self.pozycjaX-1,self.pozycjaY+1]
    def bicieprawo(self):
        if self.kolor:
            return [self.pozycjaX-1,self.pozycjaY-1]
        return [self.pozycjaX+1,self.pozycjaY+1]
class Wieza:
    wartosc=5
    def __init__(self, kolor, pozycjaX, pozycjaY):
        self.kolor = kolor
        self.pozycjaX=pozycjaX
        self.pozycjaY=pozycjaY
        self.inicjal='w'
        if kolor:
            self.inicjal='W'
    def sprawdz(self,endX,endY):
        self.pozycjaX=endX
        self.pozycjaY=endY
        return 1
class Kon:
    wartosc=3
    def __init__(self, kolor, pozycjaX, pozycjaY):
        self.kolor = kolor
        self.pozycjaX=pozycjaX
        self.pozycjaY=pozycjaY
        self.inicjal='s'
        if kolor:
            self.inicjal='S'
    def sprawdz(self,endX,endY):
        self.pozycjaX=endX
        self.pozycjaY=endY
        return 1
class Laufer:
    wartosc=3
    def __init__(self, kolor, pozycjaX, pozycjaY):
        self.kolor = kolor
        self.pozycjaX=pozycjaX
        self.pozycjaY=pozycjaY
        self.inicjal='l'
        if kolor:
            self.inicjal='L'
    def sprawdz(self,endX,endY):
        self.pozycjaX=endX
        self.pozycjaY=endY
        return 1
class Krol:
    wartosc=0
    def __init__(self, kolor, pozycjaX, pozycjaY):
        self.kolor = kolor
        self.pozycjaX=pozycjaX
        self.pozycjaY=pozycjaY
        self.inicjal='k'
        if kolor:
            self.inicjal='K'
    def sprawdz(self,endX,endY):
        self.pozycjaX=endX
        self.pozycjaY=endY
        return 1
#tworzenie bierek i uzupelnienie szachownicy na start
def init():
    for i in range(4):
        figury[i]=Pion(i+1,0,4+i,1)
        szachownica[4+i][1]=figury[i]
    figury[4]=Wieza(0,7,0)
    szachownica[7][0]=figury[4]
    figury[5]=Kon(0,6,0)
    szachownica[6][0]=figury[5]
    figury[6]=Laufer(0,5,0)
    szachownica[5][0]=figury[6]
    figury[7]=Krol(0,4,0)
    szachownica[4][0]=figury[7]
    for i in range(4):
        figury[i+8]=Pion(i+5,1,4+i,6)
        szachownica[4+i][6]=figury[i+8]
    figury[12]=Wieza(1,7,7)
    szachownica[7][7]=figury[12]
    figury[13]=Kon(1,6,7)
    szachownica[6][7]=figury[13]
    figury[14]=Laufer(1,5,7)
    szachownica[5][7]=figury[14]
    figury[15]=Krol(1,4,7)
    szachownica[4][7]=figury[15]
def drukujSzachownice():
    for i in range(9):
        print(alfabet[i], end=" ")
    print('')
    for i in range(8):
        print(8-i, end=" ")
        for j in range(8):
            if szachownica[j][7-i]:
                print(szachownica[j][7-i].inicjal, end=" ")
            else:
                print(szachownica[j][7-i], end=" ")
        print(8-i)
    for i in range(9):
        print(alfabet[i], end=" ")
def losuj(start=0,stop=7):
    from random import randint
    return randint(start,stop)
def sprawdzSzachownice(endX,endY):
    if endX<0 or endX>7:
        return 0
    if endY<0 or endY>7:
        return 0
    return 1
def wczytajRuch():
    ruchy = open(plikWymiany, 'r+')
    #pobranie ostatniej lini z pliku    
    i=0
    for line in ruchy:
       pass
    ostatniRuch = line
    ruchy.close()
    return ostatniRuch
#funkcja sluzaca tylko do testowania poprawnosci ruchow, odczytujaca wartosc z konsoli i zapisujaca ja do pliku ruch
def pobierzRuch():
    ruchNowy=input('podaj ruch np:c1c6\n')
    with open(plikWymiany, "a") as ruchy:
        ruchy.write(ruchNowy)
        ruchy.write('\n')
    ruchy.close()
#funkcja ruchu
def ruch(ostatniRuch):
    #mapowanie liter na wartosci int
    i=0
    for let in alfabet:
        if ostatniRuch[0].upper()==let:
           startX=i-1
        if ostatniRuch[2].upper()==let:
           endX=i-1
        i+=1
    #dostosowanie wartosci do pol listy szachy (a1a2 -> 0001)
    startY=int(ostatniRuch[1])-1
    endY=int(ostatniRuch[3])-1
    #Z kazdym bledem funkcja ma zwracac 0
    #sprawdzenie czy podane wartosci nie wykraczaja poza szachownice
    if sprawdzSzachownice(startX,startY)==0:
        return 0
    if sprawdzSzachownice(endX,endY)==0:
        return 0
    #sprawdzanie czy istnieje bierka która ma się poruszyć
    if szachownica[startX][startY]==0:
        return 0
    #sprawdzanie czy ruch jest dozwolony
    if szachownica[startX][startY].sprawdz(endX,endY)==0:
        return 0
    #ruch
    szachownica[endX][endY]=szachownica[startX][startY]
    szachownica[startX][startY]=0
    return 1
#jakis poczatek SI-----------------------------------------------------------------------------------------------------------------------------------------
def wybierzBierke(nBierka):
    if kolor:
        bierka=figury[1+nBierka]
    else:
        bierka=figury[8+nBierka]
    return bierka
def wybierzRuch(bierka):
    #ma zwrocic 1 w przypadku dokonania poprawnego ruchu lub 0 jezeli nie da sie wykonac zadnego ruchu
    startX=bierka.pozycjaX
    startY=bierka.pozycjaY
    n=0
    while True:
        fRuch = getattr(bierka, bierka.ruchy[n])    
        endX=fRuch()[0]
        endY=fRuch()[1]
        n+=1
        if bierka.sprawdzSI(endX,endY):
            break
        if n>=len(bierka.ruchy):
            return 0
    ruchNowy=''
    ruchNowy+=alfabet[startX+1]
    ruchNowy+=str(startY+1)
    ruchNowy+=alfabet[endX+1]
    ruchNowy+=str(endY+1)
    print(ruchNowy)
    with open(plikWymiany, "a") as ruchy:
        ruchy.write(ruchNowy+'\n')
        ruchy.write('')
    ruchy.close()
    return 1
    
def ustalRuch():
    #pauza=input('pauza\n')
    #wybranie losowej bierki(na razie pionka)
    while True:
        if wybierzRuch(wybierzBierke(losuj(0,3))):
            break 
#testowa funkcja rozgrywki
def graj():
    drukujSzachownice()
    #ustalenie jaki mamy kolor i dokonanie pierwszego ruchu
    ruchy = open(plikWymiany, 'r+')
    i=0
    for line in ruchy:
        i=1
    ruchy.close()
    if 1==0:
        print(ruch(ustalRuch()))
        drukujSzachownice()
    else:
        kolor=1
    #rozgrywka
    while szachMat!=1:
        print('\n Ruch przeciwnika')
        pobierzRuch()
        print(ruch(wczytajRuch()))
        drukujSzachownice()
        print('\n Ruch si')
        ustalRuch()
        print(ruch(wczytajRuch()))
        drukujSzachownice()
#dzialanie programu:
init()
#czyszczenie plikWymiany
ruchy=open(plikWymiany, "w")
ruchy.close
graj()
