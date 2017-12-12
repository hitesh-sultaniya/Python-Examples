import psycopg2


def createTable():
    connectObj = psycopg2.connect("dbname='database1' user='postgres' password='priyanka' host='127.0.0.1' port='5432'")
    cursorObj = connectObj.cursor()
    cursorObj.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    connectObj.commit()
    connectObj.close()

def insertData(item,quantity,price):
    connectObj = psycopg2.connect("dbname='database1' user='postgres' password='priyanka' host='127.0.0.1' port='5432'")
    cursorObj = connectObj.cursor()
    cursorObj.execute("INSERT INTO store VALUES(%s,%s,%s)",(item,quantity,price))
    connectObj.commit()
    connectObj.close()

insertData("Coffee Cup",10,4.5)

def viewData():
    connectObj = psycopg2.connect("dbname='database1' user='postgres' password='priyanka' host='127.0.0.1' port='5432'")
    cursorObj = connectObj.cursor()
    cursorObj.execute("SELECT * FROM store")
    allRows = cursorObj.fetchall()
    connectObj.close()
    return allRows



def deleteData(item):
    connectObj = psycopg2.connect("dbname='database1' user='postgres' password='priyanka' host='127.0.0.1' port='5432'")
    cursorObj = connectObj.cursor()
    cursorObj.execute("DELETE FROM store WHERE item=%s",(item,))
    connectObj.commit()
    connectObj.close()

def updateData(item,quantity,price):
    connectObj = psycopg2.connect("dbname='database1' user='postgres' password='priyanka' host='127.0.0.1' port='5432'")
    cursorObj = connectObj.cursor()
    cursorObj.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity,price,item))
    connectObj.commit()
    connectObj.close()

createTable()
insertData("Straberry",4,20.7)
print(viewData())
updateData("Apple",10,90)
print(viewData())
deleteData("Apple")
