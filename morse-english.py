from dict import *

def morseEnglish():
    inputMorse = input("Enter Morse you want to translate to English: ")
    print(inputMorse + " in English is:")
    morseList = inputMorse.split(sep=" ")

    newMorseString = []
    i = 0
    while i < len(morseList):
        newMorseString.append(morseToEnglish.get(morseList[i]))
        i += 1
    messageString = " ".join(newMorseString)
    print(messageString)
morseEnglish()
