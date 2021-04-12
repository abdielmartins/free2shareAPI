from . import ma
from free_2_share.models.user_model import UserModel


class UserSchema(ma.Schema):
    class Meta:
        model = UserModel

    id = ma.Integer()
    name = ma.String()
    nickname = ma.String()
    email = ma.String()
    phone = ma.String()
    link_profile_picture = ma.String()
    bio = ma.String()
    # favorites_list = ma.List()


user_schema = UserSchema()
users_schema = UserSchema(many=True)