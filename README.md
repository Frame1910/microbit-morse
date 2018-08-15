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
In order to test this yourself, you need to download the repository, unzip it, then run it from the project root in command line/terminal. Python 3.x is needed to run most of the scripts.
**Note: Any scripts in the "Mu" file directory will not run on anything besides a Micro:bit as those files use MicroPython, not standard Python.**

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
