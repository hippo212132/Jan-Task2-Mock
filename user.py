class user:
    def __init__(self, id, type, email, username, password, phone_number):
        self.id = id
        self.type = type
        self.email = email
        self.username = username
        self.password = password
        self.phone_number = phone_number

#Creating a general USER class which means anyone thats signed up to the database

class vip_user:
    def __init__(self, id, email, username, password, phone_number):
        super().__init__(id, "vip_user", email, username, password, phone_number)

#Creating a sub class which allows for different types of users such as a VIP user for example
