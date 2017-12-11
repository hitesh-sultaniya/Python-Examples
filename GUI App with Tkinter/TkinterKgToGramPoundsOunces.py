from tkinter import *

window = Tk()

def converFromKilogram():
    textGrams.insert(END,"Grams = " + str(float(inputKg.get())*1000))
    textPounds.insert(END,"Pounds = " + str(float(inputKg.get())*2.20462))
    textOunces.insert(END,"Ounces = " + str(float(inputKg.get())*35.274))

lableKg = Label(window,text="Enter Kilogram")
lableKg.grid(row=0,column=0)

inputKg = StringVar()
txtKg = Entry(window,textvariable=inputKg)
txtKg.grid(row=0,column=1,columnspan=2)

btnConvert = Button(window,text="Convert",command=converFromKilogram)
btnConvert.grid(row=0,column=3)

textGrams = Entry(window)
textGrams.grid(row=1,column=0)

textPounds = Entry(window)
textPounds.grid(row=1,column=1)

textOunces = Entry(window)
textOunces.grid(row=1,column=2)

window.mainloop()
