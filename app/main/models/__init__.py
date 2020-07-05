from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .UserModel import UserModel
from .PropertyModel import PropertyModel
from .RentModel import RentModel
