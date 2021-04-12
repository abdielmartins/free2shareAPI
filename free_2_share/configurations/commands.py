from flask import Flask
from flask.cli import AppGroup
from click import argument
from faker import Faker
from free_2_share.models.user_model import UserModel
from free_2_share.models.card_model import CardModel
from free_2_share.models.favorite_model import FavoriteModel

faker = Faker()


def init_app(app: Flask):
    cli_db_user = AppGroup('user')
    cli_db_card = AppGroup("card")
    session = app.db.session

    @cli_db_user.command("create")
    @argument("quantity")
    def create_users(quantity):
        for _ in range(int(quantity)):
            user = {
                "name": faker.unique.name(),
                "nickname": faker.unique.name(),
                "email": faker.unique.email(),
                "password": faker.password(),
                "phone": faker.phone_number(),
                "link_profile_picture": faker.image_url(),
                "bio": faker.paragraph(nb_sentences=2)
            }
            new_user: UserModel = UserModel(**user)
            session.add(new_user)
            if _ % 10 == 0:
                session.commit()
        session.commit()

    @cli_db_card.command("create")
    @argument("quantity")
    def create_cards(quantity):
        for _ in range(int(quantity)):
            card = dict(name=faker.unique.name(),
                        promotion_link=faker.image_url(),
                        card_banner_link=faker.image_url(),
                        user_id=_+1)
            new_card = CardModel(**card)
            session.add(new_card)
            if _ % 10 == 0:
                session.commit()
        session.commit()

    app.cli.add_command(cli_db_user)
    app.cli.add_command(cli_db_card)