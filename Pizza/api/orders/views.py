from flask_restx import Namespace, Resource

order_namespace = Namespace('order', description='name space for authentication')

@order_namespace.route('/')
class HelloOrder(Resource):
    def get(self):
        return {"message": "Hello, Order. Nice to meet you!"}