from dict import *

def englishMorse():
    inputEnglish = input("Enter the English you want to translate: ")
    print(inputEnglish + " in Morse Code is:")
    inputEnglish = inputEnglish.lower()
    englishArray = list(inputEnglish)
#    englishArray = inputEnglish.split(sep=" ")

    newEnglishString = []
    i = 0
    while i < len(englishArray):
        newEnglishString.append(englishToMorse.get(englishArray[i]))
        i += 1
    messageString = " ".join(newEnglishString)
    print(messageString)
