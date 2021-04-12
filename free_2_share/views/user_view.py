import http
from flask.globals import request, session
from flask_restful import Resource, reqparse, current_app
from http import HTTPStatus

from free_2_share.models.user_model import UserModel
from free_2_share.schema.user_schema import user_schema, users_schema


class AllUsers(Resource):
    def get(self):
        all_users = UserModel.query.all()
        serializer = users_schema.dump(all_users)

        return {"data": serializer}, HTTPStatus.OK


class User(Resource):
    def get(self, user_id):
        user = UserModel.query.get(user_id)
        serializer = user_schema.dump(user)

        return {"dump": serializer}, HTTPStatus.OK

    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument("name", type=str, required=True)
        parse.add_argument("nickname", type=str, required=True)
        parse.add_argument("email", type=str, required=True)
        parse.add_argument("password", type=str, required=True)
        parse.add_argument("phone", type=str, required=True)
        parse.add_argument("link_profile_picture", type=str, required=True)
        parse.add_argument("bio", type=str, required=True)

        kwargs = parse.parse_args()

        new_user = UserModel(
            name=kwargs.name,
            nickname=kwargs.nickname,
            email=kwargs.email,
            phone=kwargs.phone,
            link_profile_picture=kwargs.link_profile_picture,
            bio=kwargs.bio,
        )

        new_user.password = kwargs.password

        session = current_app.db.session
        session.add(new_user)
        session.commit()

        serializer = user_schema.dump(new_user)

        return {"data": serializer}, HTTPStatus.OK

    def patch(self, user_id):
        parse = reqparse.RequestParser()
        parse.add_argument("name", type=str)
        parse.add_argument("nickname", type=str)
        parse.add_argument("email", type=str)
        parse.add_argument("password", type=str)
        parse.add_argument("phone", type=str)
        parse.add_argument("link_profile_picture", type=str)
        parse.add_argument("bio", type=str)

        kwargs = parse.parse_args()

        user = UserModel.query.get_or_404(user_id)

        for key, value in kwargs.items():
            if value:
                if key != "password":
                    setattr(user, key, value)

        if kwargs.password:
            setattr(user, "password", kwargs.password)

        session = current_app.db.session
        session.add(user)
        session.commit()
        serializer = user_schema.dump(user)

        return {"data": serializer}, HTTPStatus.OK

    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        session = current_app.db.session
        session.delete(user)
        session.commit()

        return {"data": f"User {user_id} has successfully been deleted"}, HTTPStatus.OK