from flask import jsonify, request
from .models import Star
from . import db

def get_stars():
    stars = Star.query.all()
    return jsonify([star.name for star in stars])

def add_star():
    data = request.get_json()
    new_star = Star(name=data['name'], distance=data['distance'])
    db.session.add(new_star)
    db.session.commit()
    return jsonify({'message': 'Star added successfully'}), 201

def update_star(star_id):
    data = request.get_json()
    star = Star.query.get(star_id)
    if not star:
        return jsonify({'message': 'Star not found'}), 404

    star.name = data['name']
    star.distance = data['distance']
    db.session.commit()
    return jsonify({'message': 'Star updated successfully'})

def delete_star(star_id):
    star = Star.query.get(star_id)
    if not star:
        return jsonify({'message': 'Star not found'}), 404

    db.session.delete(star)
    db.session.commit()
    return jsonify({'message': 'Star deleted successfully'})
