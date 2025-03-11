from flask import render_template
from models import db
from __init__ import create_app

app = create_app()

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/home")
def home():
    return render_template("main.html")

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)
