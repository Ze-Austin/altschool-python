import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores
from schemas import StoreSchema

StoreBlueprint = Blueprint("store", __name__, description="Operations on Stores")

@StoreBlueprint.route("/store")
class StoreList(MethodView):
    @StoreBlueprint.response(200, StoreSchema(many=True))
    def get(self):
        return {"stores": list(stores.values())}
    
    @StoreBlueprint.arguments(StoreSchema)
    @StoreBlueprint.response(200, StoreSchema)
    def post(self, store_data):
        for store in stores.values():
            if store_data['store_id'] == store['store_id']:
                abort(400, message=f"Store already exists")
            
        store_id = uuid.uuid4().hex
        store = {**store_data, "id": store_id}
        stores[store_id] = store

        return store, 201

@StoreBlueprint.route("/store/<string:store_id>")
class Store(MethodView):
    @StoreBlueprint.response(200, StoreSchema)
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            return abort(404, message="Store not found")
    
    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted"}
        except KeyError:
            return abort(404, message="Store not found")