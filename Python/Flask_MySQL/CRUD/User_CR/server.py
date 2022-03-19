from flask import Flask, render_template, request, redirect
# import the class from friend.py
from users import User
app = Flask(__name__)


@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users_info = User.get_all()
    print(users_info)
    return render_template("read.html", users_info=users_info)

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users_info = User.get_all()
    print(users_info)
    return render_template("read.html", users_info=users_info)

            
if __name__ == "__main__":
    app.run(debug=True)