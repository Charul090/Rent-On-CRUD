from ..models import db, UserModel
import json
import jwt
from instance.config import SECRET_KEY
import datetime


def register(details):
    try:
        firstname = details["firstname"]
        lastname = details["lastname"]
        password = details["password"]
        email = details["email"]
    except KeyError:
        return json.dumps({"error": True,
                           "message": "One or more fields are missing!"})

    if firstname == "" or lastname == "" or email == "" or password == "":
        return json.dumps({"error": True, "message": "Empty Fields"})

    if type(firstname) is not str or type(lastname) is not str or type(email) \
       is not str or type(password) is not str:
        return json.dumps({"error": True, "message": "Wrong data format!"})

    status = UserModel.query.filter(UserModel.email == email).first()

    if status is None:
        user_type = "owner"

        user = UserModel(firstname=firstname, lastname=lastname,
                         email=email, password=password, type=user_type)

        db.session.add(user)
        db.session.commit()

        return json.dumps({"error": False,
                           "message": "User registered successfully"})

    return {"error": True, "message": "Email already exists"}
