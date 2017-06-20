from flask_restful import Resource
from flask import request, abort
from database.users.models import User as db_user
from app.api import db

class User(Resource):

    def get(self):
        name = request.args.get('name', '')
        result = db_user.query.filter_by(name=name).first()
        if not result and name != '':
            result = db_user(name=str(name))
            db.session.add(result)
            db.session.commit()
        return {'message': str(result)}
