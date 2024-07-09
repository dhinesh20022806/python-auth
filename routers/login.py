from flask import Blueprint
from controllers.login import login

login_blueprint = Blueprint('/login', __name__)


login_blueprint.get('')(login)
