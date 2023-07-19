from changeColour import change_colour as changeColoursOfImage

import os
import shutil
import json
import random


def hexToTuple(hex):
    return tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))


currentDirectory = os.getcwd()
accCarModels = [{"carModelType": 20, "name": "V8"},{"carModelType": 21, "name": "NSX"},{"carModelType": 25, "name": "MERCEVO"},{"carModelType": 59, "name": "MACCAGT4"},{"carModelType": 35, "name": "MACCA"},{"carModelType": 30, "name": "M4"},{"carModelType": 33, "name": "LAMBOEVO2"},{"carModelType": 14, "name": "JAG"},{"carModelType": 56, "name": "GIN"},{"carModelType": 34, "name": "992"},{"carModelType": 23, "name": "991"},{"carModelType": 24, "name": "488EVO"},{"carModelType": 32, "name": "296"},{"carModelType": 31, "name": "EVO2"}]


class ACCLivery:
    def __init__(self):
        self.liveryID = str(random.randint(1, 100000))
        self.folderName = "DEFAULT"
        self.inGameName = "DEFAULT"
        self.carModelType = 31  # AUDI EVO 2
        self.baseColour = 341  # Black
        self.baseMaterialId = 0  # Glossy
        self.rimColour = 1
        self.rimMaterialId = 0
        self.rimTapeColour = 1
        self.rimTapeMaterialId = 0
        self.raceNumber = 000
        self.DazzleTopColour = (208, 42, 64)
        self.DazzleBottomColour = (74, 73, 135)
        self.zipPath = ''
    # Getter methods

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
    
    def setZipPath(self, zipPath):
        self.zipPath = zipPath

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

    def getZipPath(self):
        return self.zipPath
    
    # Other methods
    def createDazzle(self):
        for car in accCarModels:
            if car['carModelType'] == self.carModelType:
                dazzleTemplate = car['name'] + 'DAZZLE.png'
                sponsorTemplate = car['name'] + 'SPONSORS.png'
        dazzlePath = os.path.join(currentDirectory,'acc', dazzleTemplate)
        try:
            os.chdir(os.path.join(currentDirectory, "temp"))
            os.mkdir(self.liveryID)
            os.chdir(os.path.join(os.getcwd(), self.liveryID))
            os.mkdir('Liveries')
            os.chdir(os.path.join(os.getcwd(), 'Liveries'))
            os.mkdir(self.folderName)
        except FileExistsError:
            pass
        carPath = os.path.join(currentDirectory, 'temp',
                               self.liveryID, 'Liveries', self.folderName)
        os.chdir(currentDirectory)
        print(dazzlePath)
        first = changeColoursOfImage(
            dazzlePath, (0, 0, 0), self.DazzleTopColour)
        first.save(carPath + "/decals.png")
        final = changeColoursOfImage(
            carPath + "/decals.png", (255, 255, 255), self.DazzleBottomColour)
        final.save(carPath + "/decals.png")
        sponsorPath = os.path.join(currentDirectory,'acc',sponsorTemplate)
        carPath = os.path.join(carPath,'sponsors.png')
        shutil.copy(sponsorPath, carPath)

    def createJsonFile(self):
        examplePath = os.path.join(currentDirectory, "acc", "example.json")
        jsonDirectory = os.path.join(currentDirectory, "temp", self.liveryID)
        os.chdir(jsonDirectory)
        os.mkdir('Cars')
        jsonDirectory = os.path.join(jsonDirectory, 'Cars', self.liveryID + '.json')
        os.chdir(currentDirectory)
        shutil.copy(examplePath, jsonDirectory)
        with open(jsonDirectory, 'rb') as f:
            data = json.load(f)
        print(data["cupCategory"])
        data['carModelType'] = self.carModelType
        data['raceNumber'] = self.raceNumber
        data['skinColor1Id'] = self.baseColour
        data['skinColor2Id'] = self.baseColour
        data['skinColor3Id'] = self.baseColour
        data['skinMaterialType1'] = self.baseMaterialId
        data['skinMaterialType2'] = self.baseMaterialId
        data['skinMaterialType3'] = self.baseMaterialId
        data['rimColor1Id'] = self.rimColour
        data['rimColor2Id'] = self.rimTapeColour
        data['rimMaterialType1'] = self.rimMaterialId
        data['rimMaterialType2'] = self.rimTapeMaterialId
        data['teamName'] = self.inGameName
        data['customSkinName'] = self.folderName
        with open(jsonDirectory,'w') as out:
                json.dump(data,out)
        out.close()     
        f.close()
        
        def ZipCar(self):
            self.setZipPath(os.path.join(currentDirectory,'temp',self.liveryID))
            print(self.zipPath)

if __name__ == "__main__":
    car1 = ACCLivery()
    car1.setDazzleTopColour(hexToTuple('1E1E1E'))
    car1.setDazzleBottomColour(hexToTuple('EDFF21'))
    car1.setBaseColour(300)
    car1.setBaseMaterialId(2)
    car1.createDazzle()
    car1.createJsonFile()
    car1.ZipCar()
