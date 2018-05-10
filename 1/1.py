# 1 - http://www.pythonchallenge.com/pc/def/274877906944.html --> http://www.pythonchallenge.com/pc/def/map.html
# Given: encoded string, decode and find new url
import string
import os
dirname = os.path.dirname(__file__)
filePath = os.path.join(dirname, '1.txt')
encoded = open(filePath).read()

def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

print(caesar(encoded, 2))
# yields: 
# i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url

url = "map"
shiftedUrl = caesar(url, 2) 

print('')
print(shiftedUrl)
# yields ocr
