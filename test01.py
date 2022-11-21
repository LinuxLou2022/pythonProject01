
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import time

print("test")

box = Tk()
box.geometry("600x600")
Label(box, text="First").grid(row=0, sticky=W)
Label(box, text="Second").grid(row=1, sticky=W)

e1 = Entry(box)
e2 = Entry(box)

e1.grid(row=0, column=1)
e2.grid(row=1, column=2)

pict2 = Image.open("S.jpg")
img2 = ImageTk.PhotoImage(pict2)
label = Label(image=img2)
label.grid(row=1, column=3)

box.mainloop()
