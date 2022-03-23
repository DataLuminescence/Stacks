from flask import Flask, render_template, request, redirect
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask_app import app


# DISPLAY ROUTES ---------------------------------------------------------------


# Home route that runs at start of program
@app.route("/")
def index():
    return redirect("/dojos")

# Loads page that allows to create a dojo and displays current dojos. Liks to edit dojos or add new ninja
@app.route("/dojos")
def dojos():
    # call the get all classmethod to get all dojos in the database
    get_all_dojos = Dojo.get_all()
    # For debug purposes
    for dict in get_all_dojos: 
        print(dict.id, dict.name)
    return render_template("dojos.html", get_all_dojos = get_all_dojos)

# Loads Dojo Show page. Obtain ID of dojo to be displayed when ninja is created.
@app.route("/dojos/dojo_show/<int:id>")
def load_dojo_show(id):
    
    # Create a dictionary for the dojo id which corresponds to the newly created ninja
    ninjas_data = {
        'dojo_id' : id
    }

    # Merge the dojo and ninja data to be displayed in the ninjas_in_dojos route
    ninjas_in_dojos = Dojo.join_dojos_and_ninjas(ninjas_data)
    return render_template("ninjas_in_dojos.html", ninjas_in_dojos = ninjas_in_dojos)


# ACTION ROUTES -------------------------------------------------------------------


# Creates new dojo based on user input name
@app.route("/dojos/create_dojo", methods = ["POST"])
def create_dojo():
    Dojo.create_new(request.form)
    return redirect("/dojos")

if __name__ == "__main__":
    app.run(debug=True)