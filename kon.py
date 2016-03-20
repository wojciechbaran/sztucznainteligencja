#!/usr/bin/python
from utils import *
import sys, time, math
class Kon:
    wartosc=3
    def __init__(self, kolor, pozycjaX, pozycjaY):
        self.kolor = kolor
        self.pozycjaX=pozycjaX
        self.pozycjaY=pozycjaY
        self.inicjal='s'
        if kolor:
            self.inicjal='S'
    def sprawdz(self,endX,endY,szachownica):
        return 1
