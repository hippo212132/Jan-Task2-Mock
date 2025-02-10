#Create Virtual Enviroment (VenV) within requirements file, CTRL + SHift + P.
#Add libraries to file and download them.

from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session

import db



app = Flask(__name__)


app.config["SESSION_TYPE"] = (
    "filesystem"
)

Session(app)

@app.route("/")
def index():

    if not session.get("user"):
        return render_template("index.html")
    
    return render_template("index.html", user=session["user"])

    #Checking if a session is avaliable it will pass for now.
    #Eventually it will skip login if a session is found.

    
    #If No session was found, you would be redirected to signup Page




@app.route("/logout")
def logout():
    if 'user' in session:
        session.clear()
    return redirect("/")
    
         


@app.route("/signup", methods = ["GET", "POST"])
def signup():
    
    if session.get("user"):
        return render_template("index.html", user=session["user"])
    

    if request.method == "POST":

        type = "vip_user"

        Email = request.form.get("Email")
        if len(Email) <= 0 or "@" not in Email:
            return render_template("signup.html", error="Please Enter a valid email address")
       
        Username = request.form.get("Username")
        if len(Username) <= 0:
            return render_template("signup.html", error="Please Ener a Username")
        
        Password = request.form.get("Password")
        if len(Password) <=0:
            return render_template("signup.html", error="Please Enter a password")
        
        cpass = request.form.get("cpass")
        if Password != cpass:
            return render_template("signup.html", error="Confirm Password should match password")
        
        Phone = request.form.get("Phone")
        if len(Phone) < 11 or "07" not in Phone:
            return render_template("signup.html", error="Please Enter a valid phone Number")

        user = db.create_user(type, Email, Username, Password, Phone)

        session["user"] = user

        return render_template("login.html")
    else:
        return render_template("signup.html")

@app.route("/login", methods = ["GET", "POST"])
def login():

    if not session.get("user"):
        return render_template("login.html")
 

    if request.method == "POST":


        email = request.form.get("email")
        password = request.form.get("password")

        user = db.check_user(email, password)

        session["user"] = user

        return render_template("index.html", user=session["user"])
        
    return render_template("login.html", error="Not a valid user")


@app.route("/tickets", methods = ["GET", "POST"])
def tickets():

    
    if request.method == "POST":

        
        
        TICKET_PRICE = 15.99
        VIP_TICKET_PRICE = 24.99

        qty = request.form.get("QTY")
        
        
        
        total = float(VIP_TICKET_PRICE) * float(qty)
        return render_template("Tickets.html", total = total)
    return render_template("Tickets.html")
    
@app.route("/about") 
def about():
    return render_template("about.html") 

@app.route("/contact")
def contact():
    return render_template("contact.html")
# main
if __name__ == "__main__":
    app.run(debug=True)

