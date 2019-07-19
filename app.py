from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)






@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/gospel')
def gospel():
    return render_template("gospel.html")

@app.route('/highlife')
def highlife():
    return render_template("highlife.html")

@app.route('/hiplife')
def hiplife():
    return render_template("hiplife.html")

@app.route('/raggae')
def raggae():
    return render_template("raggae.html")


if __name__ == '__main__':
    app.run()
