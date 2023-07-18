from changeColour import change_colour

import os

currentDirectory = os.getcwd()
print(currentDirectory)

accCarModels = [{"carModelType": 31 , "dazzleTemplate":"EVO2DAZZLE.png"}]

class ACCLivery:
    def __init__(self):
        self.folderName = "DEFAULT REV"
        self.inGameName = "DEFAULT REV"
        self.carModelType = 31  # AUDI EVO 2
        self.baseColour = 341  # Black
        self.baseMaterialId = 0  # Glossy
        self.rimColour = 1
        self.rimMaterialId = 0
        self.rimTapeColour = 1
        self.rimTapeMaterialId = 0
        self.raceNumber = 000
        self.DazzleTopColour = (208, 42, 64)
        self.DazzleBottomColour = (74, 73, 135) # im not letting people fuck with the decals layer json cba same with decals (yet?)
 # Getter methods
    def getFolderName(self):
        return self.folderName
    
    def getInGameName(self):
        return self.inGameName
    
    def getCarModelType(self):
        return self.carModelType

    def getBaseColour(self):
        return self.baseColour

    def getBaseMaterialId(self):
        return self.baseMaterialId

    def getRimColour(self):
        return self.rimColour

    def getRimMaterialId(self):
        return self.rimMaterialId

    def getRimTapeColour(self):
        return self.rimTapeColour

    def getRimTapeMaterialId(self):
        return self.rimTapeMaterialId

    def getRaceNumber(self):
        return self.raceNumber

    def getDazzleTopColour(self):
        return self.dazzleTopColour

    def getDazzleBottomColour(self):
        return self.dazzleBottomColour

    # Setter methods
    def setCarModelType(self, value):
        self.carModelType = value

    def setBaseColour(self, value):
        self.baseColour = value
    
    def setFolderName(self, value):
        self.folderName = value

    def setInGameName(self, value):
        self.inGameName = value

    def setBaseMaterialId(self, value):
        self.baseMaterialId = value

    def setRimColour(self, value):
        self.rimColour = value

    def setRimMaterialId(self, value):
        self.rimMaterialId = value

    def setRimTapeColour(self, value):
        self.rimTapeColour = value

    def setRimTapeMaterialId(self, value):
        self.rimTapeMaterialId = value

    def setRaceNumber(self, value):
        self.raceNumber = value

    # Other methods
    def createDazzle(self):
        for car in accCarModels:
            if car['carModelType'] == self.carModelType:
                dazzleTemplate = car['dazzleTemplate']
        dazzlePath = currentDirectory + "/acc/"+ dazzleTemplate
        carPath = "/home/jonan0/Documents/GitHub/xm3Bot/"+"Liveries/"+self.folderName
        try:
            os.mkdir(carPath)
        except FileExistsError:
            pass
        first = change_colour(dazzlePath, (0,0,0), self.DazzleTopColour)
        first.save(carPath+"/temp.png")
        final = change_colour(carPath+"/first.png", (255,255,255), self.Dazzle)
        final.save(carPath+"/decals.png")

car1 = ACCLivery()
car1.createDazzle()       


