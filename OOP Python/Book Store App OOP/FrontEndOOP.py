"""
A programme that stores of book's information below,
"""

from tkinter import *
from BackEndOOP import DatabaseHelper


class FrontEnd(object):

    def __init__(self,window):

       self.window = window
       self.window.wm_title("Book Store")
       self.databaseHelper = DatabaseHelper()
       lblTitle = Label(self.window,text="Title")
       lblTitle.grid(row=0,column=0)

       lblTitle = Label(self.window,text="Author")
       lblTitle.grid(row=0,column=2)

       lblTitle = Label(self.window,text="Year")
       lblTitle.grid(row=1,column=0)

       lblTitle = Label(self.window,text="ISBN")
       lblTitle.grid(row=1,column=2)

       self.strTitle = StringVar()
       self.txtTitle = Entry(self.window,textvariable=self.strTitle)
       self.txtTitle.grid(row=0,column=1)

       self.strAuthor = StringVar()
       self.txtAuthor = Entry(self.window,textvariable=self.strAuthor)
       self.txtAuthor.grid(row=0,column=3)

       self.strYear = StringVar()
       self.txtYear = Entry(self.window,textvariable=self.strYear)
       self.txtYear.grid(row=1,column=1)

       self.strISBN = StringVar()
       self.txtISBN = Entry(self.window,textvariable=self.strISBN)
       self.txtISBN.grid(row=1,column=3)

       self.listBookList = Listbox(self.window,height=10,width=30)
       self.listBookList.grid(row=2,column=0,rowspan=6,columnspan=2)
       self.listBookList.bind("<<ListboxSelect>>",self.getSelectedBookRecord)
       scrBarList = Scrollbar(self.window)
       scrBarList.grid(row=2,column=2,rowspan=6)
       self.listBookList.configure(yscrollcommand=scrBarList.set)
       scrBarList.configure(command=self.listBookList.yview)

       btnViewAll = Button(self.window,text="View All",width=17,command=self.fetchAndDisplayData)
       btnViewAll.grid(row=2,column=3)

       btnSearchEntry = Button(self.window,text="Search Entry",width=17,command=self.searchBooks)
       btnSearchEntry.grid(row=3,column=3)

       btnAddEntry = Button(self.window,text="Add Entry",width=17,command=self.addBookRecord)
       btnAddEntry.grid(row=4,column=3)

       btnUpdate = Button(self.window,text="Update",width=17,command=self.updateSelectedBookRecord)
       btnUpdate.grid(row=5,column=3)

       btnDelete = Button(self.window,text="Delete",width=17,command=self.deleteBookRecord)
       btnDelete.grid(row=6,column=3)

       btnClose = Button(self.window,text="Close",width=17,command=self.window.destroy)
       btnClose.grid(row=7,column=3)


    def getSelectedBookRecord(self,event):
        try:
            index = self.listBookList.curselection()[0]
            self.selectedRecord = self.listBookList.get(index)
            self.txtTitle.delete(0,END)
            self.txtTitle.insert(END,self.selectedRecord[1])
            self.txtAuthor.delete(0,END)
            self.txtAuthor.insert(END,self.selectedRecord[2])
            self.txtYear.delete(0,END)
            self.txtYear.insert(END,self.selectedRecord[3])
            self.txtISBN.delete(0,END)
            self.txtISBN.insert(END,self.selectedRecord[4])
        except IndexError as e:
            pass



    def fetchAndDisplayData(self):
        self.listBookList.delete(0,END)
        listBooks = self.databaseHelper.viewAllBookRecords()
        for bookRow in listBooks:
            self.listBookList.insert(END,bookRow)


    def searchBooks(self):
        self.listBookList.delete(0,END)
        listSearchedBooks = self.databaseHelper.searchBookRecord(self.strTitle.get(),self.strAuthor.get(),self.strYear.get(),self.strISBN.get())
        for searchedBook in listSearchedBooks:
            self.listBookList.insert(END,searchedBook)


    def addBookRecord(self):
        self.databaseHelper.insertBookRecord(self.strTitle.get(),self.strAuthor.get(),self.strYear.get(),self.strISBN.get())
        self.listBookList.delete(0,END)
        self.listBookList.insert(END,(self.strTitle.get(),self.strAuthor.get(),self.strYear.get(),self.strISBN.get()))


    def updateSelectedBookRecord(self):
        self.databaseHelper.updateBookRecord(self.selectedRecord[0],self.strTitle.get(),self.strAuthor.get(),self.strYear.get(),self.strISBN.get())


    def deleteBookRecord(self):
        self.databaseHelper.deleteBookRecord(self.selectedRecord[0])



window = Tk()
FrontEnd(window)
window.mainloop()
