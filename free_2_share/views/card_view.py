from flask_restful import Resource, reqparse, current_app
from http import HTTPStatus

from free_2_share.models.card_model import CardModel
from free_2_share.schema.card_schema import card_schema, cards_schema


class AllCards(Resource):
    def get(self):
        all_cards = CardModel.query.all()
        serializer = cards_schema.dump(all_cards)
        return {"data": serializer}, HTTPStatus.OK


class Card(Resource):
    def get(self, card_id):
        card = CardModel.query.get(card_id)
        serializer = card_schema.dump(card)
        return {"data": serializer}, HTTPStatus.OK

    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument("name", type=str, required=True)
        parse.add_argument("promotion_link", type=str, required=True)
        parse.add_argument("card_banner_link", type=str, required=True)
        parse.add_argument("user_id", type=int, required=True)

        args = parse.parse_args()

        new_card = CardModel(**args)
        session = current_app.db.session
        session.add(new_card)
        session.commit()
        serializer = card_schema.dump(new_card)
        return {"data": serializer}, HTTPStatus.OK

    def patch(self, card_id):
        parse = reqparse.RequestParser()
        parse.add_argument("name", type=str)
        parse.add_argument("promotion_link", type=str)
        parse.add_argument("card_banner_link", type=str)

        args = parse.parse_args()

        card = CardModel.query.get_or_404(card_id)

        for key, value in args.items():
            if value:
                setattr(card, key, value)

        session = current_app.db.session
        session.add(card)
        session.commit()
        serializer = card_schema.dump(card)
        return {"data": serializer}, HTTPStatus.OK

    def delete(self, card_id):
        card = CardModel.query.get_or_404(card_id)
        session = current_app.db.session
        session.delete(card)
        session.commit()