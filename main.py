from englishToMorse import *
from morseToEnglish import *

mode = 0
def chooseFunction():
    mode = input("English or Morse? ")
    mode = mode.lower()
    if mode == "english":
        englishMorse()
    if mode == "morse":
        morseEnglish()

while True:
    chooseFunction()
    again = input("Send another Message? y/n ")
    if again == "n":
        break
