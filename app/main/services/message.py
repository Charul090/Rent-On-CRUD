from ..models import db, MessageModel, ClosureModel
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
        return json.dumps({"error": True,
                           "message": "One or more fields are missing!"})

    if type(sender) == "" or type(receiver) == "":
        return json.dumps({"error": True, "message": "Empty Params"})

    if type(sender) is not int or type(receiver) is not int:
        return json.dumps({"error": True, "message": "Wrong params format!"})

    results = db.session.execute(''' SELECT m.message,m.sender_id,m.receiver_id
                                 FROM message as m JOIN closure
                                 as c ON m.id = c.ancestor
                                 WHERE
                                 ((m.sender_id = %d and m.receiver_id = %d)
                                 OR (m.sender_id = %d and m.receiver_id = %d))
                                 AND (c.ancestor = c.descendant); '''
                                 % (sender, receiver, receiver, sender))

    messages = []

    for x in results:
        obj = {
            "message": x[0],
            "sender": x[1],
            "receiver": x[2]
        }

        messages.append(obj)

    data = {
        "error": False,
        "sender_id": sender,
        "receiver_id": receiver,
        "messages": messages
    }

    return json.dumps(data)


def send_message(details):
    try:
        ancestor = details["ancestor"]
        descendnt = details["descendnt"]
    except KeyError:
        return False

    if type(ancestor) == "" or type(descendnt) == "":
        return False

    if type(ancestor) is not int or type(descendnt) is not int:
        return False

    return True
