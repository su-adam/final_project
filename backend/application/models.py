from application import db

class Locations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description= db.Column(db.String(30), nullable=False)

class Galleries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gallery_name = db.Column(db.String(30), nullable=False)
    informaiton = db.Column(db.String(30), nullable=False)
    fee = db.Column(db.String(30), nullable=False)
    location_id = db.Column(db.Integer, foreign_key=('location.id'), nullable=False)


    
    