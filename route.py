import json

from flask import render_template, jsonify, request, Response
from Database.database_models import GPA_HISTORY, FEEDBACK
from app import app, db, cache
from modules import calculate_gpa
from modules.data_preprocessing import DataPreProcessingGPA


@app.route('/')
@app.route('/index')
@cache.memoize()
def index():
    return render_template("index.html.jinja2")


@app.route('/calculate', methods=["POST"])
def calculate():
    # User Grades Input Form Data
    formData = request.form.to_dict()

    # Validate form data (what happens when form data not correctly fetched)
    if formData:
        try:
            data_list = DataPreProcessingGPA(formData).clean_data()
            if data_list == -1:
                return Response(status=404)
                # return jsonify({"GPA": -1})  # Error Page
            gpa = calculate_gpa.calculate(data_list[1], data_list[0])
            if gpa == - 1:
                return Response(status=404)
                # return jsonify({"GPA": -1})  # Error Page
            scale_value_list = list(data_list[0].values())
            scale = max(scale_value_list)
            grade_sheet = data_list[0]
            try:
                # noinspection PyArgumentList
                user_gpa_history = GPA_HISTORY(scale=float(scale), gpa=float(gpa), grade_sheet=json.dumps(grade_sheet))
                db.session.add(user_gpa_history)
                db.session.commit()
            except Exception as e:
                print(e)
                return Response(status=404)
                # return jsonify({"GPA": -1})

            return jsonify({"GPA": gpa})
        except (DeprecationWarning, ConnectionAbortedError, ConnectionError, ConnectionRefusedError) as e:
            print(e)
            return Response(status=404)
            # return jsonify({"GPA": -1})  # Error Page
    else:
        return Response(status=404)
        # return jsonify({"GPA": -1})  # Error Page


@app.route('/feedback', methods=["POST"])
def feedback():
    formData = request.form.to_dict()
    if formData:
        try:
            # noinspection PyArgumentList
            user_feedback = FEEDBACK(feed_back=formData["feedback"])
            db.session.add(user_feedback)
            db.session.commit()
            return jsonify({"STATUS": "OK"})
        except Exception as e:
            print(e)
            return Response(status=404)
            # return jsonify({"STATUS": "ERROR"})
    else:
        return jsonify({"STATUS": "NO DATA"})
