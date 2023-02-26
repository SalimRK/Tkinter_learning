from tkinter import *

root = Tk()
root.title("radio loop")

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]
pizza = StringVar()
pizza.set("Cheese")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode, command=lambda: clicked(pizza.get())).pack()


def clicked(value):
    myLabel.config(text=value)


myLabel = Label(root, text=pizza.get())
myLabel.pack()

root.mainloop()
