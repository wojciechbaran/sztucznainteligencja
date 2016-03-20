#!/usr/bin/python
from utils import *
import sys, time, math
class Wieza:
    wartosc=5
    def __init__(self, kolor, pozycjaX, pozycjaY):
        self.kolor = kolor
        self.pozycjaX=pozycjaX
        self.pozycjaY=pozycjaY
        self.inicjal='w'
        if kolor:
            self.inicjal='W'
    def sprawdz(self,endX,endY,szachownica):
        return 1
