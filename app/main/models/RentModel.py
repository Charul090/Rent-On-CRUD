from . import db


class RentModel(db.Model):
    __tablename__ = "rent"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    property_id = db.Column(db.Integer, db.ForeignKey("property.id"))
    booking_time = db.Column(db.DateTime)
    duration = db.Column(db.Integer)
