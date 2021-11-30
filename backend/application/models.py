from application import db

class Galleries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gallery_name = db.Column(db.String(30), nullable=False)
    informaiton = db.Column(db.String(30), nullable=False)
    fee = db.Column(db.Boolean, nullable=False, default=False)
    location = db.relationship('Location', backref='galleriesbr')

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(30), nullable=False)
    gallery_id = db.Column(db.String(30), foreign_key=('galleries.id'), nullable=false)
    