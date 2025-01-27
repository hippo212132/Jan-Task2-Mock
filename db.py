import sqlite3, hashlib
from user import user

connection = sqlite3.connect("Riget Zoo.db", check_same_thread=False)

#Establishing Connection to Database

cur = connection.cursor()

def hash(phrase): #This is a function used to hash a new password
 
    object = hashlib.md5(phrase.encode())
    object = object.hexdigest()
 
    return object


def create_user(type, email, Username, Password, phone):

    Password = hash(Password)

    cur.execute("INSERT INTO USERS (type, email, Username, Password, phone) VALUES (?,?,?,?,?)", (type, email, Username, Password, phone))
    connection.commit()

    id = cur.lastrowid

    return user(id, type, email, Username, Password, phone)

#This function allows me to use the frontend forms inputs as part of the SQL statement to add it to the database.
#THis Function will be used to add a user to a database


def check_email(email):
    
 cur.execute("SELECT * FROM USERS WHERE Email = ?", (email))

 return cur.fetchone

def check_user(email, password):

    password = hash(password)

    cur.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password,))

    

    return cur.fetchone()
