from flask_restx import Namespace, Resource, fields

auth_namespace = Namespace('Auth', description='Namespace for Authentication')

auth_model = auth_namespace.model(
    'User', {
        'id': fields.Integer(),
        'username': fields.String(required=True, description="A username"),
        'email': fields.String(required=True, description="An email"),
        'password': fields.String(required=True, description="A password")
    }
)

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