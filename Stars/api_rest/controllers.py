from flask import jsonify, request
import os

stars = []

def get_all_stars():
    return jsonify(stars)

def add_star():
    data = request.get_json()
    new_star = {'name': data['name'], 'distance': data['distance']}
    stars.append(new_star)
    return jsonify({'message': 'Star added successfully'}), 201

def validate_path():
    path = request.args.get('path')
    if not path:
        return jsonify({'message': 'Path parameter is missing'}), 400
    validation_message = is_valid_path(path)
    return jsonify({'message': validation_message})
    
def is_valid_path(path):
    if os.path.exists(path):
        return f"The path '{path}' is valid and exists."
    else:
        return f"The path '{path}' is not a valid path or does not exist."
