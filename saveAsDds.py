from wand import image
import os

def saveAsDds(victimPath,victimDestination):
    with image.Image(filename=victimPath+'.png') as img:
        img.compression = 'dxt5'
        img.save(filename=victimDestination+'.dds')

saveAsDds('/home/jonan0/Documents/GitHub/xm3Bot/temp/7051/Liveries/JMT774/decals','/home/jonan0/Documents/GitHub/xm3Bot/temp/7051/Liveries/JMT774/decals')