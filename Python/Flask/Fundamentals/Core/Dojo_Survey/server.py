from flask import Flask, render_template, request, redirect, session  #import flask and allow us to create our application
app = Flask(__name__)
app.secret_key = "asdfghjkl"

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 1
    else:
        session['counter'] += 1
    return render_template("index.html", counter=session['counter'])

@app.route('/increment/')
def counter():
    session['counter'] += 1
    return redirect('/')

@app.route('/destroy_session/')
def clear():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)