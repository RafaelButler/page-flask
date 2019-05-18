"""Imports."""
from flask import Flask
from flask_migrate import Migrate
from app.model import configure as configure_db
from app.serealizer import configure as configure_ma


def creat_app():
    """All extensions plugged into function creat_app."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # call SQLAlchemy function
    configure_db(app)
    # Migrate db
    Migrate(app, app.db)
    # Serealizer model
    configure_ma(app)
    from app.client import bp
    app.register_blueprint(bp)
    return app
