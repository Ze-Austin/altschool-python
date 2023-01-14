from flask_restx import Namespace, Resource

auth_namespace = Namespace('Auth', description='Namespace for Authentication')

@auth_namespace.route('/signup')
class SignUp(Resource):
    def post(self):
        """
            Register a user 
        """
        pass

@auth_namespace.route('/login')
class Login(Resource):
    def post(self):
        """
            Generate JWT Token
        """
        pass