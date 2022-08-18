import sqlite3


def CustomerData():
    con = sqlite3.connect('customer.db')
    cursor = con.cursor()
    cursor.execute("""  create table IF NOT EXISTS customer(
            custID INT PRIMARY KEY NOT NULL,
            name TEXT,
            task TEXT,
            price  INT 
            ) """)
    con.commit()
    con.close()


def addCustomer(custID, name, order, price):
    con = sqlite3.connect('customer.db')
    cursor = con.cursor()
    cursor.execute('insert into customer values (?,?,?,?)',
                   (custID, name, order, price))
    con.commit()
    con.close()


def showAllCustomer():
    con = sqlite3.connect('customer.db')
    cursor = con.cursor()
    data = cursor.execute('select * from customer')
    con.commit()
    return data


def deleteCustomers():
    con = sqlite3.connect('customer.db')
    cursor = con.cursor()
    cursor.execute(f'delete from customer ')
    con.commit()
    con.close()


def access_path():
    con = sqlite3.connect('access.db')
    cursor = con.cursor()
    cursor.execute("""  create table IF NOT EXISTS access(
            manager TEXT PRIMARY KEY NOT NULL
            ) """)
    con.commit()
    con.close()


def addManager(managerName):
    con = sqlite3.connect('access.db')
    cursor = con.cursor()
    cursor.execute('insert into access values(?)', (managerName))
    con.commit()
    con.close()


def showAllManagers():
    con = sqlite3.connect('access.db')
    cursor = con.cursor()
    data = cursor.execute('select * from access')
    con.commit()
    return data
