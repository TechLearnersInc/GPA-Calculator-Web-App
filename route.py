from flask import render_template, url_for, jsonify, request
import json
from app import app


@app.route('/')
@app.route('/index')
def index():
    print(url_for('static', filename='img/icon_round.png'))
    return render_template("index.html.jinja2")


@app.route('/calculate', methods=["POST"])
def calculate():
    formData = request.form.to_dict()
    # print(formData)
    print(json.dumps(formData, indent=4))
    return jsonify(
        {"GPA": 3.5}
    )
