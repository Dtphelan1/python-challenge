# 2 - http://www.pythonchallenge.com/pc/def/ocr.html
# Find uncommon characters in text-chunk hidden in src code, visit that url
import string
import os
dirname = os.path.dirname(__file__)
filePath = os.path.join(dirname, '2.txt')
longString = ''.join([line.rstrip() for line in open(filePath)])

# My intiial implementation
# dictionary for keeping counts
# countDict = {}

# for x in longString:
#     if x in countDict: 
#         countDict[x] += 1
#     else: 
#         countDict[x] = 1

# # determine what an average count is
# avgCount = 0
# for x in countDict: 
#     avgCount += countDict[x]

# avgCount /= len(countDict)
# print(avgCount)

# # build the new url string
# newUrl = ""
# for x in countDict: 
#     if countDict[x] < avgCount: 
#         if x in string.ascii_lowercase:
#             newUrl += x
#     else: 
#         print('above avg')

# OPTIMIZED IMPLEMENTATION FROM http://wiki.pythonchallenge.com/index.php?title=Level2:Main_Page
countDict = {}
for character in longString: countDict[character] = countDict.get(character, 0) + 1
avgCount = len(longString) // len(countDict)
newUrl = ''.join([character for character in countDict if countDict[character] < avgCount])
print(newUrl)