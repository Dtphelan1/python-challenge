# http://www.pythonchallenge.com/pc/return/cat.html
# says the cast name is uzi -- 
# http://www.pythonchallenge.com/pc/return/uzi.html
# Clues: 
# 1. Page title - "Whom"
# 2. January 1__6
# 3. Monday the 26th is circled 
# 4. February has 29 days, is a leap year
# 5. Jan 1 is a Thursday
# 6. <!-- he ain't the youngest, he is the second -->
# 7. <!-- todo: buy flowers for tomorrow -->, Possibly Tuesday the 27th

import datetime

print(1016 / 4)
print([x for x in range(1016,1996, 20) if datetime.date(x, 1, 26).isoweekday() == 1])
# gives us [1176, 1356, 1576, 1756, 1976]
# he aint the youngest -- so let's go with 1756
# who was relevant on Jan 26/27, 1756?
# looking it up, Mozart was born on Jan 27 1756


# http://www.pythonchallenge.com/pc/return/mozart.html
