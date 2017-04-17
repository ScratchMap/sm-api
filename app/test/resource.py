'''
    Exemple of endpoint
'''

from flask_restful import Resource

from app.test.constants import TEST_DATA


class TestResource(Resource):

    def get(self):
        return TEST_DATA
