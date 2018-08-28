# Import microbit packages
from microbit import *
# Import radio packages
import radio
#Defines maximum size of data packets in radio.
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
        # Scans until different data other than "None" is heard.
        data = radio.receive()
        if data != None:
            break

    print("Received.")
    # Return the data rectrieved from radio as the result of the function.
    return data

def radioSend(data):
    radio.on()
    # Data is entered through the parameter "data" and sent.
    print("Transmitting...")
    radio.send(data)

def englishMorse(message):
    # Data entered through parameter "message"
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

    return translatedString

def morseEnglish(message):
    # Data entered through parameter "message"
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

    return translatedString

def translator(message):
    # Data entered through parameter "message"
    # If the code detects elements of Morse in "message" then it runs the Morse to English translator.
    if "-" in message or "." in message:
        translatedMessage = morseEnglish(message)
    else:
        translatedMessage = englishMorse(message)
    # Return the translatedMessage as the result of the function.
    return translatedMessage
# Globally defined variables.
givenData = ""
translatedString = ""
def caller():
    # Define mode
    mode = input("send or receive? ")
    # Keeps the whole program looped infinitely
    while True:
        # Uses "mode" to determine to send or receive.
        if mode == "send" or mode == "Send":
            # Runs text input and translation functions if sending.
            text = input("Input message text: ")
            messageData = translator(text)
            radioSend(messageData)
            # Changes mode to receive.
            mode = "receive"
        if mode == "receive" or mode == "Received":
            # Sets givenData to whatever the result of radioListen() is.
            givenData = radioListen()
            # Takes givenData and uses it as a parameter in the translator function.
            translatedData = translator(givenData)
            print(translatedData)
            # Changes mode to send.
            mode = "send"
