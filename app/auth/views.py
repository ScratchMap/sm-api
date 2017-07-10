from flask_restful import Resource
from flask import request
# from flask import make_response, jsonify
from app.utils import db
# from app.utils import db, login_manager
# from app.users.models import User
from app.users.models import User, decode_auth_token as user_decode_auth_token
from functools import wraps
# from flask_login import login_user, login_required, logout_user, current_user


"""
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
"""

def authenticate(f):
    @wraps(f)
    def decorate_function(*args, **kwargs):
        responseObject = {
            'status' : 'error',
            'message' : 'Something went wrong. Please contact us.'
        }
        code = 401

        auth_header = request.headers.get('Authorization')
        if not auth_header:
            responseObject['message'] = 'Provide a valid auth token.'
            code = 403
            # return make_response(jsonify(responseObject)), code
            return responseObject, code

        # auth_token = auth_header.split(' ')[1]
        auth_token = auth_header
        resp = user_decode_auth_token(auth_token)
        if isinstance(resp, str):
            responseObject['message'] = resp
            # return make_response(jsonify(responseObject)), code
            return responseObject, code

        user = User.query.filter_by(
            id=resp
        ).first()
        if not user:
            # return make_response(jsonify(responseObject)), code
            return responseObject, code

        return f(resp=resp, *args, **kwargs)

    return decorate_function

class RegisterAPI(Resource):
    '''
    User registration
    '''
    def post(self):
        post_data = request.get_json()

        user = User.query.filter_by(
            email=post_data.get('email')
        ).first()
        if not user:
            try:
                user = User(
                    email=post_data.get('email'),
                    name=post_data.get('name'),
                    password=post_data.get('password')
                )
                db.session.add(user)
                db.session.commit()

                """
                login_user(user)
                
                responseObject = {
                    'status' : 'success',
                    'message' : 'Successfully registered.'
                }
                return responseObject, 201
                """
                auth_token = user.encode_auth_token(user.id)
                if isinstance(auth_token, bytes):
                    responseObject = {
                        'status' : 'success',
                        'message' : 'Successfully registered.',
                        'auth_token' : auth_token.decode()
                    }
                    # return make_response(jsonify(responseObject)), 201
                    return responseObject, 201

            except Exception as e:
                db.session.rollback()

                responseObject = {
                    'status' : 'fail',
                    'message' : 'User already exists. Please Log in.'
                }
                # return make_response(jsonify(responseObject)), 202
                return responseObject, 202

        else:
            responseObject = {
                'status' : 'fail',
                'message' : 'Sorry. That user already exists.'
            }
            # return make_response(jsonify(responseObject)), 400
            return responseObject, 400

class LoginAPI(Resource):
    '''
    User login
    '''
    def post(self):
        post_data = request.get_json()
        
        try:
            user = User.query.filter_by(
                email=post_data.get('email')
            ).first()

            if user and user.check_password(password=post_data.get('password')):
                
                """
                login_user(user)
                
                responseObject = {
                    'status' : 'success',
                    'message' : 'Successfully login in.'
                }
                return responseObject, 200
                """

                auth_token = user.encode_auth_token(user.id)

                if isinstance(auth_token, bytes):
                    responseObject = {
                        'status' : 'success',
                        'message' : 'Successfully login in.',
                        'auth_token' : auth_token.decode()
                    }
                    # return make_response(jsonify(responseObject)), 200
                    return responseObject, 200

            else:
                responseObject = {
                    'status' : 'fail',
                    'message' : 'User does not exits.'
                }
                # return make_response(jsonify(responseObject)), 404
                return responseObject, 404

        except Exception as e:
            responseObject = {
                'status' : 'fail',
                'message' : 'Try again.'
            }
            # return make_response(jsonify(responseObject)), 500
            return responseObject, 500

class UserAPI(Resource):
    '''
    User
    '''
    """
    @login_required
    def get(self):
    """
    @authenticate
    def get(self, resp):
        user = User.query.filter_by(
            id=resp
        ).first()
        """
        user = current_user
        """

        responseObject = {
            'status' : 'success',
            'data' : {
                'user_id' : user.id,
                'email' : user.email
            }
        }
        # return make_response(jsonify(responseObject)), 200
        return responseObject, 200

class LogoutAPI(Resource):
    '''
    Logout
    '''
    """
    @login_required
    def get(self):
        logout_user()
    """
    @authenticate
    def get(self, resp):
        responseObject = {
            'status' : 'success',
            'message' : 'Successfully logged out.'
        }
        # return make_response(jsonify(responseObject)), 200
        return responseObject, 200

