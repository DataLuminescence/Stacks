from flask import Flask, render_template, redirect, session, request, flash
from flask_app.models.band import Band
from flask_app.models.user import User
from flask_app import app

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)  

#------------------------------------------------------------------------------
# NEW SIGHTING - Band creation area
#------------------------------------------------------------------------------

@app.route("/new/sighting") 
def band_new():
    # validate user is logged in to enter this page
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id" : session["user_id"]
    }

    user = User.get_by_user_id(data)

    return render_template("band_new.html", user = user)

#------------------------------------------------------------------------------
# CREATE BAND
#------------------------------------------------------------------------------

# actually creates band after validation, and obtaining data from forms
@app.route("/register_band", methods=['POST'])
def register_band():

    # if band submitted registration info is invalid return user to home and 
    # display a message of where they made a mistake
    if not Band.validate_register(request.form):
        return redirect("/new/sighting")
    
    # create a dictionary from data collected from form
    query_data = {
        "user_id" : session["user_id"],
        "band_name" : request.form["band_name"],
        "genre" : request.form["genre"],
        "homecity" : request.form["homecity"],
    }

    # insert dictionary data into create_band class method in order to populate 
    # fields needed to insert new user into database. Also returns new user id
    new_band_id = Band.create_band(query_data) 

    # store user id into session
    # session["user_id"] = new_band_id #Why cant we use this to use the user id?

    # redirect elsewhere
    return redirect("/dashboard")

#------------------------------------------------------------------------------
# EDIT BAND - ACTION
#------------------------------------------------------------------------------

# takes user to band edit area
@app.route("/edit/<int:id>")
def edit_band(id):

    # validate user is logged in to enter this page
    if "user_id" not in session:
        return redirect("/")

    user_data = {
        "id" : session["user_id"]
    }

    band_data = {
        "id" : id
    }
    
    user = User.get_by_user_id(user_data)
    print(user)

    one_band = Band.get_user_and_band_by_band_id(band_data) #List of dictionaries
    print(one_band)

    return render_template("band_edit.html", user = user, one_band = one_band)

#------------------------------------------------------------------------------
# VIEW BAND - DISPLAY
#------------------------------------------------------------------------------

# takes user to band edit area
@app.route("/mybands")
def view_band():
    # validate user is logged in to enter this page
    if "user_id" not in session:
        return redirect("/")
    
    user_data = {
        "id" : session["user_id"]
    }

    user = User.get_by_user_id(user_data)
    one_band = Band.get_user_and_band_by_user_id(user_data)
    print(one_band)
    return render_template("user_band_view.html", user = user, one_band = one_band)

#------------------------------------------------------------------------------
# DELETE BAND - ACTION
#------------------------------------------------------------------------------

# deletes a band based on the id of the band selected in dashboard
@app.route("/delete_band/<int:id>")
def delete_band(id):
    # validate user is logged in to enter this page
    if "user_id" not in session:
        return redirect("/")
    data = {"id": id}
    Band.delete_band(data)
    return redirect("/dashboard")

