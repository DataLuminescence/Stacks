import string
from flask import Flask, render_template #import flask and allow us to create our application
app = Flask(__name__)



@app.route('/')
def index():
    userlist = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
    return render_template("index.html", userlist=userlist)



# @app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
# def shade(x,y,color1,color2):
#     return render_template("index.html", x=int(x), y=int(y), color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)