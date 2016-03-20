#!/usr/bin/python
from utils import *
import sys, time, math
class Laufer:
    wartosc=3
    def __init__(self, kolor, pozycjaX, pozycjaY):
        self.kolor = kolor
        self.pozycjaX=pozycjaX
        self.pozycjaY=pozycjaY
        self.inicjal='l'
        if kolor:
            self.inicjal='L'
    def sprawdz(self,endX,endY,szachownica):
        return 1
