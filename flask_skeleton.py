import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
from flask import render_template

#################################################
# Database Setup
#################################################
engine = engine = create_engine('postgresql://postgres:postgres@localhost:5432/Project_2_TLLDL')

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Encounter = Base.classes.fatal_encounter
States = Base.classes.states
Ages = Base.classes.age
Years = Base.classes.years
Genders = Base.classes.gender
Cause = Base.classes.cause_death
Illness = Base.classes.mental_illness
Race = Base.classes.race
Population = Base.classes.population


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    
    return render_template("index.html")


@app.route("/data")
def names():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    
    results = session.query(Encounter.State, Encounter.Age, Encounter.Gender, Encounter.Race, Encounter.Year, Encounter.Mental_Illness, Encounter.Cause_of_Death, Encounter.Latitude, Encounter.Longitude).all()
    session.close()

    # Convert list of tuples into normal list
    fatal_encounter = []
    for state, age, gender, race, year, illness, cause, lat, lon in results:
        encounter_dict={}
        encounter_dict["state"]= state
        encounter_dict["age"]= age
        encounter_dict["gender"]= gender
        encounter_dict["race"]= race
        encounter_dict["year"]= year
        encounter_dict["illness"]= illness
        encounter_dict["cause_of_death"]= cause
        encounter_dict["lat"] = lat
        encounter_dict["lon"] = lon
        all_encounters.append(encounter_dict)


    return jsonify(all_encounters)

@app.route("/states")
def count():
    session = Session(engine)

    results = session.query(States.State, States.counts) #, Encounter.Age, Encounter.Gender, Encounter.Race, Encounter.Year, Encounter.Mental_Illness, Encounter.Latitude, Encounter.Longitude).all()
    session.close()

    all_states = []
    for state, count in results:
        state_dict={}
        state_dict["state"] = state
        state_dict["count"] = count
        all_states.append(state_dict)

    return jsonify(all_states)

@app.route("/ages")
def age():
    session = Session(engine)

    results = session.query(Ages.Age, Ages.counts)
    session.close()

    all_ages = []
    for age, count in results:
        age_dict = {}
        age_dict["age"] = age
        age_dict["count"] = count
        all_ages.append(age_dict)

    return jsonify(all_ages)

@app.route("/years")
def year():
    session = Session(engine)

    results = session.query(Years.Year, Years.counts)
    session.close()

    all_years = []
    for year, count in results:
        year_dict = {}
        year_dict["year"] = year
        year_dict["count"] = count
        all_years.append(year_dict)

    return jsonify(all_years)

@app.route("/illness")
def illnesses():
    session = Session(engine)

    results = session.query(Illness.Mental_Illness, Illness.counts)
    session.close()

    all_illnesses = []
    for illness, count in results:
        illness_dict = {}
        illness_dict["mental_illness"] = illness
        illness_dict["count"] = count
        all_illnesses.append(illness_dict)

    return jsonify(all_illnesses)

@app.route("/causeDeath")
def cause():
    session = Session(engine)

    results = session.query(Cause.Cause_of_Death, Cause.counts)
    session.close()

    all_causes = []
    for cause, count in results:
        cause_dict = {}
        cause_dict["cause"] = cause
        cause_dict["count"] = count
        all_causes.append(cause_dict)

    return jsonify(all_causes)

@app.route("/gender")
def genders():
    session = Session(engine)

    results = session.query(Genders.Gender, Genders.counts)
    session.close()

    all_genders = []
    for gender, count in results:
        gender_dict = {}
        gender_dict["gender"] = gender
        gender_dict["count"] = count
        all_genders.append(gender_dict)

    return jsonify(all_genders)

@app.route("/race")
def race():
    session = Session(engine)

    results = session.query(Race.Race, Race.count)
    session.close()

    all_races = []
    for race, count in results:
        race_dict = {}
        race_dict["race"] = race
        race_dict["count"] = count
        all_races.append(race_dict)

    return jsonify(all_races)

@app.route("/population")
def population():
    session = Session(engine)

    results = session.query(Population.Race, Population.Percent)
    session.close()

    all_pops = []
    for race, percent in results:
        pop_dict = {}
        pop_dict["race"] = race
        pop_dict["percent"] = percent
        all_pops.append(pop_dict)

    return jsonify(all_pops)
    

if __name__ == '__main__':
    app.run(debug=True)