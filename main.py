
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import time


# callable function definitions

def changeImage(aType):
   print(aType)

   frame2.place(anchor='e', relx=1, rely=0)

   img = ImageTk.PhotoImage(Image.open("P.jpg"))
   label = Label(frame2, image=img)
   label.pack(anchor='e')
   if aType == 1:
      frame2.place(anchor='e', relx=1, rely=0)
      img = ImageTk.PhotoImage(Image.open("P.jpg"))
      label = Label(frame2, image=img)
      label.pack(anchor='e')
   elif aType == 2:
      img = ImageTk.PhotoImage(Image.open("S.jpg"))
      label = Label(frame2, image=img)
      label.pack(anchor='e')
   else:
      img = ImageTk.PhotoImage(Image.open("P.jpg"))
      label = Label(frame2, image=img)
      label.pack(anchor='e')

   theBox.update_idletasks()
   label.config(text="test")



theBox = Tk()
theBox.geometry("600x600")
time.sleep(1)

theBox.title("Asset Creator")

frame1 = ttk.Frame(theBox, padding="3 3 12 12").pack(anchor='w')
frame2 = ttk.Frame(theBox, width=50, height=50) #  .pack(anchor='e')

# frame1.pack(anchor='w')

theBox.columnconfigure(0, weight=1)
theBox.rowconfigure(0, weight=1)



# Set up Radio Buttons
v = IntVar()

b1 = Radiobutton(theBox, text="Person", value=1, variable=v, command=changeImage(1)).pack(anchor="w")
b2 = Radiobutton(theBox, text="Ship", value=2, variable=v, command=changeImage(2)).pack(anchor="w")
b3 = Radiobutton(theBox, text="Engine", value=3, variable=v, command=changeImage(3)).pack(anchor="w")
b4 = Radiobutton(theBox, text="Tool", value=4, variable=v, command=changeImage(4)).pack(anchor="w")
b5 = Radiobutton(theBox, text="Miner", value=5, variable=v, command=changeImage(5)).pack(anchor="w")
b6 = Radiobutton(theBox, text="Weapon", value=6, variable=v, command=changeImage(6)).pack(anchor="w")


# -------------------
img = ImageTk.PhotoImage(Image.open("P.jpg"))
label = Label(frame2, image=img).pack(anchor='e')
# label.pack(anchor='e')

theBox.bind()
# ttk.Button(theBox, text="update", command=lambda:changeImage(aType))
theBox.mainloop()



