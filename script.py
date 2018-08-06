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

def translator():
    inputText = input("Enter the text you want to translate: ")
    print(inputText + " in Morse Code is:")
    inputText = inputText.lower()
    textArray = list(inputText)

    newString = []
    i = 0
    while i < len(textArray):
        newString.append(dictionary.get(textArray[i]))
        i += 1
    finalString = " ".join(newString)
    print(finalString)
translator()
