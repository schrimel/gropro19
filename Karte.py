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