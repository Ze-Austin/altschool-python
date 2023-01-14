from flask_restx import Namespace, Resource

order_namespace = Namespace('Order', description='Namespace for Order')

@order_namespace.route('/orders')
class OrderGetCreate(Resource):

    def get(self):
        """
            Get all orders
        """
        pass

    def post(self):
        """
            Place an order
        """
        pass


@order_namespace.route('/order/<int:order_id>')
class GetUpdateDelete(Resource):

    def get(self, order_id):
        """
            Retrieve an order by ID
        """
        pass

    def put(self, order_id):
        """
            Update an order by ID
        """
        pass

    def delete(self, order_id):
        """
            Delete an order by ID
        """
        pass

@order_namespace.route('/user/<int:user_id>/order/<int:order_id>')
class GetSpecificOrderByUser(Resource):
    def get(self, user_id, order_id):
        """
            Get a user's specific order
        """
        pass

@order_namespace.route('/user/<int:user_id>/orders')
class UserOrders(Resource):
    def get(self):
        """
            Get all orders by a user
        """
        pass

@order_namespace.route('/order/status/<int:order_id>')
class UpdateOrderStatus(Resource):
    def patch(self, order_id):
        """
            Update an order's status
        """
        pass