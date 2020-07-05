from . import db


class MessageModel(db.Model):
    __tablename__ = "message"
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(1000))
    sender_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    receiver_id = db.Column(db.Integer, db.ForeignKey("user.id"))
