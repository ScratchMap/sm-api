"""
    app module
"""

import os

from flask import Flask
from app.api import api
from app.utils import db, bcrypt, login_manager
from flask_migrate import Migrate

BASEDIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
DEFAULT_CONFIG = os.path.join(BASEDIR, 'config/local.py')

def create_app(config=None):
    """ create app """
    app = Flask(__name__)

    if config:
        path_to_config = os.path.join(BASEDIR, config)
        app.config.from_pyfile(path_to_config)
    else:
        app.config.from_pyfile(DEFAULT_CONFIG)

    init_app(app)
    
    migrate = Migrate(app, db)

    return app

def init_app(app):
    api.init_app(app)
    init_db(app)
    init_bcrypt(app)
    init_login_manager(app)

    migrate = Migrate(app, db)

def init_db(app):
    db.init_app(app)

def init_bcrypt(app):
    bcrypt.init_app(app)

def init_login_manager(app):
    login_manager.init_app(app)