# http://www.pythonchallenge.com/pc/return/mozart.html 
# Clue: <title>let me get this straight</title>
# sounds like we should be shifting around the pink bars to be straight
from PIL import Image
import numpy as np
import os

dirname = os.path.dirname(__file__)
filePath = os.path.join(dirname, 'mozart.gif')

image = Image.open(filePath)
(width, height) = image.size;

# Lets get that pink pixel location
for i, val in enumerate(image.histogram()):
    print(i, ": ", val)

# Shows pixel with value 60 as the most common
print(max(enumerate(image.histogram()), key=lambda x: x[1]))
tmp = image.copy()
tmp.frombytes(bytes([60] * (width * height)))
tmp.save('moz-result.gif')
# tmp.show()
# Not a pink pixel -- 60 is out

# Lets find a pixel that shows up isome number of time divisible by the height
print([x for x in image.histogram() if x % height == 0 and x != 0]) 
# pixel is at index 2400 of histogram
color = image.histogram().index(2400)
print("color is: ", color)
tmp2 = image.copy()
tmp2.frombytes(bytes([color] * (width * height)))
tmp2.save('moz-result-2.gif')
# tmp2.show()
# VEry pink

# We want to shift each row s.t. the first pink pixel is at the front;
# move each row backwwards upto the index of the first pink pixel
print([row.tolist().index(195) for row in np.array(image)]) 
shiftedBytes = [bytes(np.roll(row, -row.tolist().index(195)).tolist()) for row in np.array(image)]
final = Image.frombytes(image.mode, image.size, b"".join(shiftedBytes))
final.save('mox-final-result.gif')
final.show()

# Keyword in pic - romance
# http://www.pythonchallenge.com/pc/return/romance.html 