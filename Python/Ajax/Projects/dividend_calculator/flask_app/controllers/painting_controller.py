from flask import Flask, render_template, redirect, session, request, flash
# from flask_app.models.band import Painting
from flask_app.models.user import User
from flask_app.models.painting import Painting
from flask_app import app

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)  

#------------------------------------------------------------------------------
# NEW PAINTING PAGE - DISPLAY
#------------------------------------------------------------------------------

# routes user to painting creation area
@app.route("/paintings/new")
def new_painting():

    # validate user is logged in to enter this page
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id" : session["user_id"]
    }

    # get user data based on id
    user = User.get_user_by_id(data)

    return render_template("painting_new.html", user = user)

#------------------------------------------------------------------------------
# CREATE PAINTING - ACTION
#------------------------------------------------------------------------------

# creates painting after validation, and obtaining data from forms
@app.route("/paintings/register", methods=['POST'])
def painting_register():

    # validate user is logged in to enter this page
    if "user_id" not in session:
        return redirect("/")
    
    # if painting submitted registration info is invalid return user to home and 
    # display a message of where they made a mistake
    if not Painting.validate_register(request.form):
        return redirect("/paintings/new")
    
    # create a dictionary from data collected from form
    query_data = {
        "user_id" : session["user_id"],
        "title" : request.form["title"],
        "description" : request.form["description"],
        "price" : request.form["price"]
    }

    # insert dictionary data into create_painting class method in order to populate 
    # fields needed to insert new painting into database
    Painting.create_painting(query_data) 

    # redirect to dashboard
    return redirect("/paintings")


#------------------------------------------------------------------------------
# VIEW PAINTING - DISPLAY - in user controller
#------------------------------------------------------------------------------

@app.route("/paintings/<int:id>")
def view_painting(id):
    # validate user is logged in to enter this page
    if "user_id" not in session:
        return redirect("/")
    data = {"id": id}

    painting_list = Painting.get_painting_by_id(data) #EDIT

    return render_template("user_painting_view.html", painting_list = painting_list)

#------------------------------------------------------------------------------
# DELETE PAINTING - ACTION
#------------------------------------------------------------------------------

# deletes a band based on the id of the band selected in dashboard
@app.route("/paintings/delete/<int:id>")
def delete_painting(id):
    
    # validate user is logged in to enter this page
    if "user_id" not in session:
        return redirect("/")
    data = {"id": id}
    Painting.delete_painting(data)
    return redirect("/paintings")

#------------------------------------------------------------------------------
# EDIT PAINTING - DISPLAY
#------------------------------------------------------------------------------

@app.route("/paintings/<int:id>/edit")
def edit_painting(id):

    if "user_id" not in session:
        return redirect("/")
    
    painting_data = {
        "id" : id
    }
    painting_list = Painting.get_painting_by_id(painting_data)

    return render_template("painting_edit.html", painting_list = painting_list)

#------------------------------------------------------------------------------
# UPDATE PAINTING - ACTION
#------------------------------------------------------------------------------

@app.route("/paintings/update/<int:id>", methods=['POST'])
def upate_painting(id):
    # validate user is logged in to enter this page
    if "user_id" not in session:
        return redirect("/")

    query_data = {
        "id": id,
        "title" : request.form["title"],
        "description" : request.form["description"],
        "price" : request.form["price"]
    }
    
    Painting.update_painting_by_id(query_data)

    return redirect("/paintings")

#------------------------------------------------------------------------------
# END
#------------------------------------------------------------------------------
