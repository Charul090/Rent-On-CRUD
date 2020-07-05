from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .UserModel import UserModel
from .PropertyModel import PropertyModel
from .RentModel import RentModel
from .MessageModel import MessageModel
from .ClosureModel import ClosureModel
