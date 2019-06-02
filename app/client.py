from flask import Blueprint, render_template, current_app, jsonify, request
from app.serealizer import ClientSchema
from app.model import db, Client

bp = Blueprint('client', __name__)


@bp.route('/', methods=['POST', 'GET'])
def index():
    cl = ClientSchema()
    name = request.forms('username')
    email = request.forms('email')
    user = cl.jsonify(name, email)
    db.session.add_all(user)
    db.session.commit()
    return render_template('index.html', user=user)
