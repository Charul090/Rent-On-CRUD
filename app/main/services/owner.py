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
        return False

    if firstname == "" or lastname == "" or email == "" or password == "":
        return False

    if type(firstname) is not str or type(lastname) is not str or type(email) \
       is not str or type(password) is not str:
        return False

    return True
