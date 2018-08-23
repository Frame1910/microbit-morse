from dict import *
from sys import *

def englishMorse(message):
    #Make input lower case
    message = message.lower()
    #List each character as an array of characters
    array = list(message)

    newString = []
    #Loop the comparison of individualised English characters with their value in Morse
    i = 0
    while i < len(array):
        #Add each new Morse value to a new array of morse characters
        newString.append(englishToMorse.get(array[i]))
        i += 1
    #Join each arrat value into one string
    translatedString = "&".join(newString)
    print(translatedString)

input = input("Please enter message text: ")
englishMorse(input)
