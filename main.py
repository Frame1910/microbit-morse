#Import translation modules
from englishToMorse import *
from morseToEnglish import *

#User inputs "English" or "Morse" depending on function they want
mode = 0
def chooseFunction():
    mode = input("English or Morse? ")
    #Makes user input lower case
    mode = mode.lower()
    if mode == "english":
        englishMorse()
    if mode == "morse":
        morseEnglish()
#Loop to keep program going
while True:
    chooseFunction()
    #Breaks loop if user inputs "n"
    again = input("Send another Message? y/n ")
    if again == "n":
        break
