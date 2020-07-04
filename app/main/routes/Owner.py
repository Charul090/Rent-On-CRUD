from . import owner
from flask import request
from ..services.owner import register, login


@owner.route("/register", methods=["POST"])
def registerOwner():

    response = register(request.json)

    return response


@owner.route("/login", methods=["POST"])
def loginOwner():

    response = login(request.json)

    return response
