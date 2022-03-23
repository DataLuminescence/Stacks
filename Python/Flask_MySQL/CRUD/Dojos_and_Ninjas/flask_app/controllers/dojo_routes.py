from flask import Flask, render_template, request, redirect
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja
from flask_app import app

# DISPLAY ROUTES ------------------------------------------

@app.route("/")
def index():
    # call the get all classmethod to get all dojos in the database
    get_all_dojos = Dojo.get_all()
    print(get_all_dojos)
    return render_template("create_dojo.html", get_all_dojos = get_all_dojos)

@app.route("/ninjas/create")
def new_user():
    return redirect("/")

@app.route("/dojos/create", methods = ["POST"])
def create_dojo():
    Dojo.create_new(request.form)
    return redirect("/")



# @app.route("/user/new")
# def new_user():
#     return render_template("create.html")

# @app.route("/user/show/<int:id>")
# def show_user(id):
#     # Id we requested from database is passed in as a dictionary
#     dict_of_user = {"id": id}
#     get_single_user = User.get_user(dict_of_user)
#     return render_template("/", get_single_user=get_single_user)    

# ACTION ROUTES ------------------------------------------



# @app.route("/user/edit/<int:id>")
# def edit_user(id):
#     dict_of_user = {"id": id}
#     get_single_user = User.get_user(dict_of_user)
#     return render_template("edit.html", get_single_user=get_single_user)

# @app.route("/user/update/<int:id>", methods=['POST'])
# def update_user(id):
#     dict_of_user = {
#         "id": id,
#         "first_name": request.form["first_name"],
#         "last_name": request.form["last_name"],
#         "email": request.form["email"]
#         }
#     User.update_user(dict_of_user)
#     return redirect(f"/user/show/{id}")

# @app.route("/user/delete/<int:id>")
# def delete_user(id):
#     dict_of_user = {"id": id}
#     User.delete_user(dict_of_user)
#     return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)