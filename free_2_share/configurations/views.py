from flask import Flask
from flask_restful import Api


def init_app(app: Flask):
    api = Api(app)

    from free_2_share.views.user_view import User, AllUsers
    from free_2_share.views.card_view import Card, AllCards

    api.add_resource(AllUsers, "/api/users")
    api.add_resource(User, "/api/user", endpoint="/user", methods=["POST"])
    api.add_resource(
        User,
        "/api/user/<int:user_id>",
        endpoint="/user/<int:user_id>",
        methods=["GET", "PATCH", "DELETE"],
    )

    api.add_resource(AllCards, "/api/card")
    api.add_resource(Card, "/api/card", endpoint="/card", methods=["POST"])
    api.add_resource(
        Card,
        "/api/card/<int:card_id>",
        endpoint="/card/<int:user_id>",
        methods=["GET", "PATCH", "DELETE"],
    )
