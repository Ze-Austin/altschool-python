from flask import Flask
from flask_restx import Api
from .orders.views import order_namespace
from .auth.views import auth_namespace

def create_app():
    app = Flask(__name__)

    api = Api(app)

    api.add_namespace(order_namespace)
    api.add_namespace(auth_namespace, path='/auth')

    return app