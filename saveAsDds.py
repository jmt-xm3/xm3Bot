from wand import image

def saveAsDds(victimPath,victimDestination):
    with image.Image(filename=victimPath+'.png') as img:
        img.compression = 'dxt5'
        img.save(filename=victimDestination+'.dds')

