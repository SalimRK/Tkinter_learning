from tkinter import *

root = Tk()
root.title("Frames")

frame = LabelFrame(root, text="label frame", pady=5, padx=5)
frame.pack(padx=10, pady=10)


def b1onclick():
    pass


myButton = Button(frame, text="Dont Click Here", command=b1onclick)
myButton.pack()
root.mainloop()
