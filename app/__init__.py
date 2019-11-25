from flask import Flask,jsonify
from app.config import Config
from flask_sqlalchemy import SQLAlchemy

sqlalchemy = SQLAlchemy()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(Config)

    initialize_extentions(app)
    register_blueprints(app)
    return app

def initialize_extentions(app):
    sqlalchemy.init_app(app)

def register_blueprints(app):
    from app.api import api
    app.register_blueprint(api)