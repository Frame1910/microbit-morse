#Import translation modules
from englishToMorse import *
from morseToEnglish import *
#Import radio modules
from radio import *

#User preses either button A or B to choose mode
def chooseFunction():
    microbit.display.scroll("Choose Mode")
    microbit.display.scroll("Left = English")
    microbit.display.scroll("Right = Morse")
    
    
    while :
        if button_a.is_pressed():
            englishMorse()
            radioSend()
        if button_b.is_pressed():
            morseEnglish()
            radioSend()

#Loop to keep program going
while True:
    chooseFunction()
    #Breaks loop if user inputs "n"
    again = input("Send another Message? y/n ")
    if again == "n":
        break