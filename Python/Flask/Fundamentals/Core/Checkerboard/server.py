import string
from flask import Flask, render_template #import flask and allow us to create our application
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", x=4, y=4, color1="", color2="")

@app.route('/4')
def half():
    return render_template("index.html", x=4, y=2, color1="", color2="")

@app.route('/<int:x>/<int:y>')
def dimensions(x,y):
    return render_template("index.html", x=int(x), y=int(y), color1="", color2="")

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def shade(x,y,color1,color2):
    return render_template("index.html", x=int(x), y=int(y), color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)