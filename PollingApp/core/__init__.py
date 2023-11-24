from flask import Flask
from core.auth import auth_bp
from core.main import main_bp
import os

from .extensions import db

# application factory
def create_app():
    app = Flask(__name__)  # create a flask app instance
    app.secret_key = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")

    db.init_app(app)

    # register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)


    return app