from changeColour import change_colour as changeColoursOfImage
from overlay import overlay_images
import os
import shutil
import json
import random


def hexToTuple(hex):
    return tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))


def random_rgb():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


currentDirectory = os.getcwd()
accCarModels = [{"carModelType": 8, "name": "BEN"}, {"carModelType": 20, "name": "V8"},
                {"carModelType": 21, "name": "NSX"}, {
                    "carModelType": 22, "name": "MACCA"},
                {"carModelType": 25, "name": "MERCEVO"}, {
                    "carModelType": 59, "name": "MACCAGT4"},
                {"carModelType": 35, "name": "MACCAEVO"}, {
                    "carModelType": 30, "name": "M4"},
                {"carModelType": 33, "name": "LAMBOEVO2"}, {
                    "carModelType": 14, "name": "JAG"},
                {"carModelType": 56, "name": "GIN"}, {
                    "carModelType": 34, "name": "992"},
                {"carModelType": 23, "name": "991"}, {
                    "carModelType": 24, "name": "488EVO"},
                {"carModelType": 32, "name": "296"}, {"carModelType": 31, "name": "EVO2"}]

iracingCars = [{"value": 201, "key": "Dallara P217", "files": "lmp2"},
               {"value": 202, "key": "Dallara IR18", "file": "ir18"},
               {"value": 203, "key": "Dallara F317", "file": "f317"},
               {"value": 204, "key": "FIA F4", "file": "fiaf4"}, {"value": 205, "key": "Mazda MX5 Cup", "file": "mx5"},
               {"value": 206, "key": "Dirt Late Model", "file": "latemodel"},
               {"value": 207, "key": "Dirt Sprint Car", "file": "sprint"},
               {"value": 208, "key": "Dirt", "file": "midget"}]


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
        self.DazzleTopColour = (255, 255, 255)
        self.DazzleBottomColour = (255, 255, 255)
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
        dazzlePath = os.path.join(currentDirectory, 'acc', dazzleTemplate)
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
        randomHex = ''.join(random.choice('0123456789ABCDEF') for _ in range(6))
        placeholderColour = hexToTuple(randomHex)
        while placeholderColour == self.DazzleTopColour or placeholderColour == self.DazzleBottomColour:
            randomHex = ''.join(random.choice('0123456789ABCDEF') for _ in range(6))
            placeholderColour = hexToTuple(randomHex)
        placeholderColour = placeholderColour
        tempChange = changeColoursOfImage(dazzlePath, (0, 0, 0), placeholderColour)
        tempChange.save(carPath + "/decals.png")
        first = changeColoursOfImage(carPath + "/decals.png", (255, 255, 255), self.DazzleBottomColour)
        first.save(carPath + "/decals.png")
        final = changeColoursOfImage(carPath + "/decals.png", placeholderColour, self.DazzleTopColour)
        final.save(carPath + "/decals.png")
        sponsorPng = os.path.join(currentDirectory, 'acc',
                                  sponsorTemplate)  # copy sponsors.png and finish JSON from acc folder to livery folder
        sponsorJson = os.path.join(currentDirectory, 'acc', 'sponsors.json')
        decalsJson = os.path.join(currentDirectory, 'acc', 'decals.json')
        shutil.copy(sponsorPng, os.path.join(carPath, 'sponsors.png'))
        shutil.copy(sponsorJson, os.path.join(carPath, 'sponsors.json'))
        shutil.copy(decalsJson, os.path.join(carPath,
                                             'decals.json'))  # DDS works but acc is a shit game and won't recognize them unless you turn off texDDS in menuSettings.json
        '''toDDS(os.path.join(carPath,'decals'),os.path.join(carPath,'decals_0')
        shutil.copy(os.path.join(carPath,'decals_0.dds'),os.path.join(carPath,'decals_1.dds'))
        toDDS(os.path.join(carPath,'sponsors'),os.path.join(carPath,'sponsors_0'))
        shutil.copy(os.path.join(carPath,'sponsors_0.dds'),os.path.join(carPath,'sponsors_1.dds'))'''

    def createJsonFile(self):
        examplePath = os.path.join(currentDirectory, "acc", "example.json")
        jsonDirectory = os.path.join(currentDirectory, "temp", self.liveryID)
        os.chdir(jsonDirectory)
        os.mkdir('Cars')
        jsonDirectory = os.path.join(
            jsonDirectory, 'Cars', self.liveryID + '.json')
        os.chdir(currentDirectory)
        shutil.copy(examplePath, jsonDirectory)
        with open(jsonDirectory, 'rb') as f:
            data = json.load(f)
        if self.carModelType == 20:
            data['skinTemplateKey'] = 103
        if self.carModelType == 8:
            data['skinTemplateKey'] = 103  # fuck kunos for making me do this
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
        with open(jsonDirectory, 'w') as out:
            json.dump(data, out)
        out.close()
        f.close()

    def zipCar(self):
        self.setZipPath(os.path.join(currentDirectory, 'temp', self.liveryID))
        tempDirectory = os.path.join(currentDirectory, 'temp')
        os.chdir(tempDirectory)
        shutil.make_archive(str(self.liveryID), 'zip', self.zipPath)
        self.setZipPath(os.path.join(currentDirectory,
                                     'temp', self.liveryID) + '.zip')
        os.chdir(currentDirectory)


