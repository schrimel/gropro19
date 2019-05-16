# -*- coding: utf-8 -*-
from InputReader import InputReader
from OutputWrite import OutputWriter
from Berechnung import StandardBerechnung
import math
import numpy as np
import argparse

ap = argparse.ArgumentParser("Hello there!")
ap.add_argument("-i", action="store", dest="input")
ap.add_argument("-o", action="store", dest="output")
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
    #check arguments and initialize variables of main
    try:
        main.iterationen = arguments.iterationen
        if main.iterationen <= 0:
            raise ArithmeticError("Error. Also, 0 oder weniger Iterationen sind wirklich nicht moeglich. Zeitreisen wurde noch nicht implementiert.")
        if arguments.input == None: 
            main.printUsage()
            return 0
        if arguments.skalierungsfaktor < 0:
            raise ArithmeticError("Error. Der Faktor muss groesser 0 sein.")
        if arguments.output == None:
            filtered = filter(None, arguments.input.split("."))
            main.mFilename = filtered[0]
        else:
            main.mFilename = arguments.output
    except ArithmeticError as err:
        print(err.message)
        return 1
    main.mInput = InputReader(arguments.input)
    
    #read input
    main.karte = main.mInput.read()
    if(main.karte == None): #input file has semantic issues
        return 1
    karte = main.karte
    main.mBerechnung = StandardBerechnung()
    for i in range(main.iterationen):
        if (i == 0):
            main.mBerechnung.voriteration(karte, arguments.skalierungsfaktor)
        karte = main.mBerechnung.berechne(karte)
    karte.berechneMinimum(karte)
    karte.scale()
    if(main.mFilename == "<default>"):
        main.mFilename = arguments.input.split(".")[0]
    main.mOutput = OutputWriter(main.mFilename, "templates/template.txt",main.karte,main.iterationen)
    main.mOutput.write()
    return 0




if __name__ == "__main__":
    main(results)
