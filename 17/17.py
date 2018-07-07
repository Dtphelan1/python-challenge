# 17 - http://www.pythonchallenge.com/pc/return/romance.html
# Hint: Picture is of "cookies"
# Hint: Picture contains image we've seen before in puzzle 4 
from urllib.request import urlopen
from urllib.parse import unquote_plus, unquote_to_bytes
import re, bz2

# open up puzzle#4 url
orig = urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php')
choco = orig.getheader("Set-Cookie")
print(choco)
# Sugests we use busyNothing instead of nothing

num = '12345'
info = ''
# while(True):
while(False):
    res = urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='+num)
    raw = res.read().decode("utf-8")
    print(raw)
    cookie = res.getheader("Set-Cookie")
    # Accumulate all the cookie info into one variable
    info += re.search('info=(.*?);', cookie).group(1)
    match = re.search('the next busynothing is (\d+)', raw)
    if match == None: 
        break
    else:
        num = match.group(1)
# Concat the info with spaces
res = unquote_to_bytes(info.replace("+", " "))
print(res)
#  It's compressed binary -- decode with bz2
print(bz2.decompress(res).decode())
# !!! Result: "is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand."

# References the 26th -- Mozarts bDay 
# Moz dad is Leopold -- we need his phonenumber -- go back to prev puzz
import xmlrpc.client
conn = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
# Call him
print(conn.phone("Leopold"))
# 555-VIOLIN
# Visit: http://www.pythonchallenge.com/pc/return/violin.html
# Comment: "no! i mean yes! but ../stuff/violin.php."
# Visit: http://www.pythonchallenge.com/pc/stuff/violin.php
#  Looks like we need to literallty send him the message that "the flowers are on the way"
from urllib.request import Request
from urllib.parse import quote_plus

url = "http://www.pythonchallenge.com/pc/stuff/violin.php"
msg = "the flowers are on their way"
req = Request(url, headers = { "Cookie": "info=" + quote_plus(msg)})

print(urlopen(req).read().decode())
# <html>
# <head>
#   <title>it's me. what do you want?</title>
#   <link rel="stylesheet" type="text/css" href="../style.css">
# </head>
# <body>
# 	<br><br>
# 	<center><font color="gold">
# 	<img src="leopold.jpg" border="0"/>
# <br><br>
# oh well, don't you dare to forget the balloons.</font>
# </body>
# </html>

# Visit: http://www.pythonchallenge.com/pc/return/balloons.html