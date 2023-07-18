from changeColour import change_colour as changeColoursOfImage

import os
import shutil
import json
import random


def hexToTuple(hex):
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))


currentDirectory = os.getcwd()
accCarModels = [{"carModelType": 31, "dazzleTemplate": "EVO2DAZZLE.png"}]


class ACCLivery:
    def __init__(self):
        self.seed = str(random.randint(1, 100000))
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
        # im not letting people fuck with the decals layer json cba same with sponsors (yet?)
        self.DazzleBottomColour = (74, 73, 135)
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
        try:
            os.chdir(os.path.join(currentDirectory, "temp"))
            os.mkdir(self.seed)
            os.chdir(os.path.join(os.getcwd(), self.seed))
            os.mkdir('Liveries')
            os.chdir(os.path.join(os.getcwd(), 'Liveries'))
            os.mkdir(self.folderName)
        except FileExistsError:
            pass
        carPath = os.path.join(currentDirectory, 'temp',
                               self.seed, 'Liveries', self.folderName)
        os.chdir(currentDirectory)
        first = changeColoursOfImage(
            dazzlePath, (0, 0, 0), self.DazzleTopColour)
        first.save(carPath+"/decals.png")
        final = changeColoursOfImage(
            carPath+"/decals.png", (255, 255, 255), self.DazzleBottomColour)
        final.save(carPath+"/decals.png")

    def createJsonFile(self):
        examplePath = os.path.join(currentDirectory, "acc","example.json")
        jsonDirectory = os.path.join(currentDirectory,"temp",self.seed)
        os.chdir(jsonDirectory)
        os.mkdir('Cars')
        jsonDirectory = os.path.join(jsonDirectory,'Cars',self.seed+'.json')
        os.chdir(currentDirectory)
        shutil.copy(examplePath, jsonDirectory)
        car = json.loads(jsonDirectory)
        print(car)



car1 = ACCLivery()
car1.setDazzleTopColour(hexToTuple('1E1E1E'))
car1.setDazzleBottomColour(hexToTuple('EDFF21'))
car1.createDazzle()
car1.createJsonFile()