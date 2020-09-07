from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from os import environ
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

app.config['SECRET_KEY'] = environ['SECRET_KEY']
app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{environ['DB_USER']}:{environ['DB_PASSWORD']}@{environ['DB_HOST']}/{environ['DB_NAME']}"
app.config['SQLALCHEMY_POOL_SIZE'] = 20
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_pre_ping': True,
    'pool_recycle': 1
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
