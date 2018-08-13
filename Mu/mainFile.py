from microbit import *




# DICTIONARY DEFINITIONS ------------------------------------------------------------------------------------------

#Morse to English dictionary
morseToEnglish = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    " ":" "
}

#ENglish to Morse dictionary
englishToMorse = {
    "a":".-",
    "b":"-...",
    "c":"-.-.",
    "d":"-..",
    "e":".",
    "f":"..-.",
    "g":"--.",
    "h":"....",
    "i":"..",
    "j":".---",
    "k":"-.-",
    "l":".-..",
    "m":"--",
    "n":"-.",
    "o":"---",
    "p":".--.",
    "q":"--.-",
    "r":".-.",
    "s":"...",
    "t":"-",
    "u":"..-",
    "v":"...-",
    "w":".--",
    "x":"-..-",
    "y":"-.--",
    "z":"--..",
    " ":" "
}

# RADIO MODULES --------------------------------------------------------------------------------------------

# Turn on radio
radio.on()

# Send Function
def radioSend():
    # Send radio message
    radio.send(messageString)
    microbit.display.scroll('Sent')

data = ""
receivedString = ""
def radioRecieve():
    # Radio listener
    while True:
        data = radio.receive()
        if data != "none":
            break
    receivedString = data
    display.scroll("Received")
    print(receivedString)



# TRANSLATION MODULES ---------------------------------------------------------------------------------------

def englishMorse():
    inputEnglish = input("Enter the English you want to translate: ")
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


# MAIN.PY -------------------------------------------------------------------------------------------------------

#User pushes either button A or button B to choose a mode
def chooseFunction():
    while True:
        display.scroll("?")
        if button_a.is_pressed():
            englishMorse()
        if button_b.is_pressed():
            morseEnglish()
