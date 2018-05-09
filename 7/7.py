from PIL import Image
import re 

img = Image.open('oxygen.png')

print(img.width)
print(img.height)
print(img.getpixel((0, 0)))
# print()
row = [img.getpixel((xPos, img.height // 2)) for xPos in range(0, img.width)]
row = row[::7]
lookupSet = {}

print(''.join([chr(colorTuple[0]) for colorTuple in row]))

# drop noisey non-greys
ords = [r for r, g, b, a in row if r == g == b]
extractedString = ''.join(map(chr, ords))
print(extractedString)
# produces
# smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
numbers = re.findall(r'(\d{2,3})', extractedString)
print(numbers)
print(''.join(map(lambda x: chr(int(x)), numbers)))
# produces 'integrity'