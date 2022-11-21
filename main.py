
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import time


# callable function definitions

def changeImage(aType, frame2):
   print(aType)
   frame2.pack_forget()
#   theFrame = ttk.Frame(theBox)
#   theBox.update_idletasks()

#   frame2.place(anchor='ne', width=250, height=250, relx=1, rely=0)
#   img = ImageTk.PhotoImage(Image.open("P.jpg"))
#   label = Label(frame2, image=img)
#   label.pack(anchor='e')
#   time.sleep(2)
   if aType == 1:
      print("#1 works")
      #  frame2 = ttk.Frame(theBox, width=250, height=250)
      #  frame2.place(anchor='ne', width=250, height=250, relx=1, rely=0)
      pict1 = Image.open("P.jpg")
      img1 = ImageTk.PhotoImage(pict1)
      label1 = Label(frame2, image=img1)
      #  label1.config(text="test")
#      theBox.update_idletasks()
      label1.pack(anchor='center')
      frame2.pack(anchor='ne')
   elif aType == 2:
      print("#2 works")
      #  frame2 = ttk.Frame(theBox, width=250, height=250)
      #  frame2.place(anchor='ne', width=350, height=350, relx=1, rely=0)
      pict2 = Image.open("S.jpg")
      img2 = ImageTk.PhotoImage(pict2)
      label2 = Label(frame2, image=img2)
#      theBox.update_idletasks()
      label2.config(text="test")
      label2.pack(anchor='ne')
      #  frame2.pack(anchor='ne')
   else:
      print("# works")
      img = ImageTk.PhotoImage(Image.open("P.jpg"))
      label = Label(frame2, image=img)
      label.pack(anchor='ne')

   theBox.update_idletasks()
#   label.config(text="test")
   theBox.bind()



theBox = Tk()
theBox.geometry("600x600")
time.sleep(1)

theBox.title("Asset Creator")

frame1 = ttk.Frame(theBox, padding="3 3 12 12")
frame1.pack(anchor='nw')
frame2 = ttk.Frame(theBox, width=50, height=50)
frame2.pack(anchor='ne')

theBox.columnconfigure(0, weight=1)
theBox.rowconfigure(0, weight=1)

# Set up Radio Buttons
v = IntVar()

b1 = Radiobutton(theBox, text="Person", value=1, variable=v, command=lambda:changeImage(1,frame2)).pack(anchor="nw")
b2 = Radiobutton(theBox, text="Ship", value=2, variable=v, command=lambda:changeImage(2,frame2)).pack(anchor="nw")
b3 = Radiobutton(theBox, text="Engine", value=3, variable=v, command=lambda:changeImage(3,frame2)).pack(anchor="nw")
b4 = Radiobutton(theBox, text="Tool", value=4, variable=v, command=lambda:changeImage(4,frame2)).pack(anchor="nw")
b5 = Radiobutton(theBox, text="Miner", value=5, variable=v, command=lambda:changeImage(5,frame2)).pack(anchor="nw")
b6 = Radiobutton(theBox, text="Weapon", value=6, variable=v, command=lambda:changeImage(6,frame2)).pack(anchor="nw")


# -------------------
#  img = ImageTk.PhotoImage(Image.open("P.jpg"))
#  label = Label(frame2, image=img)#  .pack(anchor='e')
#  label.pack(anchor='ne')

theBox.bind()
# ttk.Button(theBox, text="update", command=lambda:changeImage(aType))
theBox.mainloop()



