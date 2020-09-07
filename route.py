import json
import random
from flask import render_template, jsonify, request, session
from app import app, db
from modules.data_preprocessing import *
from Database.database_models import *
from modules import calculate_gpa


@app.route('/')
@app.route('/index')
def index():
    try:
        if session["id"]:
            print(session["id"])
    except KeyError:
        pass
    return render_template("index.html.jinja2")


@app.route('/calculate', methods=["POST"])
def calculate():
    # User Grades Input Form Data
    formData = request.form.to_dict()

    # validate form data (what happens when form data not correctly fetched)
    if formData:
        try:
            data_list = DataPreProcessingGPA(formData).clean_data()
            # if data_list == -1:
            #     return "ERROR"
            gpa = calculate_gpa.calculate(data_list[1], data_list[0])
            # if gpa == - 1:
            #     return "ERROR"
            scale_value_list = list(data_list[0].values())
            scale = max(scale_value_list)
            try:
                user_gpa_history = GPA_HISTORY(scale=float(scale), gpa=float(gpa), grade_sheet=str(grade_sheet))
                db.session.add(user_gpa_history)
                db.session.commit()
            except:
                pass #return "ERROR"
            
            return jsonify(
                {"GPA": gpa})
        except (DeprecationWarning, ConnectionAbortedError, ConnectionError, ConnectionRefusedError):
            return jsonify(
                {"GPA": -1})
    else:
        return jsonify({"GPA": -1})
