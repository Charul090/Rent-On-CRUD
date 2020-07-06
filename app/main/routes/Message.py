from . import message
from flask import request
from ..services.message import get_message


@message.route("/get")
def getMessage():

    data = {
        "sender": request.args.get("sender", type=int),
        "receiver": request.args.get("receiver", type=int)
    }

    response = get_message(data)

    return response
