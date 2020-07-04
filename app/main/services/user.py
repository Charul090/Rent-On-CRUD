from ..models import db, UserModel
import json


def register(details):
    firstname = details["firstname"]
    lastname = details["lastname"]
    email = details["email"]
    password = details["password"]

    status = UserModel.query.filter(UserModel.email == email).first()

    if status is None:
        user_type = "user"

        user = UserModel(firstname=firstname, lastname=lastname,
                         email=email, password=password, type=user_type)

        db.session.add(user)
        db.session.commit()

        return json.dumps({"error": False,
                           "message": "User registered successfully"})

    return {"error": True, "message": "Email already exists"}
