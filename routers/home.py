from flask import Blueprint
from controllers.home import index

home_blueprint = Blueprint('/', __name__)

home_blueprint.get('')(index)