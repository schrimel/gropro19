# -*- coding: utf-8 -*-
from Land import Land
from Karte import Karte
import sys
import os
class InputReader:
    mFilename = ""

    def __init__(self, filename):
        self.mFilename = filename
    
    def read(self):
        try:
            wFile = open(self.mFilename, "r")
            lines = wFile.readlines()
            kennzahlBz = ""
            laender = []
            laendermap = {}
            nachbarmap = {}
            zaehler = 0
            for l in lines:
                if zaehler == 0:
                    kennzahlBz = l
                    zaehler = zaehler + 1
                if "#" in l:
                    zaehler = zaehler + 1
                    continue
                if zaehler == 2:
                    splitted = l.strip().split(" ")
                    if splitted[0] in laendermap.keys():
                        raise RuntimeError("Error. Datei '" + self.mFilename + "' enthaelt das gleiche Land doppelt. Das ist nicht erlaubt!\n")
                    if int(splitted[1]) < 1:
                        raise RuntimeError("Error. So schoen Anti-Materie auch ist, leider sind keine negativen Kennzahlen erlaubt. Ausserdem muessen Kennzahlen mindestens den Wert 1 haben.")
                    if float(splitted[3]) < -180 or float(splitted[3]) > 180:
                        raise RuntimeError("Error. Der Wert " + splitted[2] + " ist wohl offenkundig ausserhalb des erlaubten Intervalls [-180;180] fuer WGS84 Laengengrade")
                    if float(splitted[3]) < -90 or float(splitted[3]) > 90:
                        raise RuntimeError("Error. Der Wert " + splitted[3] + " ist wohl offenkundig ausserhalb des erlaubten Intervalls [-90;90] fuer WGS84 Breitengrade")
                    for l in laender:
                        if l.xPos == splitted[2] and l.yPos == splitted[3]:
                            raise RuntimeError("Error. Die Datei enthaelt Laender mit der gleichen Position. Vatikanstadt oder was?!\n")
                    neuland = Land(float(splitted[2])+181, float(splitted[3])+181, splitted[0], splitted[1])
                    laender.append(neuland)
                    laendermap[splitted[0]] = neuland
                    nachbarmap[neuland] = []
                if zaehler == 3 :
                    nachbarschaft = l.strip().split(":")
                    if(nachbarschaft[0] not in laendermap.keys()):
                        raise RuntimeError("Error. Scheint so, als wäre das Land " + nachbarschaft[0] + " nicht in der oberen Liste angegeben.")
                    heimatland = laendermap[nachbarschaft[0]]
                    nachbarNames = nachbarschaft[1].strip().split(" ")
                    for landname in nachbarNames:
                        if(landname not in laendermap.keys()):
                            raise RuntimeError("Error. Scheint so, als wäre das Land " + nachbarschaft[0] + " nicht in der oberen Liste angegeben.")
                        nachbarmap[heimatland].append(laendermap[landname])
                        nachbarmap[laendermap[landname]].append(heimatland)
                for x in laender:
                    addNachbarnToLand(self, nachbarmap[x], x)
        except IOError:
            sys.stderr.write("Error. Die Datei '" + self.mFilename +"' existiert nicht!\n")
            return None
        except RuntimeError as err:
            sys.stderr.write(err.message)
            return None
        karte = Karte(laender, kennzahlBz)
        return karte

def addNachbarnToLand(self, nachbarn, heimatland):
    heimatland.nachbarlaender = []
    for n in nachbarn:
        if not heimatland.containsNachbar(n):
            heimatland.addNachbar(n)
    