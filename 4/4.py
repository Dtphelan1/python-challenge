# 4 - http://www.pythonchallenge.com/pc/def/linkedlist.html --> http://www.pythonchallenge.com/pc/def/linkedlist.php
# <!-- urllib may help. DON'T TRY ALL NOTHINGS, since it will never end. 400 times is more than enough. -->
from urllib.request import Request, urlopen
import re

linkTemplate = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
# curNothing = "12345"
# Hit a stop case and have to manually change starting value using this hint: 
#   Yes. Divide by two and keep going.
curNothing = str(16044 // 2)
curNothing = str(52899)
pattern =r'nothing is (\d+)' 
while curNothing: 
    nextLink = linkTemplate + curNothing
    responseText = urlopen(Request(nextLink)).read().decode()
    try: 
        curNothing = re.search(pattern, responseText).group(1)
    except AttributeError:
        print('New URL:')
        print(re.search(r'([a-z]+).html',responseText).group(0)) 
        curNothing = None

    print(curNothing)   
