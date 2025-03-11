from flask import render_template
from models import db
from __init__ import create_app

app = create_app()

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, port='3000')