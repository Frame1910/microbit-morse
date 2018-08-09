from englishToMorse import *
from morseToEnglish import *

mode = 0
def chooseFunction():
    mode = input("English or Morse? (Case Sens) ")
    if mode == "English":
        englishMorse()
    if mode == "Morse":
        morseEnglish()

while True:
    chooseFunction()
    again = input("Send another Message? y/n ")
    if again == "n":
        break
