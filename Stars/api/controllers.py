from flask import jsonify, request
from .models import Star
from . import db

def get_all_stars():
    stars = Star.query.all()
    return [star.to_dict() for star in stars]

def get_star_by_id(star_id):
    star = Star.query.get(star_id)
    if not star:
        return None
    return star.to_dict()

def add_star(data):
    new_star = Star(name=data['name'], distance=data['distance'])
    db.session.add(new_star)
    db.session.commit()
    return new_star.to_dict()

def update_star(star_id, data):
    star = Star.query.get(star_id)
    if not star:
        return None
    
    star.name = data['name']
    star.distance = data['distance']
    db.session.commit()
    return star.to_dict()

def delete_star(star_id):
    star = Star.query.get(star_id)
    if not star:
        return None
    
    db.session.delete(star)
    db.session.commit()
    return {'message': 'Star deleted successfully'}
