# 13 - http://www.pythonchallenge.com/pc/return/disproportional.html
# Button 5 is clickable - http://www.pythonchallenge.com/pc/phonebook.php
# produces xml -- let's use an xml client

import xmlrpc.client
conn = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
# List avail methods
print(conn.system.listMethods())
# Look up more info re: phone
print(conn.system.methodHelp("phone"))
print(conn.system.methodSignature("phone"))
# Let's check on bert
print(conn.phone("Bert"))
print(conn.phone("Bert", "ITALY"))