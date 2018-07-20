# 18 - http://www.pythonchallenge.com/pc/return/balloons.html
# Hint: <!-- it is more obvious that what you might think -->
# There's a difference between both files 
# NOTHING - try: http://www.pythonchallenge.com/pc/return/difference.html
# Try: http://www.pythonchallenge.com/pc/return/brightness.html
# Hint: <!-- maybe consider deltas.gz -->
# Download at: http://www.pythonchallenge.com/pc/return/deltas.gz

import bz2
import difflib
import gzip
import os
import re

dirname = os.path.dirname(__file__)
filePath = os.path.join(dirname, 'deltas.gz')

f = gzip.open(filePath, 'rb')
print(dir(f))
# print(f.read().decode())
arr1, arr2 = [], []
for line in f: 
    # Let's separate those two different columns of data 
    # end of first col
    indOfFirstEnd = 53
    # start of second
    indOfSecondStart = indOfFirstEnd + 3;
    arr1.append(line[:indOfFirstEnd].decode()+"\n")
    arr2.append(line[indOfSecondStart:].decode())

compare = difflib.Differ().compare(arr1, arr2)

# some files for the diffs 
same = open(os.path.join(dirname, "same.png"), "wb")
additions = open(os.path.join(dirname, "additions.png"), "wb")
deletions = open(os.path.join(dirname, "deletions.png"), "wb")

for line in compare: 
    print(line)
    # get the bytes
    bs = bytes([int(o, 16) for o in line[2:].strip().split(" ") if o])
    if line[0] == "+":
        same.write(bs)
    elif line[0] == "-":
        additions.write(bs)
    else:
        deletions.write(bs)
# word: butter
same.close()
# word: fly
additions.close()
# "../hex/bin.html"
deletions.close()
# 19 - http://www.pythonchallenge.com/pc/hex/bin.html
# U:butter
# P:fly