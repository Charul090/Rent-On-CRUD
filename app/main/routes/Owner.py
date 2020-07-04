from . import owner
from flask import request
from ..services.owner import register


@owner.route("/register", methods=["POST"])
def registerOwner():

    response = register(request.json)

    return response
