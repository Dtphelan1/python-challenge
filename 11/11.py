# 11 - http://www.pythonchallenge.com/pc/return/5808.html
from PIL import Image
import os

dirname = os.path.dirname(__file__)
filePath = os.path.join(dirname, 'cave.jpg')

img = Image.open(filePath)

(w, h) = img.size
even = Image.new('RGB', (w // 2, h // 2))
odd  = Image.new('RGB', (w // 2, h // 2))

for i in range(w): 
    for j in range(h):
        p = img.getpixel((i, j))
        if ((i + j) % 2 == 1):
            odd.putpixel((i // 2, j // 2), p)
        else: 
            even.putpixel((i // 2, j // 2), p)

even.save('even.jpg')
odd.save('odd.jpg')
# even photo has the word evil in it
# visit: http://www.pythonchallenge.com/pc/return/evil.html