"""All the imports here."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def configure(app):
    """Start to initialize the Database."""
    db.init_app(app)
    app.db = db


class client(db.Model):
    """Client table with id, name, email."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(225))
    email = db.Column(db.String(225))
