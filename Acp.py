from tkinter import *
from datetime import date

root = Tk()
root.title("Getting Started with Widgets")
root.geometry("600x500")
root.configure(bg="black")

lbl = Label(text="Let's Add,Substract,Multiply and Divide Two Numbers!", bg="cyan", fg="black", height=1, width=300)

n1_lbl = Label(text="Enter Number 1", bg="black", fg="cyan")
n1_entry = Entry(bg="cyan", fg="black")

n2_lbl = Label(text="Enter Number 2", bg="black", fg="cyan")
n2_entry = Entry(bg="cyan", fg="black")

def multiply():
    
    n1 = int(n1_entry.get())
    n2 = int(n1_entry.get())
    product = n1*n2
    
    text_box.delete(1.0, END)
    text_box.insert(END, f"Here's the Multiplication: {product}\n")
    
def add():
    n1 = int(n1_entry.get())
    n2 = int(n2_entry.get())
    total = n1 + n2
    
    text_box.delete(1.0, END)
    text_box.insert(END, f"Here's the sum: {total}\n")

def subtract():
    n1 = int(n1_entry.get())
    n2 = int(n2_entry.get())
    result = n1 - n2
    
    text_box.delete(1.0, END)
    text_box.insert(END, f"Here's the difference: {result}\n")

def divide():
    n1 = int(n1_entry.get())
    n2 = int(n2_entry.get())
    result1 = n1/n2
    
    text_box.delete(1.0, END)
    text_box.insert(END, f"Here's the quitent: {result1}\n")
    
text_box = Text(height = 3, bg = "cyan", fg = "black")

btn_add = Button(text = "Add", command = add, height = 1, bg = "black", fg = "cyan")
btn_div = Button(text = "Divide", command = divide, height = 1, bg = "black", fg = "cyan")
btn_mult = Button(text = "Multiply", command = multiply, height = 1, bg = "black", fg = "cyan")
btn_sub = Button(text = "Subtract", command = subtract, height = 1, bg = "black", fg = "cyan")

lbl.pack()
n1_lbl.pack()
n1_entry.pack()
n2_lbl.pack()
n2_entry.pack()
btn_add.pack()
btn_div.pack()
btn_mult.pack()
btn_sub.pack()
text_box.pack()

root.mainloop()