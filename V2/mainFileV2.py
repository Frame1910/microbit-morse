from sys import *
from microbit import *
import radio
radio.config(length=251)
# Morse to English dictionary
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
# English to Morse dictionary
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

def radioListen():
    radio.on()
    print("Scanning...")
    while True:
        data = radio.receive()
        if data != None:
            if data == "exit":
                exit()
            else:
                break

    print("Received.")

    return data

def radioSend(data):
    radio.on()

    print("Transmitting...")
    radio.send(data)

def englishMorse(message):
    # Make input lower case
    message = message.lower()
    # List each character as an array of characters
    array = list(message)

    newString = []
    # Loop the comparison of individualised English characters with their value in Morse
    i = 0
    while i < len(array):
        # Add each new Morse value to a new array of morse characters
        newString.append(englishToMorse.get(array[i]))
        i += 1
    # Join each arrat value into one string
    translatedString = "&".join(newString)
    print(translatedString)

    return translatedString

def morseEnglish(message):
    # Split each Morse chracter by the spaces between them
    array = message.split("&")

    newString = []
    # Loop the comparison of individualised Morse characters with their value in English
    i = 0
    while i < len(array):
        # Add each translated value to a new array
        newString.append(morseToEnglish.get(array[i]))
        i += 1
    # Join each arrat value into one string
    translatedString = "".join(newString)
    print(translatedString)

    return translatedString

def translator(message):
    if "-" in message or "." in message:
        translatedMessage = morseEnglish(message)
    else:
        translatedMessage = englishMorse(message)

    return translatedMessage

givenData = ""
translatedString = ""
def caller():
    mode = input("send or receive? ")
    while True:
        if mode == "send":
            text = input("Input message text: ")
            messageData = translator(text)
            radioSend(messageData)
            mode = "receive"
        if mode == "receive":
            givenData = radioListen()
            translatedData = translator(givenData)
            print(translatedData)
            mode = "send"