from . import db


class ClosureModel(db.Model):
    __tablename__ = "closure"
    id = db.Column(db.Integer, primary_key=True)
    ancestor = db.Column(db.Integer, db.ForeignKey("message.id"))
    descendant = db.Column(db.Integer, db.ForeignKey("message.id"))
     