dictionary = dict(
    a=".-",
    b="-...",
    c="-.-.",
    d="-..",
    e=".",
    f="..-.",
    g="--.",
    h="....",
    i="..",
    j=".---",
    k="-.-",
    l=".-..",
    m="--",
    n="-.",
    o="---",
    p=".--.",
    q="--.-",
    r=".-.",
    s="...",
    t="-",
    u="..-",
    v="...-",
    w=".--",
    x="-..-",
    y="-.--",
    z="--..")

"""def morse():
    inputEnglish = input("Enter the English you want to translate: ")
    print(inputEnglish + " in Morse Code is:")
    inputText = inputEnglish.lower()
    englishArray = list(inputEnglish)

    newEnglishString = []
    i = 0
    while i < len(englishArray):
        newEnglishString.append(dictionary.get(englishArray[i]))
        i += 1
    finalEnglishString = " ".join(newEnglishString)
    print(finalEnglishString)
    return(finalEnglishString) """

def english():
    inputMorse = input("Enter Morse you want to translate to English: ")
    print(inputMorse + " in English is:")
    morseList = inputMorse.split(sep=" ")

    newMorseString = []
    i = 0
    while i < len(morseList):
        newMorseString.append(dictionary.get(morseList[i]))
        i += 1
    finalMorseString = " ".join(newMorseString)
    print(finalMorseString)
english()
