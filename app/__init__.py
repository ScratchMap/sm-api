"""
    app module
"""

import os

from flask import Flask
from app.api import api

BASEDIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
DEFAULT_CONFIG = os.path.join(BASEDIR, 'config/local.py')

print(DEFAULT_CONFIG)

def create_app(config=None):
    """ create app """
    app = Flask(__name__)

    if config:
        app.config.from_pyfile(config)
    else:
        app.config.from_pyfile(DEFAULT_CONFIG)

    init_app(app)

    return app


def init_app(app):
    api.init_app(app)
