from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    from free_2_share.models.user_model import UserModel
    from free_2_share.models.card_model import CardModel
    from free_2_share.models.favorite_model import FavoriteModel