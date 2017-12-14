import sqlite3

def connectDataBase():
    connect = sqlite3.connect("bookstore.db")
    cursor = connect.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    connect.commit()
    connect.close()

def insertBookRecord(title,author,year,isbn):
    connect = sqlite3.connect("bookstore.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO books VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    connect.commit()
    connect.close()

def viewAllBookRecords():
    connect = sqlite3.connect("bookstore.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM books")
    bookList = cursor.fetchall()
    connect.close()
    return bookList

def searchBookRecord(title="",author="",year="",isbn=""):
    connect = sqlite3.connect("bookstore.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    bookList = cursor.fetchall()
    connect.close()
    return bookList

def deleteBookRecord(id):
    connect = sqlite3.connect("bookstore.db")
    cursor = connect.cursor()
    cursor.execute("DELETE FROM books WHERE id=?",(id,))
    connect.commit()
    connect.close()

def updateBookRecord(id,title,author,year,isbn):
    connect = sqlite3.connect("bookstore.db")
    cursor = connect.cursor()
    cursor.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    connect.commit()
    connect.close()


connectDataBase();
