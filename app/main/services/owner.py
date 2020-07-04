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


def login(details):
    try:
        email = details["email"]
        password = details["password"]
    except KeyError:
        return json.dumps({"error": True,
                           "message": "One or more fields are missing!"})

    if email == "" or password == "":
        return json.dumps({"error": True, "message": "Empty Fields"})

    if type(email) is not str or type(password) is not str:
        return json.dumps({"error": True, "message": "Wrong data format!"})

    data = UserModel.query.filter(UserModel.email == email).first()

    if data is not None:
        if data.type != "owner":
            return json.dumps({"error": True,
                               "message": "User does not have authorization!"})
        else:
            if data.password == password:
                obj = {
                    "email": data.email,
                    "type": data.type,
                    "created_at": str(datetime.datetime.utcnow()),
                    "expire_at": str(datetime.datetime.utcnow()
                                     + datetime.timedelta(days=1))
                }

                encode_jwt = jwt.encode(obj, SECRET_KEY)

                return json.dumps({"error": False,
                                   "token": encode_jwt.decode(),
                                   "message": "Logged in successfully!"})

            else:
                return json.dumps({"error": True,
                                   "message":
                                   "You have entered the wrong password!"})

    return json.dumps({"error": True, "message": "Unknown error!"})


def add_property(details):
    try:
        area = details["area"]
        amenities = details["amenities"]
        bedrooms = details["bedrooms"]
        furnishing = details["furnishing"]
        address = details["address"]
        price = details["price"]

    except KeyError:
        return False

    if area == "" or amenities == "" or bedrooms == "" or furnishing == "" or \
       address == "" or price == "":
        return False

    if type(area) is not int or type(bedrooms) is not int or \
       type(furnishing) is not bool \
       or type(address) is not str or type(price) is not int:
        return False

    return True
