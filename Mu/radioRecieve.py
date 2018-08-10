import radio
import microbit

# Turn on radio
radio.on()

data = ""
messageString = ""
def radioRecieve():
    # Radio listener
    while True:
        data = radio.receive()
        if data != "none":
            break
    messageString = data
    microbit.display.scroll('Hello!' + messageString)