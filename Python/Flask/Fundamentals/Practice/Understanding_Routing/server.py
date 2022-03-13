from ast import IsNot
import string
from flask import Flask #import flask and allow us to create our application
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/dojo")
def dojo():
    return "Dojo!"

#/say/hello
@app.route('/say/<string:name>')
def say(name):
    return f"Hi, {str(name)}!" #Is  str() redundant here?

#/repeat/36/hello
@app.route('/repeat/<greeting>/<int:number>')
def repeat(greeting, number): 
    output = ""
    for i in range(0, number):
        output += f"<p>{greeting}</p>"
    return output

if __name__=="__main__":
    app.run(debug=True)