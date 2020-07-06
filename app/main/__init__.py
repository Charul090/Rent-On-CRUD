from flask import Flask
from flask_cors import CORS
from config import app_config
from .models import db
from flask_migrate import Migrate
from .routes import user as user_blueprint, owner as owner_blueprint, message as message_blueprint


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile("config.py")

    app.register_blueprint(user_blueprint, url_prefix="/user")
    app.register_blueprint(owner_blueprint, url_prefix="/owner")
    app.register_blueprint(message_blueprint, url_prefix="/message")

    db.init_app(app)
    migrate = Migrate(app, db)

    return app
