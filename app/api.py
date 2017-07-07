from flask_restful import Api

from app.test.resource import TestResource
from app.hello.controllers import Hello
from app.users.views import Users
from app.auth.views import RegisterAPI, LoginAPI, UserAPI, LogoutAPI

class ScratchMapApi(Api):

    def init_app(self, app):
        super(ScratchMapApi, self).init_app(app)
        app.after_request(self.add_cors_headers)
        if not app.config['DEBUG']:
            app.run(host='0.0.0.0', port=app.config['PORT'])

    def add_cors_headers(self, response):
        """ Allow Cross domain responses """
        # TODO in production we need to use only our domain
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')

        return response


api = ScratchMapApi()

api.add_resource(RegisterAPI, '/auth/register')
api.add_resource(LoginAPI, '/auth/login')
api.add_resource(UserAPI, '/auth/status')
api.add_resource(LogoutAPI, '/auth/logout')
api.add_resource(Users, '/users')
api.add_resource(Hello, '/hello')
api.add_resource(TestResource, '/test')
