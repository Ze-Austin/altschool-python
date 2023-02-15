import unittest
from .. import create_app
from ..config.config import config_dict
from ..utils import db
from flask_jwt_extended import create_access_token
from ..models.orders import Order

class OrderTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config=config_dict['test'])
        self.appctx = self.app.app_context()
        self.appctx.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.drop_all()
        self.appctx.pop()
        self.app = None
        self.client = None

    def test_get_all_orders(self):
        token = create_access_token(identity="Test User")

        headers = {
            "Authorization": f"Bearer {token}"
        }

        response = self.client.get('/orders/orders', headers=headers)

        assert response.status_code == 200

        assert response.json == []

    def test_place_order(self):
        data = {
            "size": "SMALL",
            "quantity": 1,
            "flavour": "Pepperoni"
        }

        token = create_access_token(identity="Test User")

        headers = {
            "Authorization": f"Bearer {token}"
        }

        response = self.client.post('/orders/orders', json=data, headers=headers)

        assert response.status_code == 201

        orders = Order.query.all()

        order_id = orders[0].id

        assert order_id == 1

        assert len(orders) == 1

        assert response.json['size'] == 'Sizes.SMALL'

    # Function to test the retrieval of a single order
    def test_get_single_order(self):
        token = create_access_token(identity="Test User")

        headers = {
            "Authorization": f"Bearer {token}"
        }

        response = self.client.get('/orders/order/1', headers=headers)

        assert response.status_code == 404