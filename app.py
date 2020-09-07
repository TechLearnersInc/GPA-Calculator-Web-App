from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from sqlalchemy.ext.declarative import declarative_base

# from Database.database import Database

app = Flask(__name__)

app.config['SECRET_KEY'] = 'HelloWorld'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://inan:12345@localhost/gpacalculator"
app.config['SQLALCHEMY_POOL_SIZE'] = 20
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_pre_ping': True,
    'pool_recycle': 1,
}

# Database Connect
db = SQLAlchemy(app=app)
dbEngine = db.engine
dbBase = declarative_base(dbEngine)

# protecting our app
csrf = CSRFProtect(app)

from route import *

if __name__ == '__main__':
    app.run()
