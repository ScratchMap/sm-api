from app import app
from flask import request
from flask import jsonify

@app.route('/')
@app.route('/index')
def index():
    if request.method == 'GET':
        name = 'Darth'
        lastname = 'Vader'
        response = jsonify(name=name, lastname=lastname)
    return response
