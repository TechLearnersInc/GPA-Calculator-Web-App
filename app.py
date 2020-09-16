from flask import Flask
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from os import environ
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

cache = Cache()
cache.init_app(
    app=app,
    config={
        "CACHE_TYPE": "memcached",
        'tcp_nodelay': True,
        'tcp_keepalive': True,
        'connect_timeout': 2000,
        'send_timeout': 750 * 1000,
        'receive_timeout': 750 * 1000,
        '_poll_timeout': 2000,
        'ketama': True,
        'remove_failed': 1,
        'retry_timeout': 2,
        'dead_timeout': 30
    }
)

app.config['SECRET_KEY'] = environ['SECRET_KEY']
app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"mysql+pymys bosql://{environ['DB_USER']}:{environ['DB_PASSWORD']}@{environ['DB_HOST']}/{environ['DB_NAME']}"
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
