import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_wtf import CSRFProtect
from Database.database import Database
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# protecting our app
csrf = CSRFProtect(app)

app.config['SECRET_KEY'] = 'HelloWorld'

# # Connecting The MySQL Database
# app.config['MYSQL_HOST'] = 'https://techlearners.mysql.database.azure.com'
# app.config['MYSQL_USER'] = 'inan@techlearners'
# app.config['MYSQL_PASSWORD'] = 'HelloWorld12345'
# app.config['MYSQL_DB'] = 'gpacalculator'
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql//techlearners.mysql.database.azure.com:3306/gpacalculator"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

db = Database()
#db.reflect_tables()


from route import *

if __name__ == '__main__':
    app.run()
