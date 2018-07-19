# 18 - http://www.pythonchallenge.com/pc/return/balloons.html
# Hint: <!-- it is more obvious that what you might think -->
# There's a difference between both files 
# NOTHING - try: http://www.pythonchallenge.com/pc/return/difference.html
# Try: http://www.pythonchallenge.com/pc/return/brightness.html
# Hint: <!-- maybe consider deltas.gz -->
# Download at: http://www.pythonchallenge.com/pc/return/deltas.gz

import os
import gzip, bz2, difflib

dirname = os.path.dirname(__file__)
filePath = os.path.join(dirname, 'deltas.gz')

f = gzip.open(filePath, 'rb')
print(dir(f))
# print(f.read().decode())
arr1, arr2 = [], []
for line in f: 
    print(line)
    # arr1.append(line[])
    # Let's separate those two different columns of data 
    ind = line.index(b'  ')
    # print(ind)
    arr1.append(line[:ind].decode()+"\n")
    arr1.append(line[ind + 2 + 1:].decode())