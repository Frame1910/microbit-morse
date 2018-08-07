from microbit import *
import audio

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

def morse():
    inputEnglish = "Darren"
    inputEnglish = inputEnglish.lower()
    englishArray = list(inputEnglish)

    newEnglishString = []
    i = 0
    while i < len(englishArray):
        newEnglishString.append(dictionary.get(englishArray[i]))
        i += 1
    finalEnglishString = " ".join(newEnglishString)
    return finalEnglishString
