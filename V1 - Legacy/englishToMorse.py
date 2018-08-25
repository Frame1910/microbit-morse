#Importing Dictionaries
from dict import *

def englishMorse():
    inputEnglish = input("Enter the English you want to translate: ")
    print(inputEnglish + " in Morse Code is:")
    #Make input lower case
    inputEnglish = inputEnglish.lower()
    #List each character as an array of characters
    englishArray = list(inputEnglish)

    newEnglishString = []
    #Loop the comparison of individualised English characters with their value in Morse
    i = 0
    while i < len(englishArray):
        #Add each new Morse value to a new array of morse characters
        newEnglishString.append(englishToMorse.get(englishArray[i]))
        i += 1
    #Join each arrat value into one string
    messageString = " ".join(newEnglishString)
    print(messageString)
