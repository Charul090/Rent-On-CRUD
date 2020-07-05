from . import user
from flask import request
from ..services.user import register, login, rent


@user.route("/register", methods=["POST"])
def registerUser():

    response = register(request.json)

    return response


@user.route("/login", methods=["POST"])
def loginUser():

    response = login(request.json)

    return response


@user.route("/rent", methods=["POST"])
def userRent():
    token = request.headers.get("Auth")

    response = rent(request.json, token)

    return response
