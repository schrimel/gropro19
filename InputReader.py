# -*- coding: utf-8 -*-
from Land import Land
from Karte import Karte
import sys

class InputReader:
    mFilename = ""

    def __init__(self, filename):
        self.mFilename = filename
    
    def read(self):
        wFile = open(self.mFilename, "r")
        lines = wFile.readlines()
        kennzahlBz = ""
        laender = []
        laendermap = {}
        nachbarmap = {}
        zaehler = 0
        for l in lines:
            if(zaehler == 0):
                kennzahlBz = l
                zaehler = zaehler + 1
            if("#" in l):
                zaehler = zaehler + 1
                continue
            if(zaehler == 2):
                splitted = l.strip().split(" ")
                neuland = Land(splitted[2], splitted[3], splitted[0], splitted[1])
                laender.append(neuland)
                laendermap[splitted[0]] = neuland
                nachbarmap[neuland] = []
            if(zaehler == 3):
                nachbarschaft = l.strip().split(":")
                heimatland = laendermap[nachbarschaft[0]]
                nachbarNames = nachbarschaft[1].strip().split(" ")
                for landname in nachbarNames:
                    nachbarmap[heimatland].append(laendermap[landname])
                    nachbarmap[laendermap[landname]].append(heimatland)
        for x in laender:
            addNachbarnToLand(self, nachbarmap[x], x)

        karte = Karte(laender, kennzahlBz)
        return karte

def addNachbarnToLand(self, nachbarn, heimatland):
    heimatland.nachbarlaender = []
    for n in nachbarn:
        if not heimatland.containsNachbar(n):
            heimatland.addNachbar(n)
    