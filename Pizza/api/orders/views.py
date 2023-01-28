from flask_restx import Namespace, Resource, fields
from ..models.orders import Order
from ..models.users import User
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity

order_namespace = Namespace('Order', description='Namespace for Order')

order_model = order_namespace.model(
    'Order', {
        'flavour': fields.String(description='Pizza Flavour', required=True),
        'quantity': fields.Integer(description='Number of Pizzas', required=True),
        'size': fields.String(description='Pizza Size', required=True,
            enum = ['SMALL', 'MEDIUM', 'LARGE', 'EXTRA_LARGE']
        ),
        'order_status': fields.String(description='Current Order Status', required=True,
            enum = ['PENDING', 'IN_TRANSIT', 'DELIVERED']
        )
    }
)

@order_namespace.route('/orders')
class OrderGetCreate(Resource):

    @order_namespace.marshal_with(order_model)
    @jwt_required()
    def get(self):
        """
            Get All Orders
        """
        orders = Order.query.all()

        return orders, HTTPStatus.OK

    @order_namespace.expect(order_model)
    @order_namespace.marshal_with(order_model)
    @jwt_required()
    def post(self):
        """
            Place an Order
        """

        username = get_jwt_identity()

        current_user = User.query.filter_by(username=username).first

        data = order_namespace.payload

        new_order = Order(
            size = data['size'],
            quantity = data['quantity'],
            flavour = data['flavour']
        )

        new_order.user = current_user

        new_order.save()

        return new_order, HTTPStatus.CREATED


@order_namespace.route('/order/<int:order_id>')
class GetUpdateDelete(Resource):

    @order_namespace.marshal_with(order_model)
    @jwt_required
    def get(self, order_id):
        """
            Retrieve an Order by ID
        """        
        order = Order.get_by_id(order_id)

        return order, HTTPStatus.OK

    def put(self, order_id):
        """
            Update an Order by ID
        """
        pass

    def delete(self, order_id):
        """
            Delete an Order by ID
        """
        pass

@order_namespace.route('/user/<int:user_id>/order/<int:order_id>')
class GetSpecificOrderByUser(Resource):
    def get(self, user_id, order_id):
        """
            Get a User's Specific Order
        """
        pass

@order_namespace.route('/user/<int:user_id>/orders')
class UserOrders(Resource):
    def get(self):
        """
            Get All Orders by a User
        """
        pass

@order_namespace.route('/order/status/<int:order_id>')
class UpdateOrderStatus(Resource):
    def patch(self, order_id):
        """
            Update an Order's Status
        """
        pass