from flask import Flask, render_template #import flask and allow us to create our application
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/play')
def play():
    return render_template("index.html", number=3)

@app.route('/play/<int:box_num>')
def play_number(box_num):
    return render_template("index.html", number=box_num, color='#9fc5f8' )

@app.route('/play/<int:box_num>/<box_color>')
def play_number_color(box_num, box_color):
    return render_template("index.html", number=box_num, color=box_color)

if __name__=="__main__":
    app.run(debug=True)