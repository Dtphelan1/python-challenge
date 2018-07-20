# 19 - http://www.pythonchallenge.com/pc/hex/bin.html
# Looks like a commented out email is in the page 
# weird map of india.
# U:butter
# P:fly
import email, base64, wave
import os

dirname = os.path.dirname(__file__)
filePath = os.path.join(dirname, 'email.txt')

message = open(filePath, "r").read()

mail = email.message_from_string(message)
audio = mail.get_payload(0).get_payload(decode=True)
audioFilePath = os.path.join(dirname, 'indian.wav')
audioFile = open(audioFilePath, 'wb');
audioFile.write(audio)

audioFilePath = os.path.join(dirname, 'indian.wav')
sourceFile = wave.open(audioFilePath, 'rb')
destFilePath = os.path.join(dirname, 'result.wav')
destFile = wave.open(destFilePath, 'wb')

print(sourceFile.getnchannels())
print(sourceFile.getsampwidth())
print(sourceFile.getframerate())
destFile.setnchannels(sourceFile.getnchannels())
destFile.setsampwidth(sourceFile.getsampwidth()//2)
destFile.setframerate(sourceFile.getframerate()*2)
frames = sourceFile.readframes(sourceFile.getnframes())
wave.big_endiana = 1
destFile.writeframes(frames)

destFile.close()