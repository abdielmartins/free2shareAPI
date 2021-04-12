from flask import Flask
from flask_restful import Api


def init_app(app: Flask):
    api = Api(app)
    from free_2_share.views.card_view import Card, AllCards
    api.add_resource(AllCards, "/api/card")
    api.add_resource(Card, "/api/card", endpoint="/card", methods=["POST"])
    api.add_resource(Card,
                     "/api/card/<int:card_id>",
                     endpoint="/card/<int:user_id>",
                     methods=["GET", "PATCH", "DELETE"],
                     )