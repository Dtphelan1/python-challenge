# 10 - http://www.pythonchallenge.com/pc/return/bull.html 
# hint: len(a[30]) = ?
# visit http://www.pythonchallenge.com/pc/return/sequence.txt - a = [1, 11, 21, 1211, 111221, 
# the sequence is an example of a see-and-say sequence; each sequential value is an oral description of the previous element
from functools import reduce 
def sequenceAtN(n): 
    if n == 1: 
        return [1]
    else: 
        prevSequence = sequenceAtN(n - 1)
        prevSequence.append(saySequence(prevSequence[n - 2]))
        return prevSequence

def saySequence(number): 
    length = len(str(number))
    listRepresentationOfNumber = list(str(number))
    saySequenceResult = []
    previousDigit = ''
    count = 0
    listRepresentationOfNumber.append('')
    for digit in listRepresentationOfNumber:
        if digit == previousDigit:
            count += 1
        else: 
            if previousDigit != '':
                saySequenceResult.append(str(count))
                saySequenceResult.append(str(previousDigit))
            previousDigit = digit
            count = 1
    return int(reduce(lambda x, y: x + y, saySequenceResult, ''))

print(len(str(sequenceAtN(31)[30])))
# produces 5808
# visit: http://www.pythonchallenge.com/pc/return/5808.html