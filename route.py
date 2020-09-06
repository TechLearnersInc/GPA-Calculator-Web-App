import json
import random
from flask import render_template, jsonify, request, session
from app import app, db
from models import GPA_HISTORY


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
        pass
        tmp = random.randint(1, 1000000)
        data = GPA_HISTORY(id=tmp, scale=4.00, gpa=3.2)
        session["id"] = tmp
        print(tmp)
        print(session["id"])
        db.session.add(data)
    db.session.commit()
    print(json.dumps(formData, indent=4))

    return jsonify(
        {"GPA": 3.5}
    )
