# Micro:morse
Micro:morse is a python based Morse code translator that is in development for a project. The planned features of this script are by order of priority:

**Bold = Completed but could still be changed**
<br>
_Italics = Initiated development_
<br>
~~Strikethrough = Development cancelled~~

- **Translate between Morse code and English**
- ~~Have either function be called at will by the user~~
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
Mu is an editor that has a built in, Real Time terminal where text input is available for use in scripts. Load ``mainFile.py`` into the editor and plug in your Micro:bits to separate computers. Run the code on each Micro:bit (Code is slightly different on each, one running the listener function first to get the conversation started).

When typing in your text, be aware that translated Morse will contain "&" symbols between each letter represented in Morse. These symbols assist the program in reading Morse code later when translating back to English. The receiving device will then stop scanning for a message and send a confirmation packet to the sender saying a message has been received. The sender will now become the receiver, and the receiver now becoming the sender.

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
      # Add each new Morse value to a new array of Morse characters
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
These modules server a purpose of translating any string they receive into their respective language/code. For example, ``englishMorse()`` takes user input and translates it into Morse code. Similarly, ``morseEnglish()`` does the same thing but in reverse.

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
      # Add each new Morse value to a new array of Morse characters
      newString.append(dictionary.get(newArray[i]))
      i += 1
  # Join each array value into one string
  messageString = " ".join(newString)
  print(messageString)
```
The method in both cases is very similar, however, when translating Morse code into English, the string of Morse characters **must** be separated by spaces by the user. The code also is modified like so:
```python
# Instead of:
newArray = list(input)
# Use:
morseList = inputMorse.split(sep=" ")
# Split each Morse character by the spaces between them
```
Changing the parsing method for the user input for Morse code is vital, the `.list()` method divides a string into an array based on words separated by spaces.
However, with Morse code, dots and dashes don't count as words to this method. Therefore the `.split()` method must be used to separate Morse words based a set parameter set to a space: `.split(sep=" ")`.
### Dictionary Modules
 The dictionary modules server as a reference for the script to translate the user input into another language/code. Both dictionaries are actual dictionary methods that contains keys and values. The keys are used as references when translating the user input characters into the corresponding language/code.
```python
newString = []
# Loop the comparison of individualised characters with their value in the target language.
i = 0
while i < len(newArray): # Loops based on number of characters in the array.
    # Add each new Morse value to a new array of Morse characters
    newString.append(dictionary.get(newArray[i]))
    i += 1
```
`.get()` is the method for reading key values and returning their corresponding values in a dictionary. This is looped for every character in the array from the `userInput`. This method is the same for both `englishMorse()` and `morseEnglish()`.

### Conversational Modules
These modules are executed after a message is received from radio. They allow the user to reply to a message they receive. However, on the other end, the device that just sent the message now listens for a reply, and will continue to do so unless cancelled.
An example of this is the `messageInterpreter.py` file.
```python
if "." in receivedString or "-" in receivedString:
      # Split each Morse chracter by the spaces between them
      receivedMorseList = receivedString.split("&")

      receivedMorseString = []
      # Loop the comparison of individualised Morse characters with their value in English
      i = 0
      while i < len(receivedMorseList):
          # Add each translated value to a new array
          receivedMorseString.append(morseToEnglish.get(receivedMorseList[i]))
          i += 1
      # Join each arrat value into one string
      translatedString = "".join(receivedMorseString)
      print("Message Received:")
      print(translatedString)
  else:
      receivedStringLower = receivedString.lower()
      # List each character as an array of characters
      receivedEnglishArray = list(receivedStringLower)

      receivedEnglishString = []
      # Loop the comparison of individualised English characters with their value in Morse
      i = 0
      while i < len(receivedEnglishArray):
          # Add each new Morse value to a new array of morse characters
          receivedEnglishString.append(englishToMorse.get(receivedEnglishArray[i]))
          i += 1
      # Join each arrat value into one string
      translatedString = "&".join(receivedEnglishString)
      print("Message Received:")
      print(translatedString)
```
This massive block of code is a amalgamation of the translator and radio modules.

Parts of the translator modules had to be copied and changed into this module because of the way the script handles data determined in other modules. For example, `receivedString` cannot be handled by the translator modules such as `englishMorse()` because it's value is determined in another stage. There are ways to avoid this and abstract the code further allowing a more dynamic flow, however that would require a re-write of the translator, radio and caller modules so they could handle parameters, allowing modules to be re-used easily in the rest of the program.

### Caller Module - _"Where the magic happens"_
The caller function serves as the user's form of control; they can launch any major function of the script and jump between modules using commands in the terminal. It does this by an infinite loop that checks for button presses on the Micro:bit.

`button_a` = Type in English and translate to Morse code.

`button_b` = Type in Morse code and translate to English.

```python
# User pushes either button A or button B to choose a mode
def caller():
  while True:
    display.scroll("?")
    if button_a.is_pressed():
      englishMorse()
    if button_b.is_pressed():
      morseEnglish()
```
After code is executed the script returns to this script for a new message.
