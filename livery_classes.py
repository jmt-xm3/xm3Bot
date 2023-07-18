from changeColour import change_colour

import os

def hexToTuple(hex):
  return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

currentDirectory = os.getcwd()
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
        self.DazzleBottomColour = (74, 73, 135) # im not letting people fuck with the decals layer json cba same with sponsors (yet?)
 # Getter methods
    def setFolderName(self, folderName):
        self._folderName = folderName

    def setInGameName(self, inGameName):
        self._inGameName = inGameName

    def setCarModelType(self, carModelType):
        self._carModelType = carModelType

    def setBaseColour(self, baseColour):
        self._baseColour = baseColour

    def setBaseMaterialId(self, baseMaterialId):
        self._baseMaterialId = baseMaterialId

    def setRimColour(self, rimColour):
        self._rimColour = rimColour

    def setRimMaterialId(self, rimMaterialId):
        self._rimMaterialId = rimMaterialId

    def setRimTapeColour(self, rimTapeColour):
        self._rimTapeColour = rimTapeColour

    def setRimTapeMaterialId(self, rimTapeMaterialId):
        self._rimTapeMaterialId = rimTapeMaterialId

    def setRaceNumber(self, raceNumber):
        self.raceNumber = raceNumber

    def setDazzleTopColour(self, DazzleTopColour):
        self.DazzleTopColour = DazzleTopColour

    def setDazzleBottomColour(self, DazzleBottomColour):
        self.DazzleBottomColour = DazzleBottomColour

     # Setter methods
    def setFolderName(self, folderName):
        self.folderName = folderName

    def setInGameName(self, inGameName):
        self.inGameName = inGameName

    def setCarModelType(self, carModelType):
        self.carModelType = carModelType

    def setBaseColour(self, baseColour):
        self.baseColour = baseColour

    def setBaseMaterialId(self, baseMaterialId):
        self.baseMaterialId = baseMaterialId

    def setRimColour(self, rimColour):
        self.rimColour = rimColour

    def setRimMaterialId(self, rimMaterialId):
        self.rimMaterialId = rimMaterialId

    def setRimTapeColour(self, rimTapeColour):
        self.rimTapeColour = rimTapeColour

    def setRimTapeMaterialId(self, rimTapeMaterialId):
        self.rimTapeMaterialId = rimTapeMaterialId

    def setRaceNumber(self, raceNumber):
        self.raceNumber = raceNumber

    def setDazzleTopColour(self, DazzleTopColour):
        self.DazzleTopColour = DazzleTopColour

    def setDazzleBottomColour(self, DazzleBottomColour):
        self.DazzleBottomColour = DazzleBottomColour

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
        return self.DazzleTopColour

    def getDazzleBottomColour(self):
        return self.DazzleBottomColour

    # Other methods
    def createDazzle(self):
        for car in accCarModels:
            if car['carModelType'] == self.carModelType:
                dazzleTemplate = car['dazzleTemplate']
        dazzlePath = currentDirectory + "/acc/"
        dazzlePath = os.path.join(dazzlePath, dazzleTemplate)
        carPath = os.path.join(currentDirectory, self.folderName)
        try:
            os.mkdir(self.folderName)
        except FileExistsError:
            pass
        first = change_colour(dazzlePath, (0,0,0), self.DazzleTopColour)
        first.save(carPath+"/temp.png")
        final = change_colour(carPath+"/temp.png", (255,255,255), self.DazzleBottomColour)
        final.save(carPath+"/decals.png")

car1 = ACCLivery()
car1.setDazzleTopColour((0,0,0))
car1.createDazzle()       


