from . import user
from flask import request

@user.route("/register")
def register():
    return "Hi"