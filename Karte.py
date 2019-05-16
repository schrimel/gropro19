import numpy as np
class Karte:
    laenderliste = []
    kennzahlBz = ""
    xmin = 0.0
    xmax = 0.0
    ymin = 0.0
    ymax = 0.0

    def __init__(self, l, kennzBz):
        self.laenderliste = []
        for land in l:
            self.laenderliste.append(land)
        self.kennzahlBz = kennzBz

    def scale(self):
        diffX = self.xmax - self.xmin
        diffY = self.ymax - self.ymin
        if diffY > diffX:
            self.xmin = self.xmin - 0.5 * (diffY-diffX)
            self.xmax = self.xmax + 0.5 * (diffY-diffX)
        elif diffX > diffY:
            self.ymin = self.ymin - 0.5 * (diffX-diffY)
            self.ymax = self.ymax + 0.5 * (diffX-diffY)

    def berechneMinimum(self):
        laenderliste = self.laenderliste
        xplus = []
        xminus = []
        yplus = []
        yminus = []
        for l in laenderliste:
            xplus.append(float(l.xPos) + float(l.radius))
            xminus.append(float(l.xPos) - float(l.radius))
            yplus.append(float(l.yPos) + float(l.radius))
            yminus.append(float(l.yPos) - float(l.radius))
        self.xmax = np.max(np.array(xplus))
        self.xmin = np.min(np.array(xminus))
        self.ymax = np.max(np.array(yplus))
        self.ymin = np.min(np.array(yminus))
    