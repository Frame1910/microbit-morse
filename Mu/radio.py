import radio
import microbit

# Turn on radio
radio.on()

# Send Function
def radioSend():
    # Send radio message
    radio.send(messageString)
    microbit.display.scroll('Sent')

data = ""
messageString = ""
def radioRecieve():
    # Radio listener
    while True:
        data = radio.receive()
        if data != "none":
            break
    messageString = data
    print(messageString)
