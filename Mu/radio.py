import radio
import microbit

messageString = "Hello World"

# Send Function
def radioSend():
    # Turn on radio
    radio.on()
    # Send radio message
    radio.send(messageString)
    microbit.display.scroll('TRUE')

while True:
    radioSend()