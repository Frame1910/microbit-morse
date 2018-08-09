import englishToMorse
import morseToEnglish

mode = 0
def chooseFunction():
    mode = input("Language? (1 = English, 2 = Morse)")
    if mode == 1:
        englishMorse()
    if mode == 2:
        morseEnglish()
