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

        grades_credits_list, grade_sheet = DataPreProcessingGPA(formData).clean_data()
        gpa = calculate_gpa.calculate(grades_credits_list, grade_sheet)
        scale_value_list = list(grade_sheet.values())
        scale = max(scale_value_list)
        user_gpa_history = GPA_HISTORY(scale=float(scale), gpa=float(gpa), grade_sheet=str(grade_sheet))
        db.session.add(user_gpa_history)
        db.session.commit()
        return jsonify(
                {"GPA": gpa}
            )

    else:
        return jsonify({"GPA": -1})
