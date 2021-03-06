from ..models import db, UserModel, PropertyModel
import json
import jwt
from instance.config import SECRET_KEY
import datetime
from ..util.auth_token import check_auth_token


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


def add_property(details, token):
    try:
        area = details["area"]
        amenities = details["amenities"]
        bedrooms = details["bedrooms"]
        furnishing = details["furnishing"]
        address = details["address"]
        price = details["price"]

    except KeyError:
        return json.dumps({"error": True,
                           "message": "One or more fields are missing!"})

    if area == "" or amenities == "" or bedrooms == "" or furnishing == "" or \
       address == "" or price == "":
        return json.dumps({"error": True, "message": "Empty Fields"})

    if type(area) is not int or type(bedrooms) is not int or \
       type(furnishing) is not bool \
       or type(address) is not str or type(price) is not int:
        return json.dumps({"error": True, "message": "Wrong data format!"})

    status, data = check_auth_token(token)

    if status is False or data["type"] == "user":
        return json.dumps({"error": True,
                           "message": "User does not have authorization!"})

    owner_data = UserModel.query.filter(UserModel.email
                                        == data["email"]).first()

    owner_id = owner_data.id

    amenities = ",".join(amenities)

    data = PropertyModel(area=area, amenities=amenities, bedrooms=bedrooms,
                         furnishing=furnishing, address=address,
                         price=price, owner_id=owner_id)

    db.session.add(data)
    db.session.commit()

    return json.dumps({"error": False,
                       "message": "Property added successfully!"})


def delete_property(details, token):
    try:
        id = details["id"]
    except KeyError:
        return json.dumps({"error": True,
                           "message": "One or more fields are missing!"})

    if type(id) is not int:
        return json.dumps({"error": True, "message": "Wrong data format!"})

    status, data = check_auth_token(token)

    if status is False or data["type"] == "user":
        return json.dumps({"error": True,
                           "message": "User does not have authorization!"})

    delete_data = PropertyModel.query.filter(PropertyModel.id == id).first()

    if delete_data is None:
        return json.dumps({"error": True,
                           "message": "Property does not exist!"})
    else:
        delete_data.delete()
        db.session.commit()
        return json.dumps({"error": False,
                           "message": "Property deleted successfully!"})


def update_property(details, token):
    try:
        area = details["area"]
        amenities = details["amenities"]
        bedrooms = details["bedrooms"]
        furnishing = details["furnishing"]
        address = details["address"]
        price = details["price"]
        id = details["id"]

    except KeyError:
        return json.dumps({"error": True,
                           "message": "One or more fields are missing!"})

    if area == "" or amenities == "" or bedrooms == "" or furnishing == "" or \
       address == "" or price == "" or id == "":
        return json.dumps({"error": True, "message": "Empty Fields"})

    if type(area) is not int or type(bedrooms) is not int or \
       type(furnishing) is not bool \
       or type(address) is not str or type(price) is not int or \
       type(id) is not int:
        return json.dumps({"error": True, "message": "Wrong data format!"})

    status, data = check_auth_token(token)

    if status is False or data["type"] == "user":
        return json.dumps({"error": True,
                           "message": "User does not have authorization!"})

    update_data = PropertyModel.query.filter(PropertyModel.id == id).first()

    if update_data is None:
        return json.dumps({"error": True,
                           "message": "Property does not exist!"})
    else:
        amenities = ",".join(amenities)

        update_data.area = area
        update_data.amenities = amenities
        update_data.bedrooms = bedrooms
        update_data.furnishing = furnishing
        update_data.address = address
        update_data.price = price
        db.session.commit()

        return json.dumps({"error": False,
                           "message": "Property updated successfully!"})
