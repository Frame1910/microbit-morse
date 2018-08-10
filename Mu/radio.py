import radio
import microbit

messageString = "Hello World"

# Turn on radio
radio.on()

# Send Function
def radioSend():
    # Send radio message
    radio.send(messageString)
    microbit.display.scroll('TRUE')

while True:
    radioSend()
