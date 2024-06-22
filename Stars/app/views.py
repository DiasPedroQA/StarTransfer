from flask import Blueprint
from .controllers import get_stars, add_star, update_star, delete_star

bp = Blueprint('main', __name__)

bp.route('/stars', methods=['GET'])(get_stars)
bp.route('/stars', methods=['POST'])(add_star)
bp.route('/stars/<int:star_id>', methods=['PUT'])(update_star)
bp.route('/stars/<int:star_id>', methods=['DELETE'])(delete_star)
