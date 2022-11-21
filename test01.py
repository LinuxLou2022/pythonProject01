
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import time

print("test")

box = Tk()
Label(box, text="First").grid(row=0, sticky=W)
Label(box, text="Second").grid(row=1, sticky=W)

e1 = Entry(box)
e2 = Entry(box)

e1.grid(row=0, column=1)

box.mainloop()
