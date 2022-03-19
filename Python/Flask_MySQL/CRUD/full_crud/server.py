from crypt import methods
from dataclasses import dataclass
from Python.Flask_MySQL.CRUD.full_crud.dog import Dog
from flask import Flask, render_template, request, redirect, session  #import flask and allow us to create our application
app = Flask(__name__)

app.secret_key = "asdfghjkl"

# DISPLAY ROUTES ------------------------------

@app.route('/')
def index():
    mysql = connectToMySQL("dogs_db")
    dogs = mysql.query_db("SELECT * FROM dogs;")
    print(dogs)
    return render_template("index.html", all_dogs = dogs)

@app.route('/dogs/new')
def new_dog():
    return redirect('add_dog.html')

@app.route('/dogs/<int:id>')
def show_dog(id):
    data = { "id": id}
    dog = Dog.get_one(data)
    return redirect('add_dog.html')    

@app.route('/dogs/edit/<int:id>')
def edit_dog(id):
    dog = Dog.get_one( {"id": id})
    return render_template("edit_dog.html", dog = dog) 


# ACTION ROUTES ------------------------------


@app.route('/dogs/create', methods = ["POST"])
def create_dog():
    Dog.create_dog(request.form)
    return redirect("/")

@app.route('/dogs/update', methods = ["POST"])
def update_dog():
    Dog.create_dog(request.form)
    return redirect("/")    

@app.route('/dogs/<int:id>/delete')
def delete_dog(id):
    Dog.delete_dog({"id":id})
    return redirect("/")


if __name__=="__main__":
    app.run(debug=True)