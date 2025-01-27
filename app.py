#Create Virtual Enviroment (VenV) within requirements file, CTRL + SHift + P.
#Add libraries to file and download them.

from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
from flask_login import login_manager, login_required, logout_user
import db



app = Flask(__name__)


app.config["SESSION_TYPE"] = (
    "filesystem"
)

Session(app)

@app.route("/")
def index():

    if session.get("user"):
        pass

    #Checking if a session is avaliable it will pass for now.
    #Eventually it will skip login if a session is found.

    return redirect("/signup")
    #If No session was found, you would be redirected to signup Page


@app.route("/signup", methods = ["GET", "POST"])
def signup():
    
    if session.get("user"):
        pass
    

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
        
        Phone = request.form.get("Phone")
        if len(Phone) < 11 or "07" not in Phone:
            return render_template("signup.html", error="Please Enter a valid phone Number")

        user = db.create_user(type, Email, Username, Password, Phone)

        session["user"] = user

        return render_template("index.html")
    else:
        return render_template("signup.html")


# main
if __name__ == "__main__":
    app.run(debug=True)

