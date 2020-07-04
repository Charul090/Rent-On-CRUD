from ..models import db, UserModel
import json
import jwt


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


def login(details):
    try:
        email = details["email"]
        password = details["password"]
    except KeyError:
        return False

    if email == "" or password == "":
        return False

    if type(email) is not str and type(password) is not str:
        return False

    return True
