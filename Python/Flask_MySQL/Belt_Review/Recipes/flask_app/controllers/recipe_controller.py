from flask import Flask, render_template, redirect, session, request, flash
from flask_app.models.recipe import Recipe
from flask_app.models.user import User
from flask_app import app

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)  


#------------------------------------------------------------------------------
# 
#------------------------------------------------------------------------------

@app.route("/recipe/edit/<int:id>") # "/recipe/edit/<int:id>"
def recipe_edit():
    return render_template("recipe_edit.html")

@app.route("/recipe_delete/<int:id>")
def recipe_delete():
    return redirect("/dashboard")

#------------------------------------------------------------------------------
# NEW RECIPE 
#------------------------------------------------------------------------------

@app.route("/recipe/new") # "/recipe/new"
def recipe_new():
    # validate user is logged in to enter this page
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id" : session["user_id"]
    }

    user = User.get_by_user_id(data)

    return render_template("recipe_new.html", user = user)


@app.route("/recipe/<int:id>") # "/recipe/<int:id>"
def recipe_info():
    # validate user is logged in to enter this page
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id" : session["user_id"]
    }

    user = User.get_by_user_id(data)
    return render_template("recipe_view.html", user = user)