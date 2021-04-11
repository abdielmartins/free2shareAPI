from . import db


class CardModel(db.Model):
    __tablename__ = "cards"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    promotion_link = db.Column(db.String, nullable=False)
    card_banner_link = db.Column(db.String, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    author = db.relationship("UserModel", backref=db.backref("card_list", lazy="joined"), lazy="joined")
