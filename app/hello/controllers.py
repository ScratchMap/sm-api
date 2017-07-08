from flask_restful import Resource
from flask import request, abort

class Hello(Resource):
    def get(self):
        name = request.args.get('name', '')
        surname = request.args.get('surname', '')
        if len(name) == 0 or len(surname) == 0:
            abort(403)
        return {'message': 'Hello {name} {surname}'.format(name=name, surname=surname)}
