from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from app.models import db


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from app.routes import main

    app.register_blueprint(main)

    return app
