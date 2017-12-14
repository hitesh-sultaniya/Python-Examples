"""
A programme that stores of book's information below,
"""

from tkinter import *
import BackEnd

window = Tk()

window.wm_title("Book Store")

lblTitle = Label(window,text="Title")
lblTitle.grid(row=0,column=0)

lblTitle = Label(window,text="Author")
lblTitle.grid(row=0,column=2)

lblTitle = Label(window,text="Year")
lblTitle.grid(row=1,column=0)

lblTitle = Label(window,text="ISBN")
lblTitle.grid(row=1,column=2)

strTitle = StringVar()
txtTitle = Entry(window,textvariable=strTitle)
txtTitle.grid(row=0,column=1)

strAuthor = StringVar()
txtAuthor = Entry(window,textvariable=strAuthor)
txtAuthor.grid(row=0,column=3)

strYear = StringVar()
txtYear = Entry(window,textvariable=strYear)
txtYear.grid(row=1,column=1)

strISBN = StringVar()
txtISBN = Entry(window,textvariable=strISBN)
txtISBN.grid(row=1,column=3)

listBookList = Listbox(window,height=10,width=30)
listBookList.grid(row=2,column=0,rowspan=6,columnspan=2)

scrBarList = Scrollbar(window)
scrBarList.grid(row=2,column=2,rowspan=6)

listBookList.configure(yscrollcommand=scrBarList.set)
scrBarList.configure(command=listBookList.yview)

def getSelectedBookRecord(event):
    global selectedRecord

    try:
        index = listBookList.curselection()[0]
        selectedRecord = listBookList.get(index)
        txtTitle.delete(0,END)
        txtTitle.insert(END,selectedRecord[1])
        txtAuthor.delete(0,END)
        txtAuthor.insert(END,selectedRecord[2])
        txtYear.delete(0,END)
        txtYear.insert(END,selectedRecord[3])
        txtISBN.delete(0,END)
        txtISBN.insert(END,selectedRecord[4])
    except IndexError as e:
        pass


listBookList.bind("<<ListboxSelect>>",getSelectedBookRecord)

def fetchAndDisplayData():
    listBookList.delete(0,END)
    listBooks = BackEnd.viewAllBookRecords()
    for bookRow in listBooks:
        listBookList.insert(END,bookRow)

btnViewAll = Button(window,text="View All",width=17,command=fetchAndDisplayData)
btnViewAll.grid(row=2,column=3)

def searchBooks():
    listBookList.delete(0,END)
    listSearchedBooks = BackEnd.searchBookRecord(strTitle.get(),strAuthor.get(),strYear.get(),strISBN.get())
    for searchedBook in listSearchedBooks:
        listBookList.insert(END,searchedBook)

btnSearchEntry = Button(window,text="Search Entry",width=17,command=searchBooks)
btnSearchEntry.grid(row=3,column=3)

def addBookRecord():
    BackEnd.insertBookRecord(strTitle.get(),strAuthor.get(),strYear.get(),strISBN.get())
    listBookList.delete(0,END)
    listBookList.insert(END,(strTitle.get(),strAuthor.get(),strYear.get(),strISBN.get()))

btnAddEntry = Button(window,text="Add Entry",width=17,command=addBookRecord)
btnAddEntry.grid(row=4,column=3)

def updateSelectedBookRecord():
    BackEnd.updateBookRecord(selectedRecord[0],strTitle.get(),strAuthor.get(),strYear.get(),strISBN.get())

btnUpdate = Button(window,text="Update",width=17,command=updateSelectedBookRecord)
btnUpdate.grid(row=5,column=3)

def deleteBookRecord():
    BackEnd.deleteBookRecord(selectedRecord[0])

btnDelete = Button(window,text="Delete",width=17,command=deleteBookRecord)
btnDelete.grid(row=6,column=3)

btnClose = Button(window,text="Close",width=17,command=window.destroy)
btnClose.grid(row=7,column=3)

window.mainloop()
