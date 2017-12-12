import sqlite3


def createTable():
    connectObj = sqlite3.connect("lite.db")
    cursorObj = connectObj.cursor()
    cursorObj.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    connectObj.commit()
    connectObj.close()

def insertData(item,quantity,price):
    connectObj = sqlite3.connect("lite.db")
    cursorObj = connectObj.cursor()
    cursorObj.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    connectObj.commit()
    connectObj.close()

#insertData("Coffee Cup",10,4.5)

def viewData():
    connectObj = sqlite3.connect("lite.db")
    cursorObj = connectObj.cursor()
    cursorObj.execute("SELECT * FROM store")
    allRows = cursorObj.fetchall()
    connectObj.close()
    return allRows



def deleteData(item):
    connectObj = sqlite3.connect("lite.db")
    cursorObj = connectObj.cursor()
    cursorObj.execute("DELETE FROM store WHERE item=?",(item,))
    connectObj.commit()
    connectObj.close()

def updateData(item,quantity,price):
    connectObj = sqlite3.connect("lite.db")
    cursorObj = connectObj.cursor()
    cursorObj.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity,price,item))
    connectObj.commit()
    connectObj.close()


print(viewData())
updateData("Coffee Cup",10,89.9)
print(viewData())
