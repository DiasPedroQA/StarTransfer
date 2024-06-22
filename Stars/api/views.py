from flask import Blueprint, jsonify, request
from api_rest.controllers import get_all_stars, get_star_by_id, add_star, update_star, delete_star

star_bp = Blueprint('stars', __name__, url_prefix='/stars')

@star_bp.route('/', methods=['GET'])
def get_stars():
    return jsonify(get_all_stars())

@star_bp.route('/<int:star_id>', methods=['GET'])
def get_star(star_id):
    star = get_star_by_id(star_id)
    if not star:
        return jsonify({'error': 'Star not found'}), 404
    return jsonify(star)

@star_bp.route('/', methods=['POST'])
def create_star():
    data = request.get_json()
    if not data or 'name' not in data or 'distance' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    
    new_star = add_star(data)
    return jsonify(new_star), 201

@star_bp.route('/<int:star_id>', methods=['PUT'])
def update_star_endpoint(star_id):
    data = request.get_json()
    if not data or 'name' not in data or 'distance' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    
    updated_star = update_star(star_id, data)
    if not updated_star:
        return jsonify({'error': 'Star not found'}), 404
    
    return jsonify(updated_star)

@star_bp.route('/<int:star_id>', methods=['DELETE'])
def delete_star_endpoint(star_id):
    deleted_star = delete_star(star_id)
    if not deleted_star:
        return jsonify({'error': 'Star not found'}), 404
    
    return jsonify(deleted_star)
