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
    #sprawdzanie poprawnosci ruchu
    def sprawdz(self,endX,endY):
        #sprawdzenie ruchu na prawo i lewo
        if self.pozycjaX!=endX:
            if math.fabs(self.pozycjaX-endX)>1:
                return 0
            else:
                if szachownica[endX][endY]==0:
                    return 0
        #sprawdzenie ruchu w przód
        if szachownica[self.pozycjaX][endY]!=0:
            return 0
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
def wczytajRuch():
    ruchy = open('ruchy.txt', 'r+')
    #pobranie ostatniej lini z pliku
    i=0
    for line in ruchy:
       i+=1
    ruchy.seek(i*4-4)
    ostatniRuch=ruchy.readline()
    ruchy.close()
    return ostatniRuch
#funkcja sluzaca tylko do testowania poprawnosci ruchow, odczytujaca wartosc z konsoli i zapisujaca ja do pliku ruch
def pobierzRuch():
    ruchy = open('ruchy.txt', 'w+')
    ruchNowy=input('\n podaj ruch np:c1c6\n')
    ruchy.write(ruchNowy+'\n')
    ruchy.truncate()
    ruchy.close()
#funkcja ruchu
def ruch(ostatniRuch):
    #mapowanie biter na wartosci int
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
    if startX<0 or startX>7:
        return 0
    if startY<0 or startY>7:
        return 0
    if endX<0 or endX>7:
        return 0
    if endY<0 or endY>7:
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
#dzialanie programu:
init()
drukujSzachownice()
#testowanie do 4 ruchow
for i in range(4):
    pobierzRuch()
    print(ruch(wczytajRuch()))
    drukujSzachownice()
