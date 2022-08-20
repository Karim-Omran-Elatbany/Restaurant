import sqlite3


def CustomerData():
    con = sqlite3.connect('customer.db')
    cursor = con.cursor()
    cursor.execute("""  create table IF NOT EXISTS customer(
            custID INTEGER PRIMARY KEY,
            name TEXT,
            task TEXT,
            price INT 
            ) """)
    con.commit()
    con.close()


def selectcustomer(custID):
    con = sqlite3.connect('customer.db')
    cursor = con.cursor()
    data = cursor.execute('SELECT * FROM customer WHERE custID=?', (custID,))
    con.commit()
    return data


def addCustomer( name, task, price):
    con = sqlite3.connect('customer.db')
    cursor = con.cursor()
    cursor.execute('insert into customer(name,task,price) values (?,?,?)',
                   (name, task, price))
    con.commit()
    con.close()


def showAllCustomer():
    con = sqlite3.connect('customer.db')
    cursor = con.cursor()
    data = cursor.execute('select * from customer')
    con.commit()
    return data

def showAllCustomerID():
    con = sqlite3.connect('customer.db')
    cursor = con.cursor()
    data = cursor.execute('select custID from customer')
    con.commit()
    return data


def deleteCustomers():
    con = sqlite3.connect('customer.db')
    cursor = con.cursor()
    cursor.execute(f'delete from customer ')
    con.commit()
    con.close()


def logintable():
    con = sqlite3.connect('login.db')
    cursor = con.cursor()
    cursor.execute("""  create table IF NOT EXISTS login(
            username TEXT PRIMARY KEY NOT NULL,
            password TEXT NOT NULL
            ) """)
    con.commit()
    con.close()


def addUser(username, password):
    con = sqlite3.connect('login.db')
    cursor = con.cursor()
    cursor.execute('insert into login values(?,?)', (username, password))
    con.commit()
    con.close()


def showAllUsers():
    con = sqlite3.connect('login.db')
    cursor = con.cursor()
    data = cursor.execute('select * from login')
    con.commit()
    return
    
