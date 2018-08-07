dictionary = {
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
    "-.-.": "k",
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
    "--..": "z"
}

def english():
    inputMorse = input("Enter Morse you want to translate to English: ")
    print(inputMorse + " in English is:")
    morseList = inputMorse.split(sep=" ")

    newMorseString = []
    i = 0
    while i < len(morseList):
        newMorseString.append(dictionary.get(morseList[i]))
        i += 1
    finalMorseString = " ".join(newMorseString)
    print(finalMorseString)
english()
