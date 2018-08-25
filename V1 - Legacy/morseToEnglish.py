#Importing Dictionaries
from dict import *

def morseEnglish():
    inputMorse = input("Enter Morse you want to translate to English: ")
    print(inputMorse + " in English is:")
    #Split each Morse chracter by the spaces between them
    morseList = inputMorse.split(sep=" ")

    newMorseString = []
    #Loop the comparison of individualised Morse characters with their value in English
    i = 0
    while i < len(morseList):
        #Add each translated value to a new array
        newMorseString.append(morseToEnglish.get(morseList[i]))
        i += 1
    #Join each arrat value into one string
    messageString = " ".join(newMorseString)
    print(messageString)
