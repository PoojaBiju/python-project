# Tkinter is a standard Python library used for creating graphical user interfaces (GUIs).
# Tkinter provides a way to create windows, dialogs, buttons, text fields, and other common GUI elements in a Python application.



from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("clock")

def time():
    string = strftime('%H:%M:%S %p')
    Label.config(text=string)
    Label.after(1000,time)

Label = Label(root,font=("ds-digital",80),background="black",foreground="cyan")
Label.pack(anchor='center')
time()

mainloop()
































# *************************

# import tkinter as ui
# import time
#
# window = ui.Tk()
#
# def update_clock():
#     hours = time.strftime("%I")
#     minutes = time.strftime("%M")
#     seconds = time.strftime("%S")
#     am_or_pm = time.strftime(("%p"))
#     time_text = hours + ":" + minutes + ":" + seconds + " " + am_or_pm
#     digital_clock_lbl.config(text=time_text)
#     digital_clock_lbl.after(1000,update_clock)
#
#
# digital_clock_lbl=ui.Label(window,text="00:00:00",
#                            font="Helvetica 72 bold")
#
# digital_clock_lbl.pack()
#
# update_clock()
#
# window.mainloop()




















