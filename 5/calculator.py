import tkinter
from tkinter import *

root = Tk()
root.title("calcolatoor")

# number input
def validate_numeric_input(text):
    return text.isnumeric()


validate_cmd = root.register(validate_numeric_input)
e = Entry(root, validate="key", validatecommand=(validate_cmd, '%S'), width=20, borderwidth=5, )
e.grid(row=0, column=0, columnspan=3)
e.insert(0, "0")


# buttons

def myButton1onclick():
    e.insert(2, "1")


def myButton2onclick():
    e.insert(2, "2")


def myButton3onclick():
    e.insert(2, "3")


def myButton4onclick():
    e.insert(2, "4")


def myButton5onclick():
    e.insert(2, "5")


def myButton6onclick():
    e.insert(2, "6")


def myButton7onclick():
    e.insert(2, "7")


def myButton8onclick():
    e.insert(2, "8")


def myButton9onclick():
    e.insert(2, "9")


def myButton0onclick():
    e.insert(2, "0")


def myButtonClearonclick():
    e.delete(0, END)


def myButtonAddonclick():
    global num1
    num1 = int(e.get())
    e.delete(0, END)
    global operation
    operation = "+"


def myButtonSubtractonclick():
    global num1
    num1 = int(e.get())
    e.delete(0, END)
    global operation
    operation = "-"


def myButtonMultiplyonclick():
    global num1
    num1 = int(e.get())
    e.delete(0, END)
    global operation
    operation = "*"


def myButtonDivideonclick():
    global num1
    num1 = int(e.get())
    e.delete(0, END)
    global operation
    operation = "/"


def myButtonAnsonclick():
    pass


def myButtonEqualsonclick():
    num2 = int(e.get())
    e.delete(0, END)
    if operation == "+":
        e.insert(0, str(num1 + num2))
    elif operation == "-":
        e.insert(0, str(num1 - num2))
    elif operation == "*":
        e.insert(0, str(num1 * num2))
    elif operation == "/":
        e.insert(0, str(num1 / num2))


# creating buttons
myButton1 = Button(root, text="1", command=myButton1onclick, borderwidth=2, padx=20, pady=10)
myButton2 = Button(root, text="2", command=myButton2onclick, borderwidth=2, padx=20, pady=10)
myButton3 = Button(root, text="3", command=myButton3onclick, borderwidth=2, padx=20, pady=10)
myButton4 = Button(root, text="4", command=myButton4onclick, borderwidth=2, padx=20, pady=10)
myButton5 = Button(root, text="5", command=myButton5onclick, borderwidth=2, padx=20, pady=10)
myButton6 = Button(root, text="6", command=myButton6onclick, borderwidth=2, padx=20, pady=10)
myButton7 = Button(root, text="7", command=myButton7onclick, borderwidth=2, padx=20, pady=10)
myButton8 = Button(root, text="8", command=myButton8onclick, borderwidth=2, padx=20, pady=10)
myButton9 = Button(root, text="9", command=myButton9onclick, borderwidth=2, padx=20, pady=10)
myButton0 = Button(root, text="0", command=myButton0onclick, borderwidth=2, padx=20, pady=10)
myButtonClear = Button(root, text="C", command=myButtonClearonclick, borderwidth=2, padx=20, pady=10)
myButtonEquals = Button(root, text="=", command=myButtonEqualsonclick, borderwidth=2, padx=20, pady=10)
myButtonAdd = Button(root, text="+", command=myButtonAddonclick, borderwidth=2, padx=20, pady=10)
myButtonSubtract = Button(root, text="-", command=myButtonSubtractonclick, borderwidth=2, padx=20, pady=10)
myButtonMultiply = Button(root, text="x", command=myButtonMultiplyonclick, borderwidth=2, padx=20, pady=10)
myButtonDivide = Button(root, text="÷", command=myButtonDivideonclick, borderwidth=2, padx=20, pady=10)
myButtonAns = Button(root, text="ANS", command=myButtonAnsonclick, borderwidth=2, padx=20, pady=10)

# griding buttons
myButton1.grid(row=1, column=0)
myButton2.grid(row=1, column=1)
myButton3.grid(row=1, column=2)
myButton4.grid(row=2, column=0)
myButton5.grid(row=2, column=1)
myButton6.grid(row=2, column=2)
myButton7.grid(row=3, column=0)
myButton8.grid(row=3, column=1)
myButton9.grid(row=3, column=2)
myButton0.grid(row=4, column=1)
myButtonClear.grid(row=4, column=0)
myButtonEquals.grid(row=4, column=2)
myButtonAdd.grid(row=0, column=3)
myButtonSubtract.grid(row=1, column=3)
myButtonMultiply.grid(row=2, column=3)
myButtonDivide.grid(row=3, column=3)
myButtonAns.grid(row=4, column=3)

root.mainloop()
