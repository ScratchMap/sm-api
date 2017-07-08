'''
    PRODUCTION config file

    please setup next environment variables:
        SQLALCHEMY_DATABASE_URI

'''

import os

DEBUG = False
TESTING = False

JSON_AS_ASCII = False

BCRYPT_LOG_ROUNDS = 13

TOKEN_EXPIRATION_DAYS = 30
TOKEN_EXPIRATION_SECONDS = 0

SECRET_KEY = os.environ.get('SECRET_KEY')

ERROR_404_HELP = False

PORT = os.environ['PORT']
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = True
