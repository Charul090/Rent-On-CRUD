from . import message
from flask import request
from ..services.message import get_message
from ..services.message import send_message


@message.route("/get")
def getMessage():

    data = {
        "sender": request.args.get("sender", type=int),
        "receiver": request.args.get("receiver", type=int)
    }

    response = get_message(data)

    return response


@message.route("/send", methods=["POST"])
def sendMessage():
    
    response = send_message(request.json)

    return response
