from flask import Flask, render_template, request, redirect
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask_app import app


# DISPLAY ROUTES ---------------------------------------------------------------

# Loads New Ninja page where user can create a new ninja
@app.route("/dojos/new_ninja")
def load_new_ninja():
    get_all_dojos = Dojo.get_all()
    get_all_ninjas = Ninja.get_all() # Does this do anything?
    return render_template("ninjas.html", get_all_dojos = get_all_dojos)


# ACTION ROUTES -------------------------------------------------------------------

# Creates ninja in new ninja page. Calls dojo_show route to show ninjas in user selected dojo
@app.route("/dojos/create_ninja", methods = ["POST"]) 
def create_ninja():
    # Takes newly created ninja attributes via request form
    Ninja.create_ninja(request.form)
    # Returns dojo id by accessing dojo_id in request.form
    return redirect(f"/dojos/dojo_show/{request.form['dojo_id']}")

if __name__ == "__main__":
    app.run(debug=True)