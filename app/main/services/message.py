from ..models import MessageModel, ClosureModel
import json
import jwt
from instance.config import SECRET_KEY
import datetime
from ..util.auth_token import check_auth_token


def get_message(details):
    try:
        sender = details["sender"]
        receiver = details["receiver"]
    except KeyError:
        return False
    
    if type(sender) == "" or type(receiver) == "":
        return False

    if type(sender) is not int or type(receiver) is not int:
        return False

    return True
