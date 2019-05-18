from flask_marshmallow import Marshmallow
from app.model import Client

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class ClientSchema(ma.ModelSchema):
    """Generate marshmallow Schemas using ModelSchema."""

    class Meta:
        """Import model client."""

        model = Client
