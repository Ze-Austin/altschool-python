from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from models import UserModel
from db import db
from schemas import UserSchema

blp = Blueprint("Users", "users", description="Operations on Users")

@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        if UserModel.query.filter(UserModel.username == user_data["username"]).first():
            abort(409, message="This username is taken")
        
        user = UserModel(
            username = user_data["username"],
            password = pbkdf2_sha256.hash(user_data["password"])
        )

        db.session.add(user)
        db.session.commit()

        return {"message": "User Created Successfully"}, 201