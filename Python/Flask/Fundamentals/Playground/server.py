from ast import IsNot
from pydoc import render_doc
import string
from flask import Flask, render_template #import flask and allow us to create our application
app = Flask(__name__)



#/repeat/36/hello
@app.route('/repeat/<int:number>/<greeting>')
def repeat(number, greeting): 
    output = ""
    return output


#Rendering our first HTML page with flask
@app.route("/index")
def index():
    #pass in the name of the html file and any variables that we plan to use on that page
    return render_template("index.html", my_string="hello", times = 5)

@app.route("/lists")
def lists():
    student_list = [
        {"name":"max", "id": "7"}
        {"name":"chris", "id": "1"}
        {"name":"amanda", "id": "3"}
        # {"name":"hiago", "id": "21"}
    ]
    return render_template("list.html", students = student_list)


if __name__=="__main__":
    app.run(debug=True)