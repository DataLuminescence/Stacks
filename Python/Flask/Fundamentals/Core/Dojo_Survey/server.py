from flask import Flask, render_template, request, redirect, session  #import flask and allow us to create our application
app = Flask(__name__)
app.secret_key = "asdfghjkl"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    form = {
                'name': request.form['name'],
                'location': request.form['location'],
                'language': request.form['language'],
                'comment': request.form['comment'],
            }
    session['form'] = form
    return redirect('/result/')

@app.route('/result/')
def counter():
    return render_template("results.html")

@app.route('/destroy_session/')
def clear():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)