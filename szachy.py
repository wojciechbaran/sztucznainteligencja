#!/usr/bin/python
# -*- coding: utf-8 -*-
fff
import sys, time, math
from pion import *
from wierza import *
from kon import *
from krol import *
from laufer import *
from hetman import *
from utils import *
#szachownica - lista dwuwymiarowa, pierwsza wartosc x, druga y, zakres 0-7, wartosci: 0 gdy pusta, bierka
szachownica=[[0 for x in range(8)] for x in range(8)]
#listy przechowywujace bierki
bierkiBiale=[0 for x in range(8)]
bierkiCzarne=[0 for x in range(8)]
#sciezka do pliku wymiany ruchow
plikWymiany='ruchy.txt'
#lista alfabet sluzy do wyswietlania planszy oraz ustalenia wartosci x ruchu
alfabet=[" ","A","B","C","D","E","F","G","H"]
UNICODE_PIECES = {
  'W': u'♜', 'S': u'♞', 'L': u'♝', 'Q': u'♛',
  'K': u'♚', 'P': u'♟', 'w': u'♖', 's': u'♘',
  'l': u'♗', 'q': u'♕', 'k': u'♔', 'p': u'♙',
  None: ' '
}
#nasz kolor, domyslnie bialy
kolor=0
#flaga SzachMat
szachMat=0

#tworzenie bierek i uzupelnienie szachownicy na start
def init():
    for i in range(4):
        bierkiBiale[i]=Pion(i+1,0,4+i,1)
        szachownica[4+i][1]=bierkiBiale[i]
    bierkiBiale[4]=Wieza(0,7,0)
    szachownica[7][0]=bierkiBiale[4]
    bierkiBiale[5]=Kon(0,6,0)
    szachownica[6][0]=bierkiBiale[5]
    bierkiBiale[6]=Laufer(0,5,0)
    szachownica[5][0]=bierkiBiale[6]
    bierkiBiale[7]=Krol(0,4,0)
    szachownica[4][0]=bierkiBiale[7]
    for i in range(4):
        bierkiCzarne[i]=Pion(i+5,1,4+i,6)
        szachownica[4+i][6]=bierkiCzarne[i]
    bierkiCzarne[4]=Wieza(1,7,7)
    szachownica[7][7]=bierkiCzarne[4]
    bierkiCzarne[5]=Kon(1,6,7)
    szachownica[6][7]=bierkiCzarne[5]
    bierkiCzarne[6]=Laufer(1,5,7)
    szachownica[5][7]=bierkiCzarne[6]
    bierkiCzarne[7]=Krol(1,4,7)
    szachownica[4][7]=bierkiCzarne[7]
def drukujSzachownice():
    for i in range(9):
        print(alfabet[i], end=" ")
    print('')
    for i in range(8):
        print(8-i, end=" ")
        for j in range(8):
            if szachownica[j][7-i]:
                print(UNICODE_PIECES[szachownica[j][7-i].inicjal], end=" ")
            else:
                print(' ', end=" ")
        print(8-i)
    for i in range(9):
        print(alfabet[i], end=" ")
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
    if szachownica[startX][startY].sprawdz(endX,endY,szachownica)==0:
        return 0
    #czy następuje bicie
    if szachownica[endX][endY]!=0:
        if szachownica[endX][endY].kolor:
            bierkiCzarne.remove(szachownica[endX][endY])
        else:
            bierkiBiale.remove(szachownica[endX][endY])
    #ruch
    aktualizujPozycje(szachownica[startX][startY],endX,endY)        
    szachownica[endX][endY]=szachownica[startX][startY]
    szachownica[startX][startY]=0
    return 1
#jakis poczatek SI-----------------------------------------------------------------------------------------------------------------------------------------
def wybierzBierke(nBierka):
    while True:
        if kolor:
            bierka=bierkiBiale[nBierka]
        else:
            bierka=bierkiCzarne[nBierka]
        #dla testów czy pion
        if type(bierka)==Pion:
            break
        else:
            nBierka=losuj(0,3)
    return bierka
def wybierzRuch(bierka):
    #ma zwrocic 1 w przypadku dokonania poprawnego ruchu lub 0 jezeli nie da sie wykonac zadnego ruchu
    startX=bierka.pozycjaX
    startY=bierka.pozycjaY
    n=0
    nMax=2
    while True:
        if bierka.ruchy[n]=='przod':
            nr=losuj(1,2)
            endX=bierka.przod(nr)[0]
            endY=bierka.przod(nr)[1]
            if nMax>0:
                nMax-=1
                n-=1
        else:
            fRuch = getattr(bierka, bierka.ruchy[n])    
            endX=fRuch()[0]
            endY=fRuch()[1]
        n+=1
        if bierka.sprawdz(endX,endY,szachownica):
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
