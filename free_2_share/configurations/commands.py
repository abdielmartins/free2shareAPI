from flask import Flask
from flask.cli import AppGroup
from click import argument
from free_2_share.models.user_model import UserModel
from free_2_share.models.card_model import CardModel
from free_2_share.models.favorite_model import FavoriteModel


def init_app(app: Flask):
    cli_db_group = AppGroup('user')

    session = Flask.cirr