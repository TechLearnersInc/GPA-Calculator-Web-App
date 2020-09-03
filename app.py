import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_wtf import CSRFProtect

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# protecting our app
csrf = CSRFProtect(app)

app.config['SECRET_KEY'] = 'HelloWorld'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from route import *

if __name__ == '__main__':
    app.run()
