from . import db

class Star(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    distance = db.Column(db.Float)

    def __repr__(self):
        return f'<Star {self.name}>'
