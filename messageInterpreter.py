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


# REQUIRES TESTING --------------------------------------------------------------------------
receivedString = "....&.&.-..&.-..&---& &.--&---&.-.&.-..&-.."
def messageInterpreter():
    if "." in receivedString or "-" in receivedString:
        # Split each Morse chracter by the spaces between them
        receivedMorseList = receivedString.split(sep="&")
        print(receivedMorseList)

        receivedMorseString = []
        # Loop the comparison of individualised Morse characters with their value in English
        i = 0
        while i < len(receivedMorseList):
            # Add each translated value to a new array
            receivedMorseString.append(morseToEnglish.get(receivedMorseList[i]))
            print(receivedMorseString)
            i += 1
        # Join each arrat value into one string
        translatedString = "".join(receivedMorseString)
        print("Message Received:")
        print(translatedString)
    else:
        receivedStringLower = receivedString.lower()
        # List each character as an array of characters
        receivedEnglishArray = list(receivedStringLower)

        receivedEnglishString = []
        # Loop the comparison of individualised English characters with their value in Morse
        i = 0
        while i < len(receivedEnglishArray):
            # Add each new Morse value to a new array of morse characters
            receivedEnglishString.append(englishToMorse.get(receivedEnglishArray[i]))
            i += 1
        # Join each arrat value into one string
        translatedString = "&".join(receivedEnglishString)
        print("Message Received:")
        print(translatedString)
messageInterpreter()
