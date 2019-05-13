# -*- coding: utf-8 -*-
import math
class Land:
    xPos = 0.0
    yPos = 0.0
    kennzeichen = ""
    kennzahl = 0
    kraftX = 0.0
    kraftY = 0.0
    radius = 0.0
    nachbarlaender = []

    def __init__(self, x, y, kennZe, kennZa):
        self.xPos = x
        self.yPos = y
        self.kennzeichen = kennZe
        self.kennzahl = kennZa 
        self.radius = math.sqrt(float(self.kennzahl) / (math.pi))

    def __str__(self):
        return str(self.xPos) + " " + str(self.yPos) + " " + str(self.radius) + " " + self.kennzeichen

    def __repr__(self):
        return str(self.xPos) + " " + str(self.yPos) + " " + str(self.radius) + " " + self.kennzeichen

    def addNachbar(self, nachbar):
        self.nachbarlaender.append(nachbar)
    
    def containsNachbar(self, nachbar):
        return nachbar in self.nachbarlaender