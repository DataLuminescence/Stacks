from flask import render_template, redirect, session, request
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)  

from flask import flash
from flask_app.models.user import User

#------------------------------------------------------------------------------
# HOME ROUTES 
#------------------------------------------------------------------------------

# home route that runs at start of program
@app.route("/")
def index():
    # if the there is a user id in session redirect user to dashboard
    if "user_id" in session:
        return redirect("/dashboard")
    return render_template("index.html")

#------------------------------------------------------------------------------
# REGISTER ROUTES 
#------------------------------------------------------------------------------

# when register button is pressed on home page
@app.route("/register_user", methods=['POST'])
def register_user():

    # if user submitted registration info is invalid return user to home and 
    # display a message of where they made a mistake
    if not User.validate_register(request.form):
        return redirect("/")

    # convert password to bcrypt
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    
    # create a dictionary from data collected from form
    query_data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" : pw_hash
    }

    # insert dictionary data into create_user class method in order to populate 
    # fields needed to insert new user into database. Also returns new user id
    new_user_id = User.create_user(query_data)

    # store user id into session
    session["user_id"] = new_user_id #Why cant we use this to use the user id?

    # redirect elsewhere
    return redirect("/dashboard") 

#------------------------------------------------------------------------------
# LOGIN ROUTES 
#------------------------------------------------------------------------------

@app.route("/login_user", methods=['POST'])
def login_user():

    # if user submitted login info is invalid return user to home and 
    # display a message of where they made a mistake
    if not User.validate_login(request.form):
        return redirect("/")
    
    # create a dictionary from data collected from form
    query_data = {
        "email" : request.form["email"]
    }
    logged_in_user = User.get_by_email(query_data)
    
    if not logged_in_user:
        return redirect("/")

    # run query to database
    session["user_id"] = logged_in_user.id

    # redirect elsewhere
    return redirect("/dashboard") 

#------------------------------------------------------------------------------
# DASHBOARD ROUTES 
#------------------------------------------------------------------------------

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id" : session["user_id"]
    }
    user = User.get_by_user_id(data)
    return render_template("dashboard.html", user = user)

#------------------------------------------------------------------------------
# DASHBOARD ROUTES 
#------------------------------------------------------------------------------

# Logs user out of session by clearing the session, then redirects them to home
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")