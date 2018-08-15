# Micro:morse
Micro:morse is a python based Morse code translator that is in development for a project. The planned features of this script are by order of priority:

**Bold = Completed but could still be changed**
<br>
_Italics = Initiated development_
<br>
~~Strikethrough = Development cancelled~~

- **Translate between Morse code and English**
- **Have either function be called at will by the user**
- **Transmit the translated data over radio using Micro:bits**
- **Input message data into the Micro:bit via a terminal interface on a computer/laptop**
- Allow users to have a conversation over this communication method, this includes:
  - ~~Sending a message at will~~
  - ~~Being able to receive a message at any time from someone else~~
  - _Two way conversation, with both parties having the same code being executed on each one of their Micro:bits_

## Usage
In order to test this yourself, you need:
- 2 Micro:bits
- The Mu Python Editor
Mu is an editor that has a built in, Real Time terminal where text input is available for use in scripts. Load ``mainFile.py`` into the editor and plug in your Micro:bits to separate computers

## Documentation
This project is being developed on Atom by GitHub using Python as the primary language.
<br>
Originally, there was meant to be 7 different modules:
- Translation Modules
  - English to Morse
  - Morse to English
- Radio Communications
  - Radio Receiving
  - Radio Sending
- Dictionaries
  - English to Morse
  - Morse to English
- Caller (Main function the user will interact with)

## Modular Details

### Radio Communication Modules
These two modules contain the configuration of data transfer via a radio signal between Micro:bits. Each module is slightly different and they can **not** be implemented as individualised functions. This is due to the fact that the outgoing message is determined within another function and thus the variable cannot be used in another function. Like so:
```python
newEnglishString = []
  # Loop the comparison of individualised English characters with their value in Morse
  i = 0
  while i < len(englishArray):
      # Add each new Morse value to a new array of morse characters
      newEnglishString.append(englishToMorse.get(englishArray[i]))
      i += 1
  # Join each arrat value into one string
  messageString = " ".join(newEnglishString)
  print(messageString)
```
```python
def radioSend():
    # Radio Sending
    radio.on()
    while True:
        # Send radio message
        radio.send(messageString)
        print("Sending")
        display.scroll('Sent')
```
The variable ``messageString`` is defined in an external function and cannot be read by the ``radioSend()`` function.

To fix this issue, the ``radioSend()`` function must be not exist. It's contents must be entered in the translation functions themselves. This reduces some flexibility in the algorithim as a whole.
### Translation Modules
These modules server a purpose of translating any string they receive into their respective language/code. For example, ``englishMorse()`` takes user input and translates it into morse code. Similarly, ``morseEnglish()`` does the same thing but in reverse.

These functions do this in the following way:
```python
input = input("Enter the English you want to translate: ")
  # Make input lower case
  input = input.lower()
  # List the string as an array of characters
  newArray = list(input)

  newString = []
  # Loop the comparison of individualised characters with their value in the target language.
  i = 0
  while i < len(englishArray): # Loops based on number of characters in the array.
      # Add each new Morse value to a new array of morse characters
      newEnglishString.append(englishToMorse.get(englishArray[i]))
      i += 1
  # Join each array value into one string
  messageString = " ".join(newEnglishString)
  print(messageString)
```
The method in both cases is very similar, however, when translating morse code into English, the string of morse characters **must** be seperated by spaces by the user.
