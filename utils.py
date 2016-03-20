#!/usr/bin/python
def losuj(start=0,stop=7):
    from random import randint
    return randint(start,stop)
def sprawdzSzachownice(endX,endY):
    if endX<0 or endX>7:
        return 0
    if endY<0 or endY>7:
        return 0
    return 1
#nadanie nowych wartosci pozycji bierki
def aktualizujPozycje(bierka,endX,endY):
    bierka.pozycjaX=endX
    bierka.pozycjaY=endY
