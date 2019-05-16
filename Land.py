# -*- coding: utf-8 -*-
import math
class Land:
    xPos = 0.0 #: x-Position des Mittelpunktes
    yPos = 0.0 #: y-Position des Mittelpunktes
    kennzeichen = "" #: Laenderkennzeichen
    kennzahl = 0 #: Kennzahl
    kraftX = 0.0 #: aktuelle Kraft in x-Richtung (nur waehrend einer Iteration benoetigt)
    kraftY = 0.0  #: aktuelle Kraft in y-Richtung (nur waehrend einer Iteration benoetigt)
    radius = 0.0 #: Radius des Kreises
    nachbarlaender = [] #: Nachbarlaender

    def __init__(self, x, y, kennZe, kennZa):
        """
        Konstruktor der Klasse Land bekommt Mittelpunkt (x,y) das Laenderkennzeichen kennZe und die Kennzahl kennZa
        """
        self.xPos = x
        self.yPos = y
        self.kennzeichen = kennZe
        self.kennzahl = kennZa 
        self.radius = math.sqrt(float(self.kennzahl) / (math.pi))

    def __str__(self):
        """
        Gibt String-Repraesentation fuer Ausgabe zurueck
        """
        return str(self.xPos) + " " + str(self.yPos) + " " + str(self.radius) + " " + self.kennzeichen

    def __repr__(self):
        """
        Gibt String-Repraesentation fuer Ausgabe zurueck
        Wird zu Debugging-Zwecken benoetigt
        """
        return str(self.xPos) + " " + str(self.yPos) + " " + str(self.radius) + " " + self.kennzeichen

    def addNachbar(self, nachbar):
        """
        fuegt Nachbarn der Liste hinzu
        """
        self.nachbarlaender.append(nachbar)
    
    def containsNachbar(self, nachbar):
        """
        True wenn nachbar ein Nachbar des self-Objektes
        """
        return nachbar in self.nachbarlaender