class iRacingLivery:
    def __init__(self):
        self.name = str(random.randint(1, 10000))
        self.path = os.path.join(currentDirectory, "temp", (self.name + '.png'))
        self.base_colour = (255, 0, 0)
        self.dazzle1 = (0, 255, 0)
        self.dazzle2 = (0, 0, 255)
        self.car = "lmp2"

    def set_name(self, name):
        self.name = name

    def set_path(self, path):
        self.path = path

    def set_base_colour(self, base_colour):
        self.base_colour = base_colour

    def set_dazzle1(self, dazzle1):
        self.dazzle1 = dazzle1

    def set_dazzle2(self, dazzle2):
        self.dazzle2 = dazzle2

    def set_car(self, car):
        self.car = car

    def get_name(self):
        return self.name

    def get_path(self):
        return self.path

    def get_base_colour(self):
        return self.base_colour

    def get_dazzle1(self):
        return self.dazzle1

    def get_dazzle2(self):
        return self.dazzle2

    def get_car(self):
        return self.car

    def create_livery(self):
        specMap = os.path.join(currentDirectory, 'iracing', (self.car + 'spec.mip'))
        dazzlePath = os.path.join(currentDirectory, 'iracing', (self.car + 'dazzle.png'))
        sponsorPath = os.path.join(currentDirectory, 'iracing', (self.car + 'sponsors.png'))
        shutil.copy(dazzlePath, self.path)
        placeholder1 = random_rgb()
        while placeholder1 == (255, 0, 0) or placeholder1 == (0, 255, 0) or placeholder1 == (0, 0, 255):
            placeholder1 = random_rgb()
        temp = changeColoursOfImage(self.path, (0, 255, 0), placeholder1, tolerance=5)
        temp.save(self.path)
        placeholder2 = random_rgb()
        while placeholder2 == (255, 0, 0) or placeholder2 == (0, 255, 0) or placeholder2 == (0, 0, 255):
            placeholder2 = random_rgb()
        temp1 = changeColoursOfImage(self.path, (0, 0, 255), placeholder2, tolerance=5)
        temp1.save(self.path)
        red = changeColoursOfImage(self.path, (255, 0, 0), self.base_colour, tolerance=5)
        red.save(self.path)
        blue = changeColoursOfImage(self.path, placeholder2, self.dazzle1, tolerance=5)
        blue.save(self.path)
        green = changeColoursOfImage(self.path, placeholder1, self.dazzle2, tolerance=5)
        green.save(self.path)
        overlay_images(self.path, sponsorPath, self.path)
        return specMap, self.path
