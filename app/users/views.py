from flask_restful import Resource
from flask import request, abort

import uuid

from app.users.models import User
from app.database import db

class Users(Resource):

    def get(self):
        # name = request.args.get('name', '')
        # result = User.query.filter_by(name=name).first()

        # if not result and name != '':
        #     result = db_user(name=str(name))
        #     # db.session.add(result)
        #     # db.session.commit()
        # return {'message': str(result)}

        return [ {'id': user.id, 'name': user.name} for user in User.query.all() ]

    def post(self):
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        id = str(uuid.uuid4())
        print(name)
        print(email)
        print(password)
        user = User(id=id, name=name, email=email, password=password)

        db.session.add(user)
        db.session.commit()

        return user.id;
