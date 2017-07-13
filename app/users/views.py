from flask_restful import Resource
from app.users.models import User
from app.auth.views import authenticate

class Users(Resource):

    @authenticate
    def get(self, resp):
        responseObject = {
            'status' : 'success',
            'message' : [{
                'id': user.id,
                'name': user.name,
                'email' : user.email
            }for user in User.query.all()]
        }
        return responseObject, 201

