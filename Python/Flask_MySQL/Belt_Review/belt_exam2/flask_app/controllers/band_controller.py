from flask import Flask, render_template, redirect, session, request, flash
from flask_app.models.band import Band
from flask_app.models.user import User
from flask_app import app

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)  

#------------------------------------------------------------------------------
# GO TO NEW BAND PAGE - DISPLAY
#------------------------------------------------------------------------------

# routes user to band creation area
@app.route("/band/new")
def new_band():

    # validate user is logged in to enter this page
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id" : session["user_id"]
    }

    #
    user = User.get_by_user_id(data)

    return render_template("band_new.html", user = user)

#------------------------------------------------------------------------------
# EDIT BAND - DISPLAY
#------------------------------------------------------------------------------

# takes user to band edit area
@app.route("/band/edit/<int:id>")
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

    # get band by id we dont care about user EDIT 
    one_band = Band.get_user_and_band_by_band_id(band_data) #List of dictionaries
    print(one_band)

    # EDIT do it the right way
    return render_template("band_edit.html", user = user, one_band = one_band)

#------------------------------------------------------------------------------
# VIEW BAND - DISPLAY
#------------------------------------------------------------------------------

# takes user to band edit area
@app.route("/band/mybands")
def view_band(): # change name EDIT
    
    # validate user is logged in to enter this page
    if "user_id" not in session:
        return redirect("/")
    
    user_data = {
        "id" : session["user_id"]
    }

    # user = User.get_by_user_id(user_data)
    user_bands = User.get_band_of_user(user_data) #one band not appropriate name EDIT

    return render_template("user_band_view.html", user_bands = user_bands)

#------------------------------------------------------------------------------
# CREATE BAND - ACTION
#------------------------------------------------------------------------------

# creates band after validation, and obtaining data from forms
@app.route("/band/register", methods=['POST'])
def band_register():

    # validate user is logged in to enter this page
    if "user_id" not in session:
        return redirect("/")
    
    # if band submitted registration info is invalid return user to home and 
    # display a message of where they made a mistake
    if not Band.validate_register(request.form):
        return redirect("/band/new")
    
    # create a dictionary from data collected from form
    query_data = {
        "user_id" : session["user_id"],
        "band_name" : request.form["band_name"],
        "genre" : request.form["genre"],
        "homecity" : request.form["homecity"]
    }

    # insert dictionary data into create_band class method in order to populate 
    # fields needed to insert new user into database
    Band.create_band(query_data) 

    # redirect elsewhere
    return redirect("/dashboard")


#------------------------------------------------------------------------------
# UPDATE BAND - ACTION
#------------------------------------------------------------------------------

@app.route("/band/update/<int:id>", methods=['POST'])
def upate_band(id):
    # validate user is logged in to enter this page
    if "user_id" not in session:
        return redirect("/")
    
    query_data = {
        "id": id,
        "user_id" : session["user_id"],
        "band_name" : request.form["band_name"],
        "genre" : request.form["genre"],
        "homecity" : request.form["homecity"]
    }
    
    Band.update_band_by_band_id(query_data)

    return redirect("/dashboard")

#------------------------------------------------------------------------------
# DELETE BAND - ACTION
#------------------------------------------------------------------------------

# deletes a band based on the id of the band selected in dashboard
@app.route("/band/delete/<int:id>")
def delete_band(id):
    
    # validate user is logged in to enter this page
    if "user_id" not in session:
        return redirect("/")
    data = {"id": id}
    Band.delete_band(data)
    return redirect("/dashboard")

