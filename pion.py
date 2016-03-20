#!/usr/bin/python
from utils import *
import sys, time, math
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
    def sprawdz(self,endX,endY,szachownica):
        if sprawdzSzachownice(endX,endY)==0:
           return 0
        #sprawdzenie ruchu na prawo i lewo
        if self.pozycjaX!=endX:
            if math.fabs(self.pozycjaX-endX)>1:
                return 0
            else:
                if szachownica[endX][endY]==0 or szachownica[endX][endY].kolor==self.kolor:
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
        return 1
    #typy ruchow
    ruchy=['przod','bicielewo','bicieprawo']
    def przod(self,n):
        if self.kolor:
            return [self.pozycjaX,self.pozycjaY-n]
        return [self.pozycjaX,self.pozycjaY+n]
    def bicielewo(self):
        if self.kolor:
            return [self.pozycjaX+1,self.pozycjaY-1]
        return [self.pozycjaX-1,self.pozycjaY+1]
    def bicieprawo(self):
        if self.kolor:
            return [self.pozycjaX-1,self.pozycjaY-1]
        return [self.pozycjaX+1,self.pozycjaY+1]
