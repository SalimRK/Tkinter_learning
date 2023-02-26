from tkinter import *

root = Tk()
root.title("radio")

r = IntVar()
r.set(0)


def clicked(value):
    myLabel.config(text=value)


Radiobutton(root, text="option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

myLabel = Label(root, text=r.get())
myLabel.pack()

root.mainloop()
