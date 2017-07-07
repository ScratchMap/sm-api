from flask_restful import Resource
# from flask import make_response, jsonify
from app.users.models import User
# from app.auth.views import authenticate
from flask_login import login_required

class Users(Resource):

    # @authenticate
    # def get(self, resp):
    @login_required
    def get(self):
        responseObject = {
            'status' : 'success',
            'message' : [{
                'id': user.id,
                'name': user.name,
                'email' : user.email
            }for user in User.query.all()]
        }
        # return make_response(jsonify(responseObject)), 201
        return responseObject, 201

