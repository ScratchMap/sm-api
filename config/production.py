'''
    PRODUCTION config file

    please setup next environment variables:
        SQLALCHEMY_DATABASE_URI

'''

import os

DEBUG = False
TESTING = False

JSON_AS_ASCII = False

ERROR_404_HELP = False

PORT = os.environ['PORT']
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
