# -*- coding: utf-8 -*-
from InputReader import InputReader
from OutputWrite import OutputWriter
from Berechnung import StandardBerechnung
import math
import numpy as np
import argparse

ap = argparse.ArgumentParser("Hello there!")
ap.add_argument("-i", action="store", dest="input")
ap.add_argument("-o", action="store", dest="output", default="<default>")
ap.add_argument("-n", action="store", dest="iterationen", type=int, default=100)
ap.add_argument("-s", action="store", dest="skalierungsfaktor", type=float, default=1)

results = ap.parse_args()
class Main:

    mFilename = ""
    mInput = None
    mOutput = None
    mBerechnung = None
    karte = None
    iterationen = 100

    def printUsage(self):
        print("Benutzung von 'Harry Plotter' - Grosse Prog 2019")
        print("python Main.py [-options]")
        print("Eingabedatei: -i 'Dateipfad'\nAusgabedatei: -o 'Dateipfad' (Standard ist Eingabename.gpl)")
        print("Anzahl Iterationen: -n <int>")
        print("Skalierungsfaktor Voriteration: -s <float>")
    
    
def main(arguments):
    main = Main()
    if arguments.input == None:
        main.printUsage()
        return 0
    main.mInput = InputReader(arguments.input)
    main.mFilename = arguments.output
    main.karte = main.mInput.read()
    if(main.karte == None):
        return 1
    main.iterationen = arguments.iterationen
    karte = main.karte
    main.mBerechnung = StandardBerechnung()
    for i in range(main.iterationen):
        if (i == 0):
            main.mBerechnung.voriteration(karte, arguments.skalierungsfaktor)
        karte = main.mBerechnung.berechne(karte)
    berechneMinimum(karte)
    scale(karte)
    if(main.mFilename == "<default>"):
        main.mFilename = arguments.input.split(".")[0]
    main.mOutput = OutputWriter(main.mFilename, "template.txt",main.karte,main.iterationen)
    main.mOutput.write()
    return 0

def scale(karte):
    diffX = karte.xmax - karte.xmin
    diffY = karte.ymax - karte.ymin
    if diffY > diffX:
        karte.xmin = karte.xmin - 0.5 * (diffY-diffX)
        karte.xmax = karte.xmax + 0.5 * (diffY-diffX)
    elif diffX > diffY:
        karte.ymin = karte.ymin - 0.5 * (diffX-diffY)
        karte.ymax = karte.ymax + 0.5 * (diffX-diffY)

def berechneMinimum(karte):
    laenderliste = karte.laenderliste
    xplus = []
    xminus = []
    yplus = []
    yminus = []
    for l in laenderliste:
        xplus.append(float(l.xPos) + float(l.radius))
        xminus.append(float(l.xPos) - float(l.radius))
        yplus.append(float(l.yPos) + float(l.radius))
        yminus.append(float(l.yPos) - float(l.radius))
    karte.xmax = np.max(np.array(xplus))
    karte.xmin = np.min(np.array(xminus))
    karte.ymax = np.max(np.array(yplus))
    karte.ymin = np.min(np.array(yminus))
    


if __name__ == "__main__":
    main(results)