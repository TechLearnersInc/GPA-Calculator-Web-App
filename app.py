from flask import Flask

from flask_wtf import CSRFProtect

app = Flask(__name__)

# protecting our app
csrf = CSRFProtect(app)

app.config['SECRET_KEY'] = 'HelloWorld'

from route import *

if __name__ == '__main__':
    app.run()
