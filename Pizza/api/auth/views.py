from flask_restx import Namespace, Resource

auth_namespace = Namespace('auth', description='name space for authentication')

@auth_namespace.route('/')
class HelloAuth(Resource):
    def get(self):
        return {"message": "Hello, Auth. Nice to meet you!"}