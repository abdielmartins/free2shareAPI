from flask import Flask
from flask.cli import AppGroup
from click import argument
from free_2_share.models.user_model import UserModel
from free_2_share.models.card_model import CardModel
from free_2_share.models.favorite_model import FavoriteModel


def init_app(app: Flask):
    cli_db_user = AppGroup('user')

    session = app.db.session

    @cli_db_user.command("create")
    @argument("quantity")
    def create_users(quantity):
        ...