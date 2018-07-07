# 12 - http://www.pythonchallenge.com/pc/return/evil.html
# shows http://www.pythonchallenge.com/pc/return/evil1.jpg -- try other numbers
# go to http://www.pythonchallenge.com/pc/return/evil2.jpg --  "not .pjg - .gfx"
# go to http://www.pythonchallenge.com/pc/return/evil2.gfx -- downloads file
# go to http://www.pythonchallenge.com/pc/return/evil3.jpg -- "no more evil"
# go to http://www.pythonchallenge.com/pc/return/evil4.jpg -- "bert is evil"
# go to http://www.pythonchallenge.com/pc/return/bert.html -- picture of bert "yes, bert is evil"

#let's mess with our file
import os

dirname = os.path.dirname(__file__)
filePath = os.path.join(dirname, 'evil2.gfx')

data = open(filePath, 'rb').read()
# print(data)
for i in range(5): 
    open('%d.jpg' % i ,'wb').write(data[i::5])

# writes out 'disproportionality' with the ity crossed out 
# try http://www.pythonchallenge.com/pc/return/disproportionality.html
# - doesn't work
# and http://www.pythonchallenge.com/pc/return/disproportional.html
# - bingo 