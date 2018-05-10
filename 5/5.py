# 5 - http://www.pythonchallenge.com/pc/def/peak.html
# use pickle library to solve riddle 
# http://www.pythonchallenge.com/pc/def/peak.html
import pickle
from urllib.request import urlopen

raw = urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(raw)
# To be honest, looked this part up -- it's a serialization of ascii art
# print(data) 

# Each tuple is a character and the number of times it repeats 
for line in data:
    print("".join([k * v for k, v in line]))
# This spells out channel
print('channel')
