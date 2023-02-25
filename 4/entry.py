from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=5, )
e.pack()
e.insert(0, "Enter Your Name")


def myClick():
    helo = f'Hello {e.get()}'
    myLabel = Label(root, text=helo)
    myLabel.pack()


myButton = Button(root, text="Click Me!", command=myClick, borderwidth=2)
myButton.pack()

root.mainloop()
