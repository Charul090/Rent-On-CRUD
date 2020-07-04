from . import user
from flask import request
from ..services.user import register


@user.route("/register", methods=["POST"])
def registerUser():

    response = register(request.json)

    return response
