import numpy as np
import math
from numpy import linalg as LA
from Land import Land


class Berechnung:

    def luftlinie(self, landA, landB):
        arrA = [landA.xPos, landA.yPos]
        vektorA = np.array(arrA, dtype=float)
        vektorB = np.array([landB.xPos, landB.yPos], dtype=float)
        distanceAB = np.subtract(vektorA, vektorB)
        return distanceAB

    def normVektor(self, landA, landB):
        vektorA = np.array([landA.xPos, landA.yPos], dtype=float)
        vektorB = np.array([landB.xPos, landB.yPos], dtype=float)
        return np.subtract(vektorA, vektorB) / LA.norm(np.subtract(vektorA, vektorB))

    def distance(self, landA, landB):
        arrA = [landA.xPos, landA.yPos]
        vektorA = np.array(arrA, dtype=float)
        vektorB = np.array([landB.xPos, landB.yPos], dtype=float)
        distanceLength = LA.norm(np.subtract(vektorA, vektorB))
        radii = landA.radius + landB.radius
        return distanceLength - radii

    def berechne(self, karte):
        besucht = []
        liste = karte.laenderliste
        for i in range(0,len(liste)):
            heimatland = liste[i]
            for j in range(0, len(liste)):
                ausland = liste[j]
                if ausland == heimatland:
                    continue
                if self.distance(heimatland, ausland) < 0 and not heimatland in besucht:
                    luftlinieAB = self.luftlinie(heimatland, ausland)
                    luftlinieBA = self.luftlinie(ausland, heimatland)
                    g = 0.2
                    #forceHeimatland = -1 * 0.5 * self.distance(heimatland, ausland) * luftlinieAB / LA.norm(luftlinieAB)
                    forceHeimatland =  -1 * g * self.normVektor(heimatland, ausland) * self.distance(heimatland, ausland)
                    #print(forceHeimatland)
                    heimatland.kraftX += forceHeimatland[0]
                    heimatland.kraftY += forceHeimatland[1]
                    #forceAusland = -1 * 0.5 * self.distance(ausland, heimatland) * luftlinieBA / LA.norm(luftlinieBA)
                    #forceAusland = -1 * 0.5 * luftlinieBA * (LA.norm(luftlinieBA) - heimatland.radius - ausland.radius) / LA.norm(luftlinieBA)
                    #print(forceAusland)
                    #ausland.kraftX += forceAusland[0]
                    #ausland.kraftY += forceAusland[1]
                    besucht.append(heimatland)
                elif self.distance(heimatland, ausland) > 0 and ausland in heimatland.nachbarlaender:
                    g = 0.2
                    luftlinieAB = self.luftlinie(heimatland, ausland)
                    luftlinieBA = self.luftlinie(ausland, heimatland)
                    forceHeimatland = -1 * g * self.normVektor(heimatland, ausland) * self.distance(heimatland, ausland)
                    #print(forceHeimatland)
                    heimatland.kraftX += forceHeimatland[0]
                    heimatland.kraftY += forceHeimatland[1]
                    #forceAusland = 0.5*luftlinieBA * (LA.norm(luftlinieBA)-heimatland.radius - ausland.radius) / LA.norm(luftlinieBA)
                    #ausland.kraftX += forceAusland[0]
                    #ausland.kraftY += forceAusland[1]
                    besucht.append(heimatland)
        for land in liste:
            land.xPos = float(land.xPos) + float(land.kraftX)
            land.yPos = float(land.yPos) + float(land.kraftY)
            land.kraftX = 0.0
            land.kraftY = 0.0
        return karte



    
