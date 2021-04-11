from . import ma
from free_2_share.models.card_model import CardModel


class CardSchema(ma.Schema):
    class Meta:
        model = CardModel

    id = ma.Integer()
    name = ma.String()
    promotion_link = ma.String()
    card_banner_link = ma.String()
    user_id = ma.Integer()


card_schema = CardSchema()
cards_schema = CardSchema(many=True)