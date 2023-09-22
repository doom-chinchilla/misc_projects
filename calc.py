# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from tkinter import * 

# globally declaring the expression variable 
expression = ""

def press(num): 
    global expression 

    expression = expression + str(num)
    expression.set(expression)

def equalpress():
    try: 
        global expression 

        total = str(eval(expression))
        equation.set(total)

        expression = ""

    except: 
        equation.set("Error!")
        expression = ""

def clear(): 
    global expression 
    expression = ""
    equation.set("")

# == driver code == 
if __name__ == "__main__": 
    gui = Tk()

    gui.configure(background = "light blue")
    gui.title = "Calculator"
    gui.geometry = ("275x150")

    equation = StringVar()

    expression_field = Entry(gui, textvar=equation)
    expression_field.grid(columnspan=4,ipadx=70)

    # create all the grid buttons 
    b1 = Button(gui, text="1",fg='black',bg="light grey",command=lambda: press(1), height=1, width=7)
    b1.grid(row=2,column=0)
    
    b2 = Button(gui, text="2",fg='black',bg="light grey",command=lambda: press(2), height=1, width=7)
    b2.grid(row=2,column=1)
    
    b3 = Button(gui, text="3",fg='black',bg="light grey",command=lambda: press(3), height=1, width=7)
    b3.grid(row=2,column=2)
    
    b4 = Button(gui, text="4",fg='black',bg="light grey",command=lambda: press(4), height=1, width=7)
    b4.grid(row=2,column=3)
    
    b5 = Button(gui, text="5",fg='black',bg="light grey",command=lambda: press(5), height=1, width=7)
    b5.grid(row=3,column=0)
    
    b6 = Button(gui, text="6",fg='black',bg="light grey",command=lambda: press(6), height=1, width=7)
    b6.grid(row=3,column=1)
    
    b7 = Button(gui, text="7",fg='black',bg="light grey",command=lambda: press(7), height=1, width=7)
    b7.grid(row=3,column=2)
    
    b8 = Button(gui, text="8",fg='black',bg="light grey",command=lambda: press(8), height=1, width=7)
    b8.grid(row=3,column=3)
    
    b9 = Button(gui, text="9",fg='black',bg="light grey",command=lambda: press(9), height=1, width=7)
    b9.grid(row=4,column=0)
    
    b0 = Button(gui, text="0",fg='black',bg="light grey",command=lambda: press(0), height=1, width=7)
    b0.grid(row=4,column=1)
    
    bDecimal = Button(gui, text=".",fg='black',bg="light grey",command=lambda: press("."), height=1, width=7)
    bDecimal.grid(row=4,column=2)
    
    bPlus = Button(gui, text = "+", fg="black", bg="light grey", command=lambda: press("+"), height=1, width=7)
    bPlus.grid(row=5, column=0)
    
    bDivide = Button(gui, text = "/", fg="black", bg="light grey", command=lambda: press("/"), height=1, width=7)
    bDivide.grid(row=5, column=1)
    
    bMultiply = Button(gui, text = "*", fg="black", bg="light grey", command=lambda: press("*"), height=1, width=7)
    bMultiply.grid(row=5, column=2)
    
    bEqual = Button(gui, text = "=", fg="black", bg="light grey", command=lambda: equalpress(), height=1, width=7)
    bEqual.grid(row=5, column=3)
    
    bClear = Button(gui, text = "Clear", fg="black", bg="light grey", command=lambda: clear(), height=1, width=7)
    bClear.grid(row=6, column=0)
    
    # start the gui 
    gui.mainloop()