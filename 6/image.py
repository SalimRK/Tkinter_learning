from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("image.py")
root.iconbitmap("D:\MyPC\Projects\coding\python\Tkinter_learning\\6\Photo-icon.ico")
path = "D:\MyPC\Projects\coding\python\Tkinter_learning\\6\Photo.png"

myImage = ImageTk.PhotoImage(Image.open(path))
myLabel = Label(image=myImage)
myLabel.grid(column=0, row=0)
exitButton = Button(root, text="Exit", command=exit)
exitButton.grid(column=1, row=0)

root.mainloop()