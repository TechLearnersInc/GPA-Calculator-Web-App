from flask import render_template, url_for, jsonify, request
from sqlalchemy import MetaData, create_engine, Table
from sqlalchemy.sql.expression import insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import json
import random
from base26 import *


from app import app, db

# metadata = MetaData()
# engine = create_engine('mysql+pymysql://inan@techlearners:HelloWorld12345@'
#                        'techlearners.mysql.database.azure.com/gpacalculator', pool_pre_ping=True)

# engine = create_engine('mysql+pymysql://inan:12345@'
#                        'localhost/gpacalculator', pool_pre_ping=True)
# Session = sessionmaker(bind=engine)
# session = Session()


@app.route('/')
@app.route('/index')
def index():
    # metadata.reflect(bind=engine)

    # print(metadata.reflect(bind=engine))
    # print(metadata.tables.keys())
    # GPA_HISTORY = metadata.tables["gpa_history"]
    return render_template("index.html.jinja2")


@app.route('/calculate', methods=["POST"])
def calculate():
    # User Grades Input Form Data
    formData = request.form.to_dict()

    # validate form data (what happens when form data not correctly fetched)
    if formData:

        # user_id = Base26Converter().encode(counter)
        pass
    # metadata.reflect(bind=engine)

    # Base 26 To Calculate Hash For User ID

    # Create Database Session
    # Session = scoped_session(sessionmaker(bind=engine))
    session = db.Session()

    # Add items to gpa_history table
    # GPA_HISTORY = Table('gpa_history', metadata, autoload=True, autoload_with=engine)
    ins_user_gpa = db.GPA_HISTORY.insert().values(id=random.randint(100, 10000), scale=4.00, gpa=2.5)
    # Add items to grading history table
    # GRADING_SYSTEM = Table('grading_system', metadata, autoload=True, autoload_with=engine)

    db.session.execute(ins_user_gpa)
    db.session.commit()
    print(json.dumps(formData, indent=4))

    return jsonify(
        {"GPA": 3.5}
    )
