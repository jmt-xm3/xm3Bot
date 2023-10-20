import os
from PIL import Image, ImageDraw, ImageFont
assetDir = os.path.join(os.getcwd(), 'acc')
fontPath = os.path.join(assetDir,'BebasNeue-Regular.ttf')
fnt = ImageFont.truetype(fontPath, 40)
with Image.open(os.path.join(assetDir,'square.png')) as im:
    draw = ImageDraw.Draw(im)
    draw.text((128, 128), "Hello", font=fnt, fill=(0, 0, 0, 255))
    im.save(os.path.join(assetDir, "000F.png"))
