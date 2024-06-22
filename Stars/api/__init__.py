from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    api_rest = Flask(__name__)
    api_rest.config.from_object(Config)
    db.init_app(api_rest)

    with api_rest.app_context():
        from . import models, views
        db.create_all()
        api_rest.register_blueprint(views.bp)

    return api_rest
