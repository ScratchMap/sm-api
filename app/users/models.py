
from app.utils import db, bcrypt
from datetime import datetime, timedelta
import jwt
from flask import current_app
# from flask_login import UserMixin

# class User(UserMixin, db.Model):
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password,
            current_app.config.get('BCRYPT_LOG_ROUNDS')
        ).decode()

    def __repr__(self):
        return '<User %r>' % self.name

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def encode_auth_token(self, user_id):
        try:
            payload = {
                'exp' : datetime.utcnow() + timedelta(
                    days=current_app.config.get('TOKEN_EXPIRATION_DAYS'),
                    seconds=current_app.config.get('TOKEN_EXPIRATION_SECONDS')
                ),
                'iat' : datetime.utcnow(),
                'sub' : user_id
            }
            return jwt.encode(
                payload,
                current_app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )

        except Exception as e:
            return e


def decode_auth_token(auth_token):
    '''
    Validates the auth token
    :param auth_token:
    :return: integer|string
    '''
    try:
        payload = jwt.decode(
            auth_token,
            current_app.config.get('SECRET_KEY')
        )
        return payload['sub']
    
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
