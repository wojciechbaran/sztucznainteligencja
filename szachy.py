#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, time
szachownica=[[0 for x in range(8)] for x in range(8)]
figury=[0 for x in range(16)]
plikWymiany='ruchy.txt'
alfabet=[" ","A","B","C","D","E","F","G","H"]
class Pion:
    wartosc=1
    def __init__(self, numer, kolor, pozycjaX, pozycjaY):
        self.numer = numer
        self.kolor = kolor
        self.pozycjaX=pozycjaX
        self.pozycjaY=pozycjaY
        self.inicjal='p'
        if kolor:
            self.inicjal='P'
class Wieza:
    wartosc=5
    def __init__(self, kolor, pozycjaX, pozycjaY):
        self.kolor = kolor
        self.pozycjaX=pozycjaX
        self.pozycjaY=pozycjaY
        self.inicjal='w'
        if kolor:
            self.inicjal='W'
class Kon:
    wartosc=3
    def __init__(self, kolor, pozycjaX, pozycjaY):
        self.kolor = kolor
        self.pozycjaX=pozycjaX
        self.pozycjaY=pozycjaY
        self.inicjal='s'
        if kolor:
            self.inicjal='S'
class Laufer:
    wartosc=3
    def __init__(self, kolor, pozycjaX, pozycjaY):
        self.kolor = kolor
        self.pozycjaX=pozycjaX
        self.pozycjaY=pozycjaY
        self.inicjal='l'
        if kolor:
            self.inicjal='L'
class Krol:
    wartosc=0
    def __init__(self, kolor, pozycjaX, pozycjaY):
        self.kolor = kolor
        self.pozycjaX=pozycjaX
        self.pozycjaY=pozycjaY
        self.inicjal='k'
        if kolor:
            self.inicjal='K'
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
    i=0
    for line in ruchy:
       i+=1
    ruchy.seek(i*4-4)
    return ruchy.readline()
    ruchy.close()
def pobierzRuch():
    ruchy = open('ruchy.txt', 'w+')
    ruchNowy=input('\n podaj ruch np:c1c6\n')
    ruchy.write(ruchNowy+'\n')
    ruchy.truncate()
    ruchy.close()
def ruch(ostatniRuch):
    i=0
    for let in alfabet:
        if ostatniRuch[0].upper()==let:
           startX=i-1
        if ostatniRuch[2].upper()==let:
           endX=i-1
        i+=1
        startY=int(ostatniRuch[1])-1
        endY=int(ostatniRuch[3])-1
    szachownica[endX][endY]=szachownica[startX][startY]
    szachownica[startX][startY]=0
    
init()
drukujSzachownice()
for i in range(4):
    pobierzRuch()
    ruch(wczytajRuch())
    drukujSzachownice()
