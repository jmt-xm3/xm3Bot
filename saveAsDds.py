from wand import image
import os

def saveAsDds(victimPath,victimDestination):
    with image.Image(filename=victimPath+'.png') as img:
        img.compression = 'dxt5'
        img.save(filename=victimDestination+'.dds')

