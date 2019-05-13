# -*- coding: utf-8 -*-
from InputReader import InputReader
from OutputWrite import OutputWriter
from Berechnung import Berechnung
import math
import numpy as np
class Main:

    mFilename = ""
    mInput = InputReader("input.txt")
    #mOutput = OutputReader()
    #ber = Berechnung()
    karte = None
    iterationen = 100

    def printUsage(self):
        #useful
        return 0
    
    
def main(arguments):
    main = Main()
    main.karte = main.mInput.read()
    karte = main.karte
    b = Berechnung()
    iterationen = 10000
    for i in range(iterationen):
        karte = b.berechne(karte)
    berechneMinimum(karte)
    scale(karte)
    output = OutputWriter("input", "template.txt",main.karte,iterationen)
    output.write()
    return 0

def scale(karte):
    diffX = karte.xmax - karte.xmin
    diffY = karte.ymax - karte.ymin
    max = diffX
    if diffY > diffX:
        max = diffY
    karte.xmax = karte.xmax + max
    karte.ymax = karte.ymax + max

def berechneMinimum(karte):
    laenderliste = karte.laenderliste
    xplus = []
    xminus = []
    yplus = []
    yminus = []
    for l in laenderliste:
        xplus.append(l.xPos + l.radius)
        xminus.append(l.xPos - l.radius)
        yplus.append(l.yPos + l.radius)
        yminus.append(l.yPos - l.radius)
    karte.xmax = np.max(np.array(xplus))
    karte.xmin = np.min(np.array(xminus))
    karte.ymax = np.max(np.array(yplus))
    karte.ymin = np.min(np.array(yminus))
    


if __name__ == "__main__":
    main([])
