'''
    LOCAL config file

    please setup next environment variables:
        SQLALCHEMY_DATABASE_URI

'''

DEBUG = True
TESTING = False

JSON_AS_ASCII = False

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:PostGreSQL@localhost/sm'
SQLALCHEMY_TRACK_MODIFICATIONS = True

PERMANENT_SESSION_LIFETIME = 3600
