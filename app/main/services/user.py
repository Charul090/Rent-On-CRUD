from ..models import db, UserModel, RentModel
import json
import jwt
from instance.config import SECRET_KEY
import datetime
from ..util.auth_token import check_auth_token


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
        return json.dumps({"error": True,
                           "message": "One or more fields are missing!"})

    if email == "" or password == "":
        return json.dumps({"error": True, "message": "Empty Fields"})

    if type(email) is not str or type(password) is not str:
        return json.dumps({"error": True, "message": "Wrong data format!"})

    data = UserModel.query.filter(UserModel.email == email).first()

    if data is not None:
        if data.password == password:
            obj = {
                "email": data.email,
                "type": data.type,
                "created_at": str(datetime.datetime.utcnow()),
                "expire_at": str(datetime.datetime.utcnow()
                                 + datetime.timedelta(days=1))
            }

            encode_jwt = jwt.encode(obj, SECRET_KEY)

            return json.dumps({"error": False, "token": encode_jwt.decode(),
                               "message": "Logged in successfully!"})

        else:
            return json.dumps({"error": True,
                               "message":
                               "You have entered the wrong password!"})

    return json.dumps({"error": True, "message": "Unknown error!"})


def rent(details, token):
    try:
        property_id = details["property_id"]
        time = details["time"]
        duration = details["duration"]
    except KeyError:
        return json.dumps({"error": True,
                           "message": "One or more fields are missing!"})

    if property_id == "" or time == "" \
       or duration == "":
        return json.dumps({"error": True, "message": "Empty Fields"})

    if type(property_id) is not int or type(time) is not str or \
       type(duration) is not int:
        return json.dumps({"error": True, "message": "Wrong data format!"})

    status, data = check_auth_token(token)

    if status is False:
        return json.dumps({"error": True,
                           "message": "Token has expired!"})

    user_data = UserModel.query.filter(UserModel.email
                                       == data["email"]).first()

    if user_data is not None:
        user_id = user_data.id

        data = RentModel(user_id=user_id, property_id=property_id,
                         booking_time=time, duration=duration)
        db.session.add(data)
        db.session.commit()

        return json.dumps({"error": False,
                           "message": "Property rented successfully!"})

    else:
        return json.dumps({"error": True, "message": "Email does not exists"})
