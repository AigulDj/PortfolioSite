import datetime

import flask
from flask import Flask, redirect, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from typing import Callable


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admin.db'
app.config['SECRET_KEY'] = 'adminkey'

Bootstrap(app)


class MySQLAlchemy(SQLAlchemy):
    Column: Callable
    Integer: Callable
    String: Callable


db = MySQLAlchemy(app)

admin = Admin(app)


class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))


admin.add_view(ModelView(Owner, db.session))

db.create_all()

dat = datetime.datetime.now()
year = dat.year


@app.route("/")
def home():
    return render_template("index.html", year=year)


@app.route("/admin")
def admin():
    return render_template("admin.html")


if __name__ == "__main__":
    app.run(debug=True)
