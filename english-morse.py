def englishMorse():
    inputEnglish = input("Enter the English you want to translate: ")
    print(inputEnglish + " in Morse Code is:")
    inputText = inputEnglish.lower()
    englishArray = list(inputEnglish)

    newEnglishString = []
    i = 0
    while i < len(englishArray):
        newEnglishString.append(dictionary.get(englishArray[i]))
        i += 1
    messageString = " ".join(newEnglishString)
    print(messageString)
