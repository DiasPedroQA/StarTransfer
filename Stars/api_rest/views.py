from flask import Blueprint, request, jsonify
from .controllers import get_all_stars, add_star, validate_path

main_bp = Blueprint('main', __name__)

@main_bp.route('/stars', methods=['GET'])
def get_stars():
    return get_all_stars()

@main_bp.route('/stars', methods=['POST'])
def create_star():
    return add_star()

@main_bp.route('/validate_path', methods=['GET'])
def validate_path_route():
    return validate_path()
