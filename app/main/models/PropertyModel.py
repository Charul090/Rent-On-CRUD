from . import db

class PropertyModel(db.Model):
    __tablename__="property"
    id = db.Column(db.Integer, primary_key = True)
    area = db.Column(db.Integer)
    amenities = db.Column(db.String(240))
    bedrooms = db.Column(db.Integer)
    furnishing = db.Column(db.Boolean)
    adderss = db.Column(db.String(200))
    price = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))