from flask import Blueprint
from controllers.register import get_register, post_register

register_blueprint = Blueprint( '/register', __name__)

register_blueprint.get('')(get_register)

register_blueprint.post('')(post_register)