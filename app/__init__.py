"""
    app module
"""

import os

from flask import Flask
from app.api import api

BASEDIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
DEFAULT_CONFIG = os.path.join(BASEDIR, 'config/local.py')


def create_app(config=None):
    """ create app """
    app = Flask(__name__)

    if config:
        path_to_config = os.path.join(BASEDIR, config)
        print(path_to_config)
        app.config.from_pyfile(path_to_config)
    else:
        print(DEFAULT_CONFIG)
        app.config.from_pyfile(DEFAULT_CONFIG)

    init_app(app)

    return app


def init_app(app):
    api.init_app(app)
