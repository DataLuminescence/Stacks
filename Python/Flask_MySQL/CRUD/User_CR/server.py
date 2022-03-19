from flask import Flask, render_template, request, redirect
# import the class from friend.py
from users import User

app = Flask(__name__)

# DISPLAY ROUTES ------------------------------------------

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users_info = User.get_all()
    print(users_info)
    return render_template("read.html", users_info=users_info)

@app.route("/user/new")
def new_user():
    return render_template("create.html")

# ACTION ROUTES ------------------------------------------


@app.route("/user/create", methods = ["POST"])
def create_user():
    User.create_user(request.form)
    return redirect("/")

# @app.route("/user/<int:id>")
# def show_user(id):
#     pass

# @app.route("/user/edit/<int:id>")
# def edit_user(id):
#     pass




if __name__ == "__main__":
    app.run(debug=True)