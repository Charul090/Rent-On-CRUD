from flask import Blueprint

user = Blueprint('user', __name__)
owner = Blueprint('owner',__name__)

from . import User,Owner
