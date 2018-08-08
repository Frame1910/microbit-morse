import radio
import microbit

messageString = ""
def radioRecieve():
    # Turn on radio
    radio.on()
    # Radio listener
    while True:
        radio.receive()
        if radio.receive() != "none":
            break
        
    messageString = radioRecieve()
    microbit.display.scroll("TRUE")
    return messageString
while True:
    radioRecieve()