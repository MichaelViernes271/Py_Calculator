"""
 Name: Viernes, Michael
 Date:06/07/2023 11:37:06 pm
"""

from tkinter import Tk, Entry, Button, StringVar
import tkinter.font as font


class Calculator(object):
    """Basic calculator. Can add, sub, mult, divide, percent, PEMDAS."""

    def __init__(self, master):
        super(Calculator, self).__init__()
        master.title("Py Calculator")
        master.geometry("357x420+0+0")
        master.config(bg="gray")
        master.resizable(False, False)

        # define font
        my_font = font.Font(family="Bell Gothic Std Black", size=12)

        # write the equation on the screen
        self.equation = StringVar()
        self.entry_value = ""
        Entry(width=17, bg="#ffff00", font=("Bell Gothic Std Black", 28),
              textvariable=self.equation).place(x=0, y=0)

        # input buttons for basic operations and numbers
        # grouping
        button_01 = Button(master, font=my_font, width=11, height=4, text="(",
                           relief="flat", bg="white", command=lambda: self.show("(")).place(x=0, y=50)
        button_02 = Button(master, font=my_font, width=11, height=4, text=")",
                           relief="flat", bg="white", command=lambda: self.show(")")).place(x=90, y=50)
        # percent
        button_03 = Button(master, font=my_font, width=11, height=4, text="%",
                           relief="flat", bg="white", command=lambda: self.show("%")).place(x=180, y=50)
        # numbers
        button_04 = Button(master, font=my_font, width=11, height=4, text="1",
                           relief="flat", bg="white", command=lambda: self.show(1)).place(x=0, y=125)
        button_05 = Button(master, font=my_font, width=11, height=4, text="2",
                           relief="flat", bg="white", command=lambda: self.show(2)).place(x=90, y=125)
        button_06 = Button(master, font=my_font, width=11, height=4, text="3",
                           relief="flat", bg="white", command=lambda: self.show(3)).place(x=180, y=125)
        button_07 = Button(master, font=my_font, width=11, height=4, text="4",
                           relief="flat", bg="white", command=lambda: self.show(4)).place(x=0, y=200)
        button_08 = Button(master, font=my_font, width=11, height=4, text="5",
                           relief="flat", bg="white", command=lambda: self.show(5)).place(x=90, y=200)
        button_09 = Button(master, font=my_font, width=11, height=4, text="6",
                           relief="flat", bg="white", command=lambda: self.show(6)).place(x=180, y=200)
        button_10 = Button(master, font=my_font, width=11, height=4, text="7",
                           relief="flat", bg="white", command=lambda: self.show(7)).place(x=0, y=275)
        button_11 = Button(master, font=my_font, width=11, height=4, text="8",
                           relief="flat", bg="white", command=lambda: self.show(8)).place(x=180, y=275)
        button_12 = Button(master, font=my_font, width=11, height=4, text="9",
                           relief="flat", bg="white", command=lambda: self.show(9)).place(x=90, y=275)
        button_13 = Button(master, font=my_font, width=11, height=4, text="0",
                           relief="flat", bg="white", command=lambda: self.show(0)).place(x=90, y=350)
        button_14 = Button(master, font=my_font, width=11, height=4, text=".",
                           relief="flat", bg="white", command=lambda: self.show(".")).place(x=180, y=350)
        # operations
        button_15 = Button(master, font=my_font, width=11, height=4, text="+",
                           relief="flat", bg="white", command=lambda: self.show("+")).place(x=270, y=350)
        button_16 = Button(master, font=my_font, width=11, height=4, text="-",
                           relief="flat", bg="white", command=lambda: self.show("-")).place(x=270, y=200)
        button_17 = Button(master, font=my_font, width=11, height=4, text="/",
                           relief="flat", bg="white", command=lambda: self.show("/")).place(x=270, y=50)
        button_18 = Button(master, font=my_font, width=11, height=4, text="*",
                           relief="flat", bg="white", command=lambda: self.show("*")).place(x=270, y=125)
        button_19 = Button(master, font=my_font, width=11, height=4, text="=",
                           relief="flat", bg="white", command=self.solve).place(x=270, y=350)
        # clear
        button_20 = Button(master, font=my_font, width=11, height=4, text="C",
                           relief="flat", command=self.clear).place(x=0, y=350)

    def show(self, value):
        """display the expression"""
        print(f"value/operand: {value}")
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        """clears the screen"""
        print("clear screen")
        self.entry_value = ""
        self.equation.set(self.entry_value)

    def solve(self):
        """evaluate expression"""
        result = eval(self.entry_value)
        self.equation.set(result)
        print(f"result: {result}")


root = Tk()
calculator = Calculator(root)
root.mainloop()


# tutorial reference
#
# Parvat Computer Technology. (2021, April 16).
# Creating A Calculator Using Tkinter | Python Tkinter GUI Tutorial [Video].
# YouTube. https://www.youtube.com/watch?v=6CZB6VTy3Hg
