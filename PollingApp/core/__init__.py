from flask import Flask
from core.auth import auth_bp
from core.main import main_bp

# application factory
def create_app():
    app = Flask(__name__)  # create a flask app instance

    # register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)


    return app