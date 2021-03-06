from flask import Flask, render_template, request, redirect
# import the class from Users.py
from users import User

app = Flask(__name__)

# DISPLAY ROUTES ------------------------------------------------------------------------------


@app.route("/")
def index():
    # Home route which displays all the users currently in the database

    
    get_all_user = User.get_all() # classmethod to put all users in database into a dictionary
    print(get_all_user)
    return render_template("read_all.html", get_all_user = get_all_user)


@app.route("/user/new")
def new_user():
    # Renders template where a new user will be created
    return render_template("create.html")


@app.route("/user/show/<int:id>")
def show_user(id):
    # Renders information of single user

    dict_of_user = {"id": id} # id we requested from database is passed in as a dictionary
    get_single_user = User.get_user(dict_of_user) # put single user from database into dictionary
    return render_template("read_one.html", get_single_user=get_single_user)    

# ACTION ROUTES ------------------------------------------------------------------------------

@app.route("/user/create", methods = ["POST"])
def create_user():
    User.create_user(request.form)
    test = User.get_recent_user()
    id = test["id"]
    return redirect(f"/user/show/{id}")

@app.route("/user/edit/<int:id>")
def edit_user(id):
    dict_of_user = {"id": id}
    get_single_user = User.get_user(dict_of_user)
    return render_template("edit.html", get_single_user=get_single_user)

@app.route("/user/update/<int:id>", methods=['POST'])
def update_user(id):
    dict_of_user = {
        "id": id,
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
        }
    User.update_user(dict_of_user)
    return redirect(f"/user/show/{id}")

@app.route("/user/delete/<int:id>")
def delete_user(id):
    dict_of_user = {"id": id}
    User.delete_user(dict_of_user)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)