from . import owner
from flask import request
from ..services.owner import register, login, add_property, \
                             delete_property, update_property


@owner.route("/register", methods=["POST"])
def registerOwner():

    response = register(request.json)

    return response


@owner.route("/login", methods=["POST"])
def loginOwner():

    response = login(request.json)

    return response


@owner.route("/add", methods=["POST"])
def addProperty():

    token = request.headers.get("Auth")

    response = add_property(request.json, token)

    return response


@owner.route("/delete", methods=["POST"])
def deleteProperty():

    token = request.headers.get("Auth")

    response = delete_property(request.json, token)

    return response


@owner.route("/update", methods=["POST"])
def updateProperty():

    token = request.headers.get("Auth")

    response = update_property(request.json, token)

    return response
