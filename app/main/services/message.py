from ..models import db, MessageModel, ClosureModel
import json
import jwt
from instance.config import SECRET_KEY
import datetime
from ..util.auth_token import check_auth_token
from sqlalchemy import and_


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
        sender_id = details["sender"]
        receiver_id = details["receiver"]
        message = details["message"]
    except KeyError:
        return json.dumps({"error": True,
                           "message": "One or more fields are missing!"})

    if sender_id == "" or receiver_id == "" or message == "":
        return json.dumps({"error": True, "message": "Empty Params"})

    if type(sender_id) is not int or type(receiver_id) is \
    not int or type(message) is not str:
        return json.dumps({"error": True, "message": "Wrong params format!"})

    enter_data_message = MessageModel(
                         message=message, sender_id=sender_id,
                         receiver_id=receiver_id)

    db.session.add(enter_data_message)
    db.session.commit()

    previous_id_fetch = MessageModel.query.filter(
                        and_(MessageModel.sender_id.in_(
                        [sender_id, receiver_id]),
                        MessageModel.receiver_id.in_(
                        [sender_id, receiver_id])))

    previous_id = []

    for z in previous_id_fetch:
        previous_id.append(z.id)

    anc = 0
    des = 0

    if len(previous_id) == 1:
        anc = int(previous_id[0])
        des = int(previous_id[0])
    else:
        anc = int(previous_id[-2])
        des = int(previous_id[-1])

    enter_data_closure = ClosureModel(
                         ancestor=anc,
                         descendant=des)

    db.session.add(enter_data_closure)
    db.session.commit()

    return json.dumps({"error": False, "message": "Message recorded"})
