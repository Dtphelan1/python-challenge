# 3 - http://www.pythonchallenge.com/pc/def/equality.html
# Hint: "One small letter, surrounded by EXACTLY three big bodyguards on each of its sides."
import re
import os
dirname = os.path.dirname(__file__)
filePath = os.path.join(dirname, '3.txt')

pattern = r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]'
newUrl = "".join(re.findall(pattern, open(filePath).read()))
print(newUrl)
