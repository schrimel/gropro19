# -*- coding: utf-8 -*-
from Land import Land
from Karte import Karte
import sys
import os
import re
class InputReader:
    mFilename = "" #: dateiname fuer eingabedatei

    def __init__(self, filename):
        """
        Konstruktor erhaelt den Dateinamen der Eingabedatei und speichert ihn ab
        """
        self.mFilename = filename
    
    def read(self):
        """
        liest die Eingabedatei ein und gibt ein Objekt von Karte mit allen eingelesenen Informationen zurueck
        """
        try:
            wFile = open(self.mFilename, "r")
            lines = wFile.readlines()
            kennzahlBz = ""
            laender = []
            laendermap = {}
            nachbarmap = {}
            zaehler = 0
            for l in lines:
                if zaehler == 0: #erste zeile
                    kennzahlBz = l
                    zaehler = zaehler + 1
                if "#" in l: #kommentar
                    zaehler = zaehler + 1
                    continue
                if zaehler == 2: #lese land ein
                    splitted = l.strip().split(" ") #zeile in einzelne bestandteile splitten

                    #input validieren
                    if splitted[0] in laendermap.keys():
                        raise RuntimeError("Error. Datei '" + self.mFilename + "' enthaelt das gleiche Land doppelt. Das ist nicht erlaubt!\n")
                    if not re.match("[A-Z]{1,3}",splitted[0]):
                        raise RuntimeError("Error. Laenderkennzeichen haben 1-3 Grossbuchstaben. Andere Zeichen sind nicht erlaubt.\n")
                    if int(splitted[1]) < 1:
                        raise RuntimeError("Error. So schoen Anti-Materie auch ist, leider sind keine negativen Kennzahlen erlaubt. Ausserdem muessen Kennzahlen mindestens den Wert 1 haben.")
                    if float(splitted[3]) < -180 or float(splitted[3]) > 180:
                        raise RuntimeError("Error. Der Wert " + splitted[2] + " ist wohl offenkundig ausserhalb des erlaubten Intervalls [-180;180] fuer WGS84 Laengengrade")
                    if float(splitted[3]) < -90 or float(splitted[3]) > 90:
                        raise RuntimeError("Error. Der Wert " + splitted[3] + " ist wohl offenkundig ausserhalb des erlaubten Intervalls [-90;90] fuer WGS84 Breitengrade")
                    for l in laender:
                        if l.xPos == splitted[2] and l.yPos == splitted[3]:
                            raise RuntimeError("Error. Die Datei enthaelt Laender mit der gleichen Position. Vatikanstadt oder was?!\n")
                    #neues Land-Objekt erzeugen und in liste speichern
                    neuland = Land(float(splitted[2])+181, float(splitted[3])+181, splitted[0], splitted[1])
                    laender.append(neuland)
                    laendermap[splitted[0]] = neuland
                    nachbarmap[neuland] = []
                if zaehler == 3 :   #nachbarschaftsbeziehungen einlesen
                    nachbarschaft = l.strip().split(":") #auftrennen in Ausgangsland, Nachbarlaender
                    #fehler wenn genannter Nachbar nicht deklariert
                    if(nachbarschaft[0] not in laendermap.keys()):
                        raise RuntimeError("Error. Scheint so, als wäre das Land " + nachbarschaft[0] + " nicht in der oberen Liste angegeben.")
                    heimatland = laendermap[nachbarschaft[0]]
                    nachbarNames = nachbarschaft[1].strip().split(" ")
                    #bidirektionale zuordnung durchfuehren
                    for landname in nachbarNames:
                        if(landname not in laendermap.keys()):
                            raise RuntimeError("Error. Scheint so, als wäre das Land " + nachbarschaft[0] + " nicht in der oberen Liste angegeben.")
                        if(laendermap[landname] not in nachbarmap[heimatland]):
                            nachbarmap[heimatland].append(laendermap[landname])
                        if(heimatland not in nachbarmap[laendermap[landname]]):
                            nachbarmap[laendermap[landname]].append(heimatland)
                for x in laender:
                    addNachbarnToLand(self, nachbarmap[x], x)
            
            if not zusammenhaengend(laender):
                raise RuntimeError("Error. Nicht alle Laender haengen zusammen.")
        except IOError:
            sys.stderr.write("Error. Die Datei '" + self.mFilename +"' existiert nicht!\n")
            return None
        except RuntimeError as err:
            sys.stderr.write(err)
            return None
        karte = Karte(laender, kennzahlBz)  #aus den eingelesenen laendern wird eine karte erzeugt
        return karte

def zusammenhaengend(laenderliste):
    """
    prueft ob alle Laender in der Liste zusammenhaengen;
    gibt true zurueck wenn alle zusammenhaengen, sonst false
    """
    startland = laenderliste[0]
    besucht = []
    besucht.append(startland)
    zusammenhaengendRek(startland, besucht)
    return len(besucht) == len(laenderliste)

def zusammenhaengendRek(startland, besucht):
    """
    Rekursionsfunktion zum pruefen ob alle laender zusammenhaengen
    void
    """
    for n in startland.nachbarlaender:
        if not n in besucht:
            besucht.append(n)
            zusammenhaengendRek(n, besucht)

def addNachbarnToLand(self, nachbarn, heimatland):
    """
    fuegt einem Land ein anderes als Nachbarn hinzu
    """
    heimatland.nachbarlaender = []
    for n in nachbarn:
        if not heimatland.containsNachbar(n):
            heimatland.addNachbar(n)
    