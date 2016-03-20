#!/usr/bin/python
from utils import *
import sys, time, math
class Krol:
    wartosc=0
    def __init__(self, kolor, pozycjaX, pozycjaY):
        self.kolor = kolor
        self.pozycjaX=pozycjaX
        self.pozycjaY=pozycjaY
        self.inicjal='k'
        if kolor:
            self.inicjal='K'
    def sprawdz(self,endX,endY,szachownica):
        return 1
