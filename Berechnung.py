import numpy as np
import math
from numpy import linalg as LA
from Land import Land

class Berechnung:
    def distance(self, landA, landB):
        arrA = [landA.xPos, landA.yPos]
        vektorA = np.array(arrA, dtype=float)
        vektorB = np.array([landB.xPos, landB.yPos], dtype=float)
        distanceLength = LA.norm(np.subtract(vektorA, vektorB))
        radii = landA.radius + landB.radius
        return distanceLength - radii
    
    def berechne(self, karte):
        pass

    def normVektor(self, landA, landB):
        vektorA = np.array([landA.xPos, landA.yPos], dtype=float)
        vektorB = np.array([landB.xPos, landB.yPos], dtype=float)
        return np.subtract(vektorA, vektorB) / LA.norm(np.subtract(vektorA, vektorB))


class StandardBerechnung(Berechnung):
    def voriteration(self, karte, faktor):
        for l in karte.laenderliste:
            l.xPos = float(l.xPos) * faktor
            l.yPos = float(l.yPos) * faktor

    def berechne(self, karte):
        besucht = []
        g = 0.5
        liste = karte.laenderliste
        for i in range(0,len(liste)):
            heimatland = liste[i]
            for j in range(0, len(liste)):
                ausland = liste[j]
                if ausland == heimatland:
                    continue
                if self.distance(heimatland, ausland) < 0 and not heimatland in besucht:
                    forceHeimatland =  -1 * g * self.normVektor(heimatland, ausland) * self.distance(heimatland, ausland)
                    heimatland.kraftX += forceHeimatland[0]
                    heimatland.kraftY += forceHeimatland[1]
                    besucht.append(heimatland)
                elif self.distance(heimatland, ausland) > 0 and ausland in heimatland.nachbarlaender:
                    forceHeimatland = -1 * g * self.normVektor(heimatland, ausland) * self.distance(heimatland, ausland)
                    heimatland.kraftX += forceHeimatland[0]
                    heimatland.kraftY += forceHeimatland[1]
                    besucht.append(heimatland)
        for land in liste:
            land.xPos = float(land.xPos) + float(land.kraftX)
            land.yPos = float(land.yPos) + float(land.kraftY)
            land.kraftX = 0.0
            land.kraftY = 0.0
        return karte



    