#!/usr/bin/python
from utils import *
import sys, time, math
class Hetman:
    wartosc=9
    def __init__(self, kolor, pozycjaX, pozycjaY):
        self.kolor = kolor
        self.pozycjaX=pozycjaX
        self.pozycjaY=pozycjaY
        self.inicjal='h'
        if kolor:
            self.inicjal='H'
    def sprawdz(self,endX,endY,szachownica):
        return 1
