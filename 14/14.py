# http://www.pythonchallenge.com/pc/return/italy.html
# 1 - "Walk around"
# 2 - "Remember 100*100 = (100 + 99 + 99 + 98) + (..."

from PIL import Image
import os
dirname = os.path.dirname(__file__)
filePath = os.path.join(dirname, 'wire.png')

# Actually a 10,000,1 image
wire = Image.open(filePath)
# Transform into a 100x100 pic; use a spiral ala 'cinna-bun'
spiralPic = Image.new('RGB', (100,100))
 
xCoord, yCoord, pixels = -1,0,0
delta = [(1,0),(0,1),(-1,0),(0,-1)]
doubleEachSide = 200 
while doubleEachSide/2>0:
    for transform in delta:
        steps = doubleEachSide // 2
        for s in range(steps):
            xCoord, yCoord = xCoord + transform[0], yCoord + transform[1]
            spiralPic.putpixel((xCoord, yCoord),wire.getpixel((pixels,0)))
            pixels += 1
        doubleEachSide -= 1

spiralPic.save('newPic.jpg')
# pic of a cat 
# named uzi 
# http://www.pythonchallenge.com/pc/return/cat.html

