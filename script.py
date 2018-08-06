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
    z="--.."
)
def translator():
    inputText = input("Please Input your text:")
    return inputText.lower
    textArray = list(inputText)

    i = 0
    while i < len(textArray):
        print(dictionary.get(textArray[i]))
        i += 1
