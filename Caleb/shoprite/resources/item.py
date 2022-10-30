import uuid
from flask import jsonify, request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from models import ItemModel
from schemas import ItemSchema, UpdateItemSchema
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

blp = Blueprint("item", __name__, description="Operations on Item")

@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        return item

    def delete(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()

        return {"message": "Item Deleted"}

    @blp.arguments(UpdateItemSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        item = ItemModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = ItemModel(id=item_id, **item_data)

        db.session.add(item)
        db.session.commit()

        return item

@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return ItemModel.query.all()
        item = items.values()
        schemass = ItemSchema()
        result = schemass.dump(item, many=True)

        return jsonify(result)

    @blp.arguments(ItemSchema)
    @blp.response(200, ItemSchema)
    def post(self, item_data):
        item = ItemModel(**item_data)

        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(400, message="An item with that name already exists")
        except SQLAlchemyError:
            abort(500, message="An error occured while creating an item")

        return item, 201
        




