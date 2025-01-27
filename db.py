import sqlite3, hashlib
from user import user

connection = sqlite3.connect("Riget Zoo.db", check_same_thread=False)

#Establishing Connection to Database

cur = connection.cursor()



def create_user(type, email, Username, Password, phone):

    cur.execute("INSERT INTO USERS (type, email, Username, Password, phone) VALUES (?,?,?,?,?)",
                 (type, email, Username, Password, phone))
    connection.commit()

    id = cur.lastrowid

    return user(id, type, email, Username, Password, phone)

#This function allows me to use the frontend forms inputs as part of the SQL statement to add it to the database.
#THis Function will be used to add a user to a database


def check_email(email):
    
 pass
