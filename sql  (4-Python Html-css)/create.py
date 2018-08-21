# from __future__ import absolute_import
import os
from flask import Flask, render_template, request
from dbmodels import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():
    db.create_all()
    print("Crezione DB da modello eseguita")


if __name__ == "__main__":
    with app.app_context():
        main()
