try:
    import tkinter as tk  # for python 3
except:
    import Tkinter as tk  # for python 2
import pygubu

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

class Application:
    def __init__(self, master):

        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file('GUI.ui')

        #3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('main', master)

    def translator(self):
        inputText = self.entry.get()
        print(inputText)
        inputText = inputText.lower()
        textArray = list(inputText)

        newString = []
        i = 0
        while i < len(textArray):
            newString.append(dictionary.get(textArray[i]))
            i += 1
        finalString = " ".join(newString)



if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()

root = Tk()
gui = GUI(root)
root.mainloop()
