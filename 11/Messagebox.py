from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Message box app")


# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askyesno("This is my PopUp", "Hello World!")
    myLabel = Label(root, text=response)
    myLabel.pack()
    # if response == 1:
    #     myLabel = Label(root, text="You Clicked YES")
    #     myLabel.pack()
    # elif response == 0:
    #     myLabel = Label(root, text="You Clicked NO")
    #     myLabel.pack()


Button(root, text="Popup", command=popup).pack()

root.mainloop()
