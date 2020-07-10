import os
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

engine = create_engine("postgresql://postgres:postgres@localhost:5432/police_violence_db")
connection = engine.connect()

# app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:postgres@localhost:5432/police_violence_db"  # police_violence_db is the title of my Postgres database
# db = SQLAlchemy(app)

Base = automap_base()
Base.prepare(engine, reflect=True)

encounter = Base.classes.fatal_encounter

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data")
def data():

    # table = db.session.query(encounter).statement
    # df = pd.read_sql_query(table, db.session.bind)
    data = engine.execute("select row_to_json(fatal_encounter) from fatal_encounter")
    stuff={}
    for record in data:
        stuff['']

    return stuff

if __name__ == "__main__":
    app.run(debug=True)