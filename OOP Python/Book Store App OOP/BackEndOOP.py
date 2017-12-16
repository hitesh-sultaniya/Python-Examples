import sqlite3


class DatabaseHelper:

    def __init__(self):
        self.connect = sqlite3.connect("bookstore.db")
        self.cursor = self.connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.connect.commit()

    def insertBookRecord(self,title,author,year,isbn):
        self.cursor.execute("INSERT INTO books VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        self.connect.commit()

    def viewAllBookRecords(self):
        self.cursor.execute("SELECT * FROM books")
        bookList = self.cursor.fetchall()
        return bookList

    def searchBookRecord(self,title="",author="",year="",isbn=""):
        self.cursor.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        bookList = self.cursor.fetchall()
        return bookList

    def deleteBookRecord(self,id):
        self.cursor.execute("DELETE FROM books WHERE id=?",(id,))
        self.connect.commit()

    def updateBookRecord(self,id,title,author,year,isbn):
        self.cursor.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
        self.connect.commit()

    def __del__(self):
        self.connect.close()
