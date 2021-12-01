from application import db

class Locations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country= db.Column(db.String(30), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    galleries = db.relationship('Galleries', backref='location')

class Galleries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gallery_name = db.Column(db.String(30), nullable=False)
    information = db.Column(db.String(30), nullable=False)
    fee = db.Column(db.String(30), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)


    
    