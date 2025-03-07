from flask import Flask, render_template, request
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)