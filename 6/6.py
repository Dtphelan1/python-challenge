import zipfile, re, string
from urllib.request import urlopen

z = zipfile.ZipFile("channel.zip")

contentOfReadme = z.read('readme.txt')
fileExt = '.txt'
# Console shows starting file is 90052.
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