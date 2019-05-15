import re
from Karte import Karte

class OutputWriter:
    mFilename = ""
    mTemplate = ""
    mKarte = Karte([], "")
    mIterationen = 0

    def __init__(self, iFilename, iTemplate, iKarte, iIterationen):
        self.mFilename = iFilename
        self.mTemplate = iTemplate
        self.mKarte = iKarte
        self.mIterationen = iIterationen

    def write(self):
        # Read contents from file as a single string
        file_handle = open(self.mTemplate, 'r')
        file_string = file_handle.read()
        file_handle.close()

        # Use RE package to allow for replacement (also allowing for (multiline) REGEX)
        file_string = (re.sub("<xmin>", str(self.mKarte.xmin) , file_string))
        file_string = (re.sub("<xmax>", str(self.mKarte.xmax) , file_string))
        file_string = (re.sub("<ymin>", str(self.mKarte.ymin) , file_string))
        file_string = (re.sub("<ymax>", str(self.mKarte.ymax) , file_string))
        
        file_string = (re.sub("<Name des Kennwertes>", self.mKarte.kennzahlBz[:-1], file_string))
        file_string = (re.sub("<nr>", str(self.mIterationen) , file_string))
        s = ""
        i = 0
        for land in self.mKarte.laenderliste:
            s = s + str(land) + " " + str(i) + "\n"
            i = i + 1 
        s = s[:-1]
        file_string = (re.sub("<Liste aus <xpos> <ypos> <radius> <autokennzeichen> <id> >", s , file_string))
        # Write contents to file.
        # Using mode 'w' truncates the file.
        file_handle = open(self.mFilename + ".gpl", 'w')
        file_handle.write(file_string)
        file_handle.close()