# 6 - http://www.pythonchallenge.com/pc/def/channel.html
# Get zip file from http://www.pythonchallenge.com/pc/def/channel.zip
# Hints: 
# 1. http://www.pythonchallenge.com/pc/def/channel.html - title: now there are pairs
# 2. http://www.pythonchallenge.com/pc/def/pants.html - amazing. zoom in
# 3. http://www.pythonchallenge.com/pc/def/zipper.html - [:3] \n\n todo: tell everyone that [:n] is to take the first n characters...
# 4. http://www.pythonchallenge.com/pc/def/zip.html - yes. find the zip.
# Readme.txt: hint1: start from 90052 \n hint2: answer is inside the zip
import zipfile, re, string

z = zipfile.ZipFile("channel.zip")

contentOfReadme = z.read('readme.txt')
# Console shows starting file is 90052.

fileExt = '.txt'
pattern = r'nothing is (\d+)'
curFile = "90052"
keepReading = True; 
concatComments = ''
while keepReading: 
    contentOfCurFile = z.read(curFile + fileExt).decode('utf-8')
    concatComments += z.getinfo(curFile + fileExt).comment.decode('utf-8')
    print(contentOfCurFile)
    try:
        curFile = re.search(pattern, contentOfCurFile).group(1)
    except:
        keepReading = False

print(concatComments)
# console shows hockey
# http://www.pythonchallenge.com/pc/def/hockey.html
# says to look more closely at the letters used in spelling hockey
# Letters spell oxygen
print('oxygen')