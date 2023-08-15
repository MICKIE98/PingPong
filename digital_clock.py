from tkinter import *
import time

root = Tk()
root.title("Clock")



def present():
    display_time = time.strftime("%I:%M:%S %p")
    digi_clock.config(text=display_time)
    digi_clock.after(200, present)


digi_clock = Label(root, font=("san sarfi", 150), bg="red", foreground="blue")
digi_clock.pack()

present()

root.mainloop()
