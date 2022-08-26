from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')
    # return "hello world"

@app.route("/boring")
def boring():
    return "<p>This is so boring!</p>"