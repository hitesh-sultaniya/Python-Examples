from tkinter import *

window = Tk()

def kilometersToMeters():
    meters = int(e1_value.get())*1000
    t1.insert(END,meters)

b1 = Button(window,text="Execute",command=kilometersToMeters)
b1.grid(row=0,column=0)

e1_value = StringVar()
e1 = Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

t1 = Text(window,height=1,width=40)
t1.grid(row=1,column=0,columnspan=2)

window.mainloop()
