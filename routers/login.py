from flask import Blueprint
from controllers.login import get_login, post_login

login_blueprint = Blueprint('/login', __name__)


login_blueprint.get('')(get_login)
login_blueprint.post('')(post_login)