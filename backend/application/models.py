from application import db

class Locations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(30), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    galleries = db.relationship('Galleries', backref='locations')

class Galleries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gallery_name = db.Column(db.String(30), nullable=False)
    information = db.Column(db.String(30), nullable=False)
    fee = db.Column(db.String(30), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)


    
